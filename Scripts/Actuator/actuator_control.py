import brickpi3
import time

print ("Hello World!")

def reset_all_wheels(BP):
    BP.reset_motor_encoder(BP.PORT_A)
    BP.reset_motor_encoder(BP.PORT_B)
    BP.reset_motor_encoder(BP.PORT_C)
    BP.reset_motor_encoder(BP.PORT_D)
    
def turn_off_all_wheels(BP):
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_B, 0)
    BP.set_motor_power(BP.PORT_C, 0)
    BP.set_motor_power(BP.PORT_D, 0)
    BP.set_motor_dps(BP.PORT_A, 0)
    BP.set_motor_dps(BP.PORT_B, 0)
    BP.set_motor_dps(BP.PORT_C, 0)
    BP.set_motor_dps(BP.PORT_D, 0)

def drive_forward(brick_pi, dps):
    print("[DRIVE] Yes, Master! Driving...")
    brick_pi.set_motor_dps(brick_pi.PORT_A, -dps)
    brick_pi.set_motor_dps(brick_pi.PORT_B, -dps)
    brick_pi.set_motor_dps(brick_pi.PORT_C, dps)
    brick_pi.set_motor_dps(brick_pi.PORT_D, dps)

def stop_driving():
    print("[DRIVE] Yes, Master! Stopping...")

def turn_left():
    print("[DRIVE] Yes, Master! Turning left...")

def turn_right():
    print("[DRIVE] Yes, Master! Turning right...")
    
def test_drive():
    try:
        BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
        print("BrickPi3 connected and running")
        
        BP.reset_motor_encoder(BP.PORT_A)
        BP.reset_motor_encoder(BP.PORT_B)
        BP.reset_motor_encoder(BP.PORT_C)
        BP.reset_motor_encoder(BP.PORT_D)
        BP.set_motor_dps(BP.PORT_A, -180)
        BP.set_motor_dps(BP.PORT_B, -170)
        BP.set_motor_dps(BP.PORT_C, 170)
        BP.set_motor_dps(BP.PORT_D, 180)
        time.sleep(1)
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_power(BP.PORT_B, 0)
        BP.set_motor_power(BP.PORT_C, 0)
        BP.set_motor_power(BP.PORT_D, 0)
        BP.set_motor_dps(BP.PORT_A, 0)
        BP.set_motor_dps(BP.PORT_B, 0)
        BP.set_motor_dps(BP.PORT_C, 0)
        BP.set_motor_dps(BP.PORT_D, 0)
   
        time.sleep(1)
        
        BP.reset_motor_encoder(BP.PORT_A)
        BP.reset_motor_encoder(BP.PORT_B)
        BP.reset_motor_encoder(BP.PORT_C)
        BP.reset_motor_encoder(BP.PORT_D)
        BP.set_motor_dps(BP.PORT_A, 180)
        BP.set_motor_dps(BP.PORT_B, 170)
        BP.set_motor_dps(BP.PORT_C, -170)
        BP.set_motor_dps(BP.PORT_D, -180)
        time.sleep(1)
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_power(BP.PORT_B, 0)
        BP.set_motor_power(BP.PORT_C, 0)
        BP.set_motor_power(BP.PORT_D, 0)
        BP.set_motor_dps(BP.PORT_A, 0)
        BP.set_motor_dps(BP.PORT_B, 0)
        BP.set_motor_dps(BP.PORT_C, 0)
        BP.set_motor_dps(BP.PORT_D, 0)
        
        BP.reset_all()
        
    except brickpi3.FirmwareVersionError as error:
        print(error)
    except:
        print("Communication with BrickPi3 unsuccessful")
