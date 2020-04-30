#!/usr/bin/env python

"""
rover.py
This is the base script of Mars Science Laboratory Curiosity Rover (DHBW
Mosbach). It starts all the necessary threads and tears down all components
after the execution is cancelled.
"""

import threading
import time

import config
from Actuator.actuator_control import stop_driving
from Camera import water_detection
from Voice_Output import speak
from Voice_Recognition import voice_recognition

__author__ = "Niklas Koopmann"
__email__ = "nik.koopmann.17@lehre.mosbach.dhbw.de"
__version__ = "1.0.0"
__maintainer__ = "TBD"
__status__ = "Production"

# setup thread for camera capture
# callback is the function to say "Water found"
# -> passed as argument to camera_capture
camera_thread = threading.Thread(
    target=water_detection.camera_capture,
    args=(speak.water_found,))

# setup thread for voice input
voice_thread = threading.Thread(target=voice_recognition.recognize)

# start both threads
try:
    camera_thread.start()
    voice_thread.start()
except KeyboardInterrupt:
    pass

# after the threads are stopped, stop the tts engine
speak.stop_tts_engine()

# and stop all wheels
stop_driving()
