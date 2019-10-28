import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

if(r.recognize_sphinx(audio) == 'start'):
    print("Mars Rover started!")
