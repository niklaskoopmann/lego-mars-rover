import pyttsx3
import config

engine = pyttsx3.init('espeak')

# volume as float from 0 to 1
engine.setProperty('volume', config.TTS_VOLUME)

# rate (words per minute) has to be an int between 1 and 200
engine.setProperty('rate', config.TTS_WORDS_PER_MINUTE)

def speak(text_to_say):
    engine.say(text_to_say)
    engine.runAndWait()

def water_found():
    speak("Water found!")

def stop_tts_engine():
    engine.stop()

speak("Voice output initialized!")