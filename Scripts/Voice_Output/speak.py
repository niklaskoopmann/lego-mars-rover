import pyttsx3
engine = pyttsx3.init()


def speak(text_to_say):
    engine.say(text_to_say)
    engine.runAndWait()


speak("Yes, Master.")