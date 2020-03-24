import brickpi3
import time

print ("[DRIVE] Setting up actuator controls...")

# set volatile addresses for attached BrickPis using their serial numbers
brickpi3.set_address(2, "07976FB6515035524E202020FF101B0C")
brickpi3.set_address(3, "45C31FAF514D3937304B2020FF15122B")

# instantiate both BrickPis
BP_drive = brickpi3.BrickPi3(2)
BP_steer = brickpi3.BrickPi3(3)

# reset all sensors/motors for the BrickPis
BP_drive.reset_all()
BP_steer.reset_all()

print("[DRIVE] Both BrickPis connected and running!")

def reset_all_motors(BP):
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

def drive_forward(motor_pwr):
    print("[DRIVE] Yes, Master! Driving...")
    BP_drive.set_motor_power(BP_drive.PORT_A, -motor_pwr)
    BP_drive.set_motor_power(BP_drive.PORT_B, -motor_pwr)
    BP_drive.set_motor_power(BP_drive.PORT_C, motor_pwr)
    BP_drive.set_motor_power(BP_drive.PORT_D, motor_pwr)

def stop_driving():
    print("[DRIVE] Yes, Master! Stopping...")
    BP_drive.set_motor_power(BP_drive.PORT_A, 0)
    BP_drive.set_motor_power(BP_drive.PORT_B, 0)
    BP_drive.set_motor_power(BP_drive.PORT_C, 0)
    BP_drive.set_motor_power(BP_drive.PORT_D, 0)

def turn_left():
    print("[DRIVE] Yes, Master! Turning left...")
    BP_steer.set_motor_power(BP_steer.PORT_A, 25)
    BP_steer.set_motor_power(BP_steer.PORT_B, -25)
    BP_steer.set_motor_power(BP_steer.PORT_C, -25)
    BP_steer.set_motor_power(BP_steer.PORT_D, 25)
    time.sleep(0.5)
    BP_steer.set_motor_power(BP_steer.PORT_A, 0)
    BP_steer.set_motor_power(BP_steer.PORT_B, 0)
    BP_steer.set_motor_power(BP_steer.PORT_C, 0)
    BP_steer.set_motor_power(BP_steer.PORT_D, 0)

def turn_right():
    print("[DRIVE] Yes, Master! Turning right...")
    
def test_drive():
    try:
        drive_forward(25)
        time.sleep(3)
        stop_driving()
        turn_left()
        drive_forward(50)
        time.sleep(1)
        stop_driving()
    except brickpi3.FirmwareVersionError as error:
        print(error)
    except:
        print("Communication with BrickPi3 unsuccessful")

