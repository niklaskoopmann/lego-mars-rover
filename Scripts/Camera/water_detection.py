# using picamera
# basic tutorial: https://maker.pro/raspberry-pi/tutorial/how-to-create-object-detection-with-opencv

#
# TODO: Maybe start a timer once water has been found.
# Until the timer is up, block water_in_sight function
# to avoid "spam" from the speak package.
#

import cv2
import numpy as np
import time
from picamera import PiCamera
from picamera.array import PiRGBArray
# from skimage import morphology
import config

# create instance of PiCamera from the drivers
camera = PiCamera()

# setup constants for this script
camera.resolution = (config.VIDEO_CAPTURE_WIDTH, config.VIDEO_CAPTURE_HEIGHT)
camera.framerate = config.VIDEO_CAPTURE_FRAMERATE

# ?
rawCapture = PiRGBArray(camera, size=(config.VIDEO_CAPTURE_WIDTH, config.VIDEO_CAPTURE_HEIGHT))

# wait for camera to fully start up
time.sleep(0.1)

# function to continuously capture video from camera
# calls "callback_func" once an object of the desired colour is in the frame
def camera_capture(callback_func):

    # keep track of whether water is currently in sight
    water_in_sight = False

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        image = frame.array
        hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        bgr = [config.TARGET_BLUE, config.TARGET_GREEN, config.TARGET_RED]
        hueThreshold = config.RECOGNITION_TOLERANCE
        hsvColor = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]

        # define min/max HSV colours for detection
        minHSV = np.array([hsvColor[0] - hueThreshold, 80, 80])
        maxHSV = np.array([hsvColor[0] + hueThreshold, 255, 255])

        # filter out everything that is not within tolerance
        mask = cv2.inRange(hsvImage, minHSV, maxHSV)

        # dilate and erode (too much for the current Raspberry Pi)
        #erodeElement = cv2.getStructuringElement(cv2.MORPH_RECT,(11,11))
        #dilateElement = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        #cv2.erode(mask, mask, erodeElement)
        #cv2.dilate(mask, mask, dilateElement)

        #thresh = cv2.threshold(mask, 240, 255, cv2.THRESH_BINARY_INV)[1]

        # result = cv2.bitwise_and(image, image, mask=mask)

        # find contours in the frame to estimate number of water objects
        (cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        #mask = cv2.drawContours(mask, cnts, -1, (240, 0, 159), 3)

        # if at least one contour was found, water is in the frame
        if len(cnts) > 0 and callback_func and not water_in_sight:
            water_in_sight = True
            callback_func()
        elif len(cnts) == 0:
            water_in_sight = False

        if water_in_sight:
            cv2.putText(image, "WATER FOUND", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        cv2.imshow("image", image)
        #cv2.imshow("clean", cleanmask)
        # cv2.imshow("result", result)

        rawCapture.truncate(0)

        # listen for ESC or Q key and break loop if pressed
        key = cv2.waitKey(1)
        if key == 27 or key == ord('q') or key == ord('Q'):
            break

    cv2.destroyAllWindows()
