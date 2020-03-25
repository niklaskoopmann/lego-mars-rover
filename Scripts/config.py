# video capture configuration
VIDEO_CAPTURE_WIDTH = 1280 # pixels
VIDEO_CAPTURE_HEIGHT = 720 # pixels
VIDEO_CAPTURE_FRAMERATE = 60 # Hz/fps

# color for object recognition
TARGET_RED = 0
TARGET_GREEN = 87
TARGET_BLUE = 166
RECOGNITION_TOLERANCE = 10 # plus/minus on hue value

# text-to-speech configuration
TTS_VOLUME = 1.0 # on a scale from 0 to 1
TTS_WORDS_PER_MINUTE = 150

# BrickPi serial numbers
BP_DRIVE_SN = "07976FB6515035524E202020FF101B0C" # see BrickPi-Info file
BP_STEER_SN = "45C31FAF514D3937304B2020FF15122B" # see BrickPi-Info file

# words to listen for
WORDS_TO_RECOGNIZE = ["start", "stop", "move", "left", "right"]

# rover movement
DURATION_FORWARD = 3 # in seconds
POWER_LIMIT = 25
