#!/usr/bin/env python

"""
config.py
This file of Mars Science Laboratory Curiosity Rover (DHBW Mosbach) contains
all the basic configuration for the different modules. This standard config is
recommended for the developed model.
"""

__author__ = "Niklas Koopmann"
__email__ = "nik.koopmann.17@lehre.mosbach.dhbw.de"
__version__ = "1.0.0"
__maintainer__ = "TBD"
__status__ = "Production"

# video capture configuration
VIDEO_CAPTURE_WIDTH = 1280  # pixels
VIDEO_CAPTURE_HEIGHT = 720  # pixels
VIDEO_CAPTURE_FRAMERATE = 60  # Hz/fps

# colour for object recognition
# blue lego brick: RGBA(0, 87, 166, 1)
TARGET_RED = 0
TARGET_GREEN = 87
TARGET_BLUE = 166
RECOGNITION_TOLERANCE = 10  # plus/minus on hue
MIN_S_V = 100  # min saturation and value

# text-to-speech configuration
TTS_VOLUME = 1.0  # on a scale from 0 to 1
TTS_WORDS_PER_MINUTE = 150

# BrickPi serial numbers (see BrickPi info file)
BP_DRIVE_FRONT_REAR_SN = "07976FB6515035524E202020FF101B0C"
BP_DRIVE_MIDDLE_SN = "45C31FAF514D3937304B2020FF15122B"
BP_STEER_SN = "84880DFD514D3937304B2020FF0A172A"

# speech recognition
WORDS_TO_RECOGNIZE = ["start", "stop", "move", "left", "right"]
PAUSE_THRESHOLD = 0.5  # in seconds

# rover movement
# idea: have weight of Rover in config and calculate req. motor power from it
DURATION_FORWARD = 3  # in seconds
MOTOR_POWER_LIMIT = 60  # per cent
MOTOR_TARGET_POWER = 25  # per cent
