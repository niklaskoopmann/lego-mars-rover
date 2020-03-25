import speech_recognition as sr
import cv2 # only for key press detection
from Voice_Output.speak import speak
from Actuator.actuator_control import drive_forward, stop_driving, turn_left, turn_right
import config

# speech_recognition documentation:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# setup a recognizer and a microphone
r = sr.Recognizer()
m = sr.Microphone()

# import snowboy configuration to wait for a hotword
#snowboy_config = ("./Snowboy/rpi-arm-raspbian-8.0-1.1.1",
# ["./Snowboy/Hey Rover.pmdl"])

# lower the pause threshold on the recognizer for quicker recognition
r.pause_threshold = config.PAUSE_THRESHOLD

# create array of tuples with the words to recognize and their weight
keywords = []
for word in config.WORDS_TO_RECOGNIZE:
    keywords.append((word, 1.0))

# functions to call when a command was recognized
def drive_forward_recognized():
    print("[VOICE] Drive command recognized.")
    drive_forward(config.MOTOR_TARGET_POWER)
    speak("Yes, Master! I shall drive...")

def stop_driving_recognized():
    print("[VOICE] Stop command recognized.")
    stop_driving()
    speak("Yes, Master! I will stop...")

def turn_left_recognized():
    print("[VOICE] Left turn command recognized.")
    turn_left()
    speak("Yes, Master! I am turning left...")

def turn_right_recognized():
    print("[VOICE] Right turn command recognized.")
    turn_right()
    speak("Yes, Master! I am turning right...")


def recognize():
    try:
        # set a threshold to triggering noise
        with m as source: r.adjust_for_ambient_noise(source)

        print("[VOICE] Set minimum energy threshold to", r.energy_threshold)
        print("[VOICE] Say some things!")

        while True:
            
            # listen for ESC or Q key and break loop if pressed
            key = cv2.waitKey(1)
            if key == 27 or key == ord('q') or key == ord('Q'):
                break
            
            with m as source:
                # add Snowboy config to listen function!
                audio = r.listen(source, phrase_time_limit=1)
            try:
                # recognize speech using Sphinx to interpret locally
                # using Google's engine for now because of the much higher accuracy
                value = r.recognize_google(audio)#, keyword_entries=keywords)

                # output recognized text -> subset of the keywords
                print("[VOICE] [DEBUG] You said:", value)

                # distinguish commands ("stop" used first to make rover stop
                # when in doubt)
                if "stop" in value:
                    stop_driving_recognized()
                elif "start" in value:
                    drive_forward_recognized()
                elif "move" in value:
                    if "left" in value:
                        turn_left_recognized()
                    elif "right" in value:
                        turn_right_recognized()
                    else:
                        raise sr.UnknownValueError("[VOICE] [ERROR] " +
                        "Direction not recognized.")
                else:
                    raise sr.UnknownValueError("[VOICE] [ERROR] " +
                    "Input not recognized.")

            except sr.UnknownValueError:
                print("[VOICE] [ERROR] Unknown Value!")

            except sr.RequestError as e:
                print("[VOICE] [ERROR] Speech Recognition Engine - " +
                "Request not fulfilled; {0}".format(e))

            except KeyboardInterrupt:
                break

    except KeyboardInterrupt:
        pass
