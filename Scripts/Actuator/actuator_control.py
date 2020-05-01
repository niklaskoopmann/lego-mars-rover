import brickpi3
import time
import config

print("[DRIVE] Setting up actuator controls...")

# set volatile addresses for attached BrickPis using their serial numbers
brickpi3.set_address(2, config.BP_DRIVE_FRONT_REAR_SN)
brickpi3.set_address(3, config.BP_STEER_SN)
brickpi3.set_address(4, config.BP_DRIVE_MIDDLE_SN)

print("[DRIVE] BrickPi addresses set.")

# instantiate all BrickPis
BP_drive_fr = brickpi3.BrickPi3(2)
BP_steer = brickpi3.BrickPi3(3)
BP_drive_m = brickpi3.BrickPi3(4)

print("[DRIVE] All BrickPis instantiated.")

# reset all sensors/motors for the BrickPis
BP_drive_fr.reset_all()
BP_steer.reset_all()
BP_drive_m.reset_all()

# set power limit (param 2, in per cent) and speed limit (param 3, in dps) for
# motors
BP_drive_fr.set_motor_limits(BP_drive_fr.PORT_A, config.MOTOR_POWER_LIMIT, 200)
BP_drive_fr.set_motor_limits(BP_drive_fr.PORT_B, config.MOTOR_POWER_LIMIT, 200)
BP_drive_fr.set_motor_limits(BP_drive_fr.PORT_C, config.MOTOR_POWER_LIMIT, 200)
BP_drive_fr.set_motor_limits(BP_drive_fr.PORT_D, config.MOTOR_POWER_LIMIT, 200)
BP_steer.set_motor_limits(BP_steer.PORT_A, config.MOTOR_POWER_LIMIT, 900)
BP_steer.set_motor_limits(BP_steer.PORT_B, config.MOTOR_POWER_LIMIT, 900)
BP_steer.set_motor_limits(BP_steer.PORT_C, config.MOTOR_POWER_LIMIT, 900)
BP_steer.set_motor_limits(BP_steer.PORT_D, config.MOTOR_POWER_LIMIT, 900)
BP_drive_m.set_motor_limits(BP_drive_m.PORT_A, config.MOTOR_POWER_LIMIT, 200)
BP_drive_m.set_motor_limits(BP_drive_m.PORT_D, config.MOTOR_POWER_LIMIT, 200)

# adjust steering motors to straight
BP_steer.set_motor_position(BP_steer.PORT_A, 0)
BP_steer.set_motor_position(BP_steer.PORT_B, 0)
BP_steer.set_motor_position(BP_steer.PORT_C, 0)
BP_steer.set_motor_position(BP_steer.PORT_D, 0)

time.sleep(0.1)

print("[DRIVE] All BrickPis connected and running!")


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


def drive_forward(support_direction=""):
    print("[DRIVE] Yes, Master! Driving...")
    
    if support_direction == "right":
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_A, -config.MOTOR_TARGET_POWER * 2)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_B, -config.MOTOR_TARGET_POWER * 2)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_C, config.MOTOR_TARGET_POWER)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_D, config.MOTOR_TARGET_POWER)
        BP_drive_m.set_motor_power(BP_drive_m.PORT_A, -config.MOTOR_TARGET_POWER)
        BP_drive_m.set_motor_power(BP_drive_m.PORT_D, 0)
    elif support_direction == "left":
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_A, -config.MOTOR_TARGET_POWER)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_B, -config.MOTOR_TARGET_POWER)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_C, config.MOTOR_TARGET_POWER * 2)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_D, config.MOTOR_TARGET_POWER * 2)
        BP_drive_m.set_motor_power(BP_drive_m.PORT_A, 0)
        BP_drive_m.set_motor_power(BP_drive_m.PORT_D, config.MOTOR_TARGET_POWER)
    else:
        #BP_steer.set_motor_position(BP_steer.PORT_A, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_B, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_C, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_D, 0)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_A, -config.MOTOR_TARGET_POWER * 1.5)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_B, -config.MOTOR_TARGET_POWER)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_C, config.MOTOR_TARGET_POWER)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_D, config.MOTOR_TARGET_POWER * 1.5)
        BP_drive_m.set_motor_power(BP_drive_m.PORT_A, -config.MOTOR_TARGET_POWER)
        BP_drive_m.set_motor_power(BP_drive_m.PORT_D, config.MOTOR_TARGET_POWER)
        #BP_steer.set_motor_position(BP_steer.PORT_A, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_B, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_C, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_D, 0)


