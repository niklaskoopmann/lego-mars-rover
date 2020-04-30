#!/usr/bin/env python

"""
voice_recognition.py
This module of Mars Science Laboratory Curiosity Rover (DHBW Mosbach) implements
speech recognition, currently using Google's engine, in order to process the
voice commands specified in the configuration.
"""

import speech_recognition as sr

import config
import cv2  # only for key press detection
from Actuator.actuator_control import (drive_forward, stop_driving, turn_left,
                                       turn_right)
from Voice_Output.speak import speak

__author__ = "Niklas Koopmann"
__email__ = "nik.koopmann.17@lehre.mosbach.dhbw.de"
__version__ = "1.0.0"
__maintainer__ = "TBD"
__status__ = "Production"

#
# TODO:
# Add Snowboy hotword detection (trained "Hey Rover" on authors voice, see
# ./Snowboy/Hey_Rover.pmdl)
#

# speech_recognition documentation:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# setup a recognizer and a microphone
r = sr.Recognizer()
m = sr.Microphone()

# import snowboy configuration to wait for a hotword
# snowboy_config = ("./Snowboy/rpi-arm-raspbian-8.0-1.1.1",
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
    speak("Yes, Master!")
    drive_forward(config.MOTOR_TARGET_POWER)


def stop_driving_recognized():
    print("[VOICE] Stop command recognized.")
    stop_driving()
    speak("Yes, Master!")


def turn_left_recognized():
    print("[VOICE] Left turn command recognized.")
    speak("Yes, Master!")
    turn_left()


def turn_right_recognized():
    print("[VOICE] Right turn command recognized.")
    speak("Yes, Master!")
    turn_right()


# recognize function to be called in separate thread, evaluates input and calls
# corresponding function
def recognize():

    # set a threshold to triggering noise relative to ambient noise
    with m as source:
        r.adjust_for_ambient_noise(source)

    # initial console output
    print("[VOICE] Set minimum energy threshold to", r.energy_threshold)
    print("[VOICE] Say some things!")

    # run until broken by keypress or interrupt
    while True:

        # listen for ESC or Q key and break loop if pressed
        key = cv2.waitKey(1)
        if key == 27 or key == ord('q') or key == ord('Q'):
            break

        # listen for input on microphone, set a limit to quickly get on to the
        # evaluation after input (no command takes longer than two seconds)
        with m as source:
            # add Snowboy config to listen function for hotword detection
            audio = r.listen(source, phrase_time_limit=2)
        try:
            # recognize speech using Sphinx to interpret locally
            # (add keyword_entries=keywords argument for Sphinx)
            # using Google's engine for now because of the much higher accuracy
            value = r.recognize_google(audio).lower()

            # output recognized text -> subset of the keywords (when using
            # Sphinx)
            print("[VOICE] [DEBUG] You said:", value)

            # distinguish commands ("stop" used first to make rover stop
            # when in doubt) and call corresponding functions
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

        # raised when the input was not empty but could not be recognized
        except sr.UnknownValueError:
            print("[VOICE] [ERROR] Unknown Value!")

        except sr.RequestError as e:
            print("[VOICE] [ERROR] Speech Recognition Engine - " +
                  "Request not fulfilled; {0}".format(e))

        except KeyboardInterrupt:
            break
