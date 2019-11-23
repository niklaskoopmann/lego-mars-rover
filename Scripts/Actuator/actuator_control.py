#import brickpi3
import time

print ("Hello World!")

def test_drive():
    try:
        BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
        print("BrickPi3 connected and running")
        BP.reset_motor_encoder(BP.PORT_A)
        BP.set_motor_dps(BP.PORT_A, 900)
        time.sleep(1)  # delay for 1 second (20ms) to reduce the Raspberry Pi CPU load.
        print(BP.get_motor_status(BP.PORT_A))
        time.sleep(1)
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_dps(BP.PORT_A, 0)
    
    except brickpi3.FirmwareVersionError as error:
        print(error)
    except:
        print("Communication with BrickPi3 unsuccessful")

def drive_forward():
    print("[DRIVE] Yes, Master! Driving...")

def stop_driving():
    print("[DRIVE] Yes, Master! Stopping...")

def turn_left():
    print("[DRIVE] Yes, Master! Turning left...")

def turn_right():
    print("[DRIVE] Yes, Master! Turning right...")