def stop_driving():
    print("[DRIVE] Yes, Master! Stopping...")
    BP_drive_fr.set_motor_power(BP_drive_fr.PORT_A, 0)
    BP_drive_fr.set_motor_power(BP_drive_fr.PORT_B, 0)
    BP_drive_fr.set_motor_power(BP_drive_fr.PORT_C, 0)
    BP_drive_fr.set_motor_power(BP_drive_fr.PORT_D, 0)
    BP_drive_m.set_motor_power(BP_drive_m.PORT_A, 0)
    BP_drive_m.set_motor_power(BP_drive_m.PORT_D, 0)
    BP_steer.set_motor_power(BP_steer.PORT_A, 0)
    BP_steer.set_motor_power(BP_steer.PORT_B, 0)
    BP_steer.set_motor_power(BP_steer.PORT_C, 0)
    BP_steer.set_motor_power(BP_steer.PORT_D, 0)
    time.sleep(0.5)


def turn_left():

    print("[DRIVE] Yes, Master! Turning left...")

    # save all four motor orientations
    orientation_a = BP_steer.get_motor_encoder(BP_steer.PORT_A)
    orientation_b = BP_steer.get_motor_encoder(BP_steer.PORT_B)
    orientation_c = BP_steer.get_motor_encoder(BP_steer.PORT_C)
    orientation_d = BP_steer.get_motor_encoder(BP_steer.PORT_D)
    
    print("[DEBUG] A: %s; B: %s; C: %s; D: %s" % (orientation_a, orientation_b, orientation_c, orientation_d))

    BP_steer.set_motor_position(BP_steer.PORT_A, 75)
    BP_steer.set_motor_position(BP_steer.PORT_B, -60)
    BP_steer.set_motor_position(BP_steer.PORT_C, 60)
    BP_steer.set_motor_position(BP_steer.PORT_D, -75)
    time.sleep(0.5)
    BP_steer.set_motor_position(BP_steer.PORT_A, 60)
    BP_steer.set_motor_position(BP_steer.PORT_B, -45)
    BP_steer.set_motor_position(BP_steer.PORT_C, 45)
    BP_steer.set_motor_position(BP_steer.PORT_D, -60)
    
    for i in range(15):
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_A, config.MOTOR_TARGET_POWER * 1.7)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_B, config.MOTOR_TARGET_POWER * 0.75)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_C, config.MOTOR_TARGET_POWER * 1)
        BP_drive_fr.set_motor_power(BP_drive_fr.PORT_D, config.MOTOR_TARGET_POWER * 1.0)
        BP_drive_m.set_motor_power(BP_drive_m.PORT_A, config.MOTOR_TARGET_POWER * 0.75)
        BP_drive_m.set_motor_power(BP_drive_m.PORT_D, config.MOTOR_TARGET_POWER * 0.75)
        time.sleep(0.1)
        BP_steer.set_motor_position(BP_steer.PORT_A, 45)
        BP_steer.set_motor_position(BP_steer.PORT_B, -45)
        BP_steer.set_motor_position(BP_steer.PORT_C, 45)
        BP_steer.set_motor_position(BP_steer.PORT_D, -45)
        
    stop_driving()
    #BP_steer.set_motor_power(BP_steer.PORT_A, -config.MOTOR_TARGET_POWER * 1.5)
    #BP_steer.set_motor_power(BP_steer.PORT_D, -config.MOTOR_TARGET_POWER * 1.5)

    # front motors (B and C) need more power to turn bc of extra weight on them
    # -> use maximum allowed power
    #BP_steer.set_motor_power(BP_steer.PORT_B, config.MOTOR_POWER_LIMIT)
    #BP_steer.set_motor_power(BP_steer.PORT_C, config.MOTOR_POWER_LIMIT)

    # turning to 45° takes around 0.3 seconds
    time.sleep(0.5)

    
    
    # drive for some time (to really turn Rover)
    #drive_forward("left")
    #time.sleep(1)
    
    #stop_driving()

    # return motors to straight orientations
    BP_steer.set_motor_position(BP_steer.PORT_A, -15)
    BP_steer.set_motor_position(BP_steer.PORT_B, -15)
    BP_steer.set_motor_position(BP_steer.PORT_C, 15)
    BP_steer.set_motor_position(BP_steer.PORT_D, 15)
    time.sleep(0.5)
    BP_steer.set_motor_position(BP_steer.PORT_A, 0)
    BP_steer.set_motor_position(BP_steer.PORT_B, 0)
    BP_steer.set_motor_position(BP_steer.PORT_C, 0)
    BP_steer.set_motor_position(BP_steer.PORT_D, 0)
    
    # turn off motors again
    BP_steer.set_motor_power(BP_steer.PORT_A, 0)
    BP_steer.set_motor_power(BP_steer.PORT_B, 0)
    BP_steer.set_motor_power(BP_steer.PORT_C, 0)
    BP_steer.set_motor_power(BP_steer.PORT_D, 0)


