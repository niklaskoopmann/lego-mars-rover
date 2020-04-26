# video capture configuration
VIDEO_CAPTURE_WIDTH = 1280 # pixels
VIDEO_CAPTURE_HEIGHT = 720 # pixels
VIDEO_CAPTURE_FRAMERATE = 60 # Hz/fps

# color for object recognition
# blue lego brick: RGBA(0, 87, 166, 1)
TARGET_RED = 0
TARGET_GREEN = 87
TARGET_BLUE = 166
RECOGNITION_TOLERANCE = 10 # plus/minus on hue value

# text-to-speech configuration
TTS_VOLUME = 1.0 # on a scale from 0 to 1
TTS_WORDS_PER_MINUTE = 150

# BrickPi serial numbers (see BrickPi info file)
BP_DRIVE_FRONT_REAR_SN = "07976FB6515035524E202020FF101B0C"
BP_DRIVE_MIDDLE_SN = "45C31FAF514D3937304B2020FF15122B"
BP_STEER_SN = "84880DFD514D3937304B2020FF0A172A"

# speech recognition
WORDS_TO_RECOGNIZE = ["start", "stop", "move", "left", "right"]
PAUSE_THRESHOLD = 0.5 # in seconds

# rover movement
DURATION_FORWARD = 3 # in seconds
MOTOR_POWER_LIMIT = 40 # per cent
MOTOR_TARGET_POWER = 25 # per cent
