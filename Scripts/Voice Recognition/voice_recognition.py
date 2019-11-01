import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()
snowboy_config = ("./Snowboy/ubuntu1404-x86_64-1.1.1", ["./Snowboy/Hey Rover.pmdl"])

def drive_forward():
    print("[DRIVE] Yes, Master! Driving...")

def stop_driving():
    print("[DRIVE] Yes, Master! Stopping...")

def turn_left():
    print("[DRIVE] Yes, Master! Turning left...")

def turn_right():
    print("[DRIVE] Yes, Master! Turning right...")

try:
    with m as source: r.adjust_for_ambient_noise(source)
    print("[VOICE] Set minimum energy threshold to {}".format(r.energy_threshold))
    print("[VOICE] Say something!")
    while True:
        with m as source: audio = r.listen(source, None, 2, snowboy_config)
        try:
            # recognize speech using Sphinx to interpret locally
            value = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print("[VOICE] [ERROR] Unknown Value!")
        except sr.RequestError as e:
            print("[VOICE] [ERROR] Speech Recognition Engine - Request not fulfilled; {0}".format(e))
except KeyboardInterrupt:
    pass
