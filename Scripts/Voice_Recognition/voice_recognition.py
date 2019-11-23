import speech_recognition as sr
from Voice_Output.speak import speak
from Actuator.actuator_control import drive_forward, stop_driving, turn_left, turn_right


r = sr.Recognizer()
m = sr.Microphone()
snowboy_config = ("./Snowboy/rpi-arm-raspbian-8.0-1.1.1", ["./Snowboy/Hey Rover.pmdl"])

def drive_forward_recognized():
    print("[VOICE] Drive command recognized.")
    drive_forward()
    speak("Yes, Master! I shall drive...")

def stop_driving_recognized():
    print("[VOICE] Stop command recognized.")
    stop_driving()
    speak("Yes, Master! I will stop...")

def turn_left_recognized():
    print("[VOICE] Left turn command recognized.")
    turn_left()
    speak("Yes, Master! I am turning left...")

def turn_right_recognized():
    print("[VOICE] Right turn command recognized.")
    turn_right()
    speak("Yes, Master! I am turning right...")


def recognize():
    try:
        with m as source: r.adjust_for_ambient_noise(source)
        print("[VOICE] Set minimum energy threshold to {}".format(r.energy_threshold))
        print("[VOICE] Say something!")
        while True:
            with m as source: audio = r.listen(source, 10, 3) # add Snowboy config here!
            try:
                # recognize speech using Sphinx to interpret locally
                value = r.recognize_sphinx(audio)
    
                if "stop" in value:
                    stop_driving_recognized()
                elif "start" in value:
                    drive_forward_recognized()
                elif "move" in value:
                    if "left" in value:
                        turn_left_recognized()
                    elif "right" in value:
                        turn_right_recognized()
                    else:
                        raise sr.UnknownValueError("[VOICE] [ERROR] Direction not recognized.")
                else:
                    raise sr.UnknownValueError("[VOICE] [ERROR] Input not recognized.")
    
            except sr.UnknownValueError:
                print("[VOICE] [ERROR] Unknown Value!")
            except sr.RequestError as e:
                print("[VOICE] [ERROR] Speech Recognition Engine - Request not fulfilled; {0}".format(e))
    except KeyboardInterrupt:
        pass