def turn_right(): # todo: maybe turn by 45 deg from current pos?

    print("[DRIVE] Yes, Master! Turning right...")

    # save all four motor orientations
    orientation_a = BP_steer.get_motor_encoder(BP_steer.PORT_A)
    orientation_b = BP_steer.get_motor_encoder(BP_steer.PORT_B)
    orientation_c = BP_steer.get_motor_encoder(BP_steer.PORT_C)
    orientation_d = BP_steer.get_motor_encoder(BP_steer.PORT_D)
    
    print("[DEBUG] A: %s; B: %s; C: %s; D: %s" % (orientation_a, orientation_b, orientation_c, orientation_d))

    BP_steer.set_motor_position(BP_steer.PORT_A, orientation_a - 45)
    BP_steer.set_motor_position(BP_steer.PORT_B, orientation_b - 45)
    BP_steer.set_motor_position(BP_steer.PORT_C, orientation_c - 45)
    BP_steer.set_motor_position(BP_steer.PORT_D, orientation_d - 45)

    #BP_steer.set_motor_power(BP_steer.PORT_A, config.MOTOR_TARGET_POWER)
    #BP_steer.set_motor_power(BP_steer.PORT_D, config.MOTOR_TARGET_POWER)

    # front motors (B and C) need more power to turn bc of extra weight on them
    # -> use maximum allowed power
    #BP_steer.set_motor_power(BP_steer.PORT_B, -config.MOTOR_POWER_LIMIT)
    #BP_steer.set_motor_power(BP_steer.PORT_C, -config.MOTOR_POWER_LIMIT)

    # turning to 45° takes around 0.3 seconds
    time.sleep(0.5)

    # turn off motors again
    BP_steer.set_motor_power(BP_steer.PORT_A, 0)
    BP_steer.set_motor_power(BP_steer.PORT_B, 0)
    BP_steer.set_motor_power(BP_steer.PORT_C, 0)
    BP_steer.set_motor_power(BP_steer.PORT_D, 0)
    
    # drive for some time (to turn Rover)
    drive_forward("right")
    time.sleep(2)
    stop_driving()

    # return motors to straight orientations
    BP_steer.set_motor_position(BP_steer.PORT_A, 0)
    BP_steer.set_motor_position(BP_steer.PORT_B, 0)
    BP_steer.set_motor_position(BP_steer.PORT_C, 0)
    BP_steer.set_motor_position(BP_steer.PORT_D, 0)
    time.sleep(0.5)


def test_drive():
    try:
        #time.sleep(3)
        #for i in range(10):
         #   drive_forward()
          #  time.sleep(0.1)
        #stop_driving()
        BP_steer.set_motor_position(BP_steer.PORT_A, 0)
        BP_steer.set_motor_position(BP_steer.PORT_B, 0)
        BP_steer.set_motor_position(BP_steer.PORT_C, 0)
        BP_steer.set_motor_position(BP_steer.PORT_D, 0)
        time.sleep(0.5)
        turn_left()
        stop_driving()
        for i in range(3):
            #stop_driving()
            BP_steer.set_motor_position(BP_steer.PORT_A, -45+(15*(i+1)))
            BP_steer.set_motor_position(BP_steer.PORT_B, 30-(10*(i+1)))
            BP_steer.set_motor_position(BP_steer.PORT_C, -30+(10*(i+1)))
            BP_steer.set_motor_position(BP_steer.PORT_D, 45-(15*(i+1)))
            drive_forward()
            time.sleep(0.1)
        stop_driving()
        #BP_steer.set_motor_position(BP_steer.PORT_A, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_B, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_C, 0)
        #BP_steer.set_motor_position(BP_steer.PORT_D, 0)
        #stop_driving()
        #turn_right()
        #stop_driving()
    except brickpi3.FirmwareVersionError as error:
        print(error)
    except:
        print("Communication with BrickPi3 unsuccessful")
        

test_drive()
