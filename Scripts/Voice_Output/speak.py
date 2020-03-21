import pyttsx3

engine = pyttsx3.init('espeak')

# volume as float from 0 to 1
engine.setProperty('volume',1.0)

# rate (words per minute) has to be an int between 1 and 200
engine.setProperty('rate',150)

def speak(text_to_say):
    engine.say(text_to_say)
    engine.runAndWait()

speak("Nice tits, get in the truck.")
#speak("Yes, Master.")
#speak("Water found!")
#speak("The quick brown fox jumped over the lazy dog.")

engine.stop()
