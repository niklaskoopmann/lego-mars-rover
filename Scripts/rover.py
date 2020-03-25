# system libs
import threading
import time

# user-defined libs
import config
from Camera import pycamtest
from Voice_Output import speak
from Voice_Recognition import voice_recognition

# setup thread for camera capture
# callback is the function to say "Water found"
# -> passed as argument to camera_capture
camera_thread = threading.Thread(
    target=pycamtest.camera_capture,
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
