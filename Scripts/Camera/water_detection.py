#!/usr/bin/env python

"""
water_detection.py
This module of Mars Science Laboratory Curiosity Rover (DHBW Mosbach) implements
a hue-based object recognition of blue 1x1-LEGO-Bricks (3007).
"""

__author__      = "Niklas Koopmann"
__email__       = "nik.koopmann.17@lehre.mosbach.dhbw.de"
__version__     = "1.0.0"
__maintainer__  = "TBD"
__status__      = "Production"



#
# TODO: Maybe start a timer once water has been found.
# Until the timer is up, block water_in_sight function
# to avoid "spam" from the speak package.
#

import cv2
import numpy as np
import time

# using picamera
# basic tutorial: https://maker.pro/raspberry-pi/tutorial/how-to-create-object-detection-with-opencv
from picamera import PiCamera
from picamera.array import PiRGBArray

# from skimage import morphology # may be used for further image processing
import config

# create instance of PiCamera from the drivers -> automatically matches
# connected cam at CSI
camera = PiCamera()

# setup constants for this script from config file
camera.resolution = (config.VIDEO_CAPTURE_WIDTH, config.VIDEO_CAPTURE_HEIGHT)
camera.framerate = config.VIDEO_CAPTURE_FRAMERATE

# setup a raw input stream from camera
rawCapture = PiRGBArray(camera, size=(
    config.VIDEO_CAPTURE_WIDTH, config.VIDEO_CAPTURE_HEIGHT))

# wait a little for camera to fully start up
time.sleep(0.1)


# function to continuously capture video from camera
# calls "callback_func" once an object of the desired colour is in the frame
def camera_capture(callback_func):

    # keep track of whether water is currently in sight
    water_in_sight = False

    # startup camera capture and process each frame
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        # get current image array
        image = frame.array

        # convert image from bgr (blue, green, red) to hsv (hue, saturation, value) colour space
        hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # get target colour data and threshold for recognition from configuration
        bgr = [config.TARGET_BLUE, config.TARGET_GREEN, config.TARGET_RED]
        hueThreshold = config.RECOGNITION_TOLERANCE

        # convert target colour information from bgr (blue, green, red) to hsv (hue, saturation, value) colour space
        hsvColor = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]

        # define min/max hsv colours for detection
        minHSV = np.array([hsvColor[0] - hueThreshold, 100, 100])
        maxHSV = np.array([hsvColor[0] + hueThreshold, 255, 255])

        # filter out everything that is not within tolerance
        mask = cv2.inRange(hsvImage, minHSV, maxHSV)

        # dilate and erode (too much for the current Raspberry Pi)
        #erodeElement = cv2.getStructuringElement(cv2.MORPH_RECT,(11,11))
        #dilateElement = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        #cv2.erode(mask, mask, erodeElement)
        #cv2.dilate(mask, mask, dilateElement)

        # find contours in the frame to filter out some noise and roughly estimate number of water objects
        (cnts, _) = cv2.findContours(mask.copy(),
                                     cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        #mask = cv2.drawContours(mask, cnts, -1, (240, 0, 159), 3)

        # if at least one contour was found, water is expected to be in the frame
        # water_in_sight is used to avoid "spam" while water stays in sight
        if len(cnts) > 0 and callback_func and not water_in_sight:
            water_in_sight = True
            callback_func()
        elif len(cnts) == 0:
            water_in_sight = False

        # when water is in the picture, add some text to it
        if water_in_sight:
            cv2.putText(image, "WATER FOUND", (40, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # display the current image
        cv2.imshow("image", image)

        # truncate (throw out) all of the raw contents
        rawCapture.truncate(0)

        # listen for ESC or Q key and break loop if pressed
        key = cv2.waitKey(1)
        if key == 27 or key == ord('q') or key == ord('Q'):
            break

    # after execution destroy all the output windows
    cv2.destroyAllWindows()
