#!/usr/bin/env python

"""
speak.py
This module of Mars Science Laboratory Curiosity Rover (DHBW Mosbach) implements
implements speech synthesis using pyttsx3 with espeak for the voice output.
"""

import pyttsx3

import config

__author__ = "Niklas Koopmann"
__email__ = "nik.koopmann.17@lehre.mosbach.dhbw.de"
__version__ = "1.0.0"
__maintainer__ = "TBD"
__status__ = "Production"

# initialize tts engine with espeak as a synthesizer
engine = pyttsx3.init('espeak')

# set volume as float from 0 to 1 from configuration
engine.setProperty('volume', config.TTS_VOLUME)

# set rate (words per minute) as int between 1 and 200 from configuration
engine.setProperty('rate', config.TTS_WORDS_PER_MINUTE)


# function to output any string via tts, halts the thread until output is
# finished
def speak(text_to_say):
    engine.say(text_to_say)
    engine.runAndWait()


# separate function to say "water found" to be used as callback for the object
# recognition thread
def water_found():
    speak("Water found!")


# stop function to be called on teardown of base script
def stop_tts_engine():
    engine.stop()


# when everything is set up, make sure the voice output can be heard
speak("Voice output initialized!")
