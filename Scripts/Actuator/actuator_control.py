#!/usr/bin/env python

"""
actuator_control.py
This module of Mars Science Laboratory Curiosity Rover (DHBW Mosbach) implements
all the functions necessary to run the rover. Driving, stopping and rotating are
implemented as documented.
"""

__author__ = "Niklas Koopmann"
__email__ = "nik.koopmann.17@lehre.mosbach.dhbw.de"
__version__ = "1.0.0"
__maintainer__ = "TBD"
__status__ = "Production"

import time

import brickpi3
import config

#
# TODO:
# - Create lists of motor groups and iterate over it whenever suitable.
# - Add sleep duration as parameter to set_steering_orientation
# - Add factors for wheel power to drive_forward
#

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
# all driving motors
BP_drive_fr.set_motor_limits(BP_drive_fr.PORT_A, config.MOTOR_POWER_LIMIT, 200)
BP_drive_fr.set_motor_limits(BP_drive_fr.PORT_B, config.MOTOR_POWER_LIMIT, 200)
BP_drive_fr.set_motor_limits(BP_drive_fr.PORT_C, config.MOTOR_POWER_LIMIT, 200)
BP_drive_fr.set_motor_limits(BP_drive_fr.PORT_D, config.MOTOR_POWER_LIMIT, 200)
BP_drive_m.set_motor_limits(BP_drive_m.PORT_A, config.MOTOR_POWER_LIMIT, 200)
BP_drive_m.set_motor_limits(BP_drive_m.PORT_D, config.MOTOR_POWER_LIMIT, 200)

# set power limit (param 2, in per cent) and speed limit (param 3, in dps) for
# all steering motors -> way higher max dps because of high friction when
# turning wheels under load
BP_steer.set_motor_limits(BP_steer.PORT_A, config.MOTOR_POWER_LIMIT, 900)
BP_steer.set_motor_limits(BP_steer.PORT_B, config.MOTOR_POWER_LIMIT, 900)
BP_steer.set_motor_limits(BP_steer.PORT_C, config.MOTOR_POWER_LIMIT, 900)
BP_steer.set_motor_limits(BP_steer.PORT_D, config.MOTOR_POWER_LIMIT, 900)

# output all four motor orientations at startup for debug purposes
orientation_c = BP_steer.get_motor_encoder(BP_steer.PORT_C)
orientation_a = BP_steer.get_motor_encoder(BP_steer.PORT_A)
orientation_b = BP_steer.get_motor_encoder(BP_steer.PORT_B)
orientation_d = BP_steer.get_motor_encoder(BP_steer.PORT_D)
print("[DEBUG] A: %s; B: %s; C: %s; D: %s" %
      (orientation_a, orientation_b, orientation_c, orientation_d))


def set_steering_orientation(deg_a, deg_b, deg_c, deg_d):
    BP_steer.set_motor_position(BP_steer.PORT_A, deg_a)
    BP_steer.set_motor_position(BP_steer.PORT_B, deg_b)
    BP_steer.set_motor_position(BP_steer.PORT_C, deg_c)
    BP_steer.set_motor_position(BP_steer.PORT_D, deg_d)
    time.sleep(0.5)


# adjust all steering motors to straight position (0 degrees if assembled
# correctly)
set_steering_orientation(0, 0, 0, 0)

# If the steering motors are already close to a 0 degree orientation, the above
# functions do not take long. Change the time to sleep according to the time it
# will take to rotate to 0.
time.sleep(0.1)

print("[DRIVE] All BrickPis connected and running!")


def drive_forward():
    print("[DRIVE] Yes, Master! Driving...")

    # more power on rear wheels bc they lag behind otherwise
    BP_drive_fr.set_motor_power(
        BP_drive_fr.PORT_A, -config.MOTOR_TARGET_POWER * 1.5)
    BP_drive_fr.set_motor_power(BP_drive_fr.PORT_B, -config.MOTOR_TARGET_POWER)
    BP_drive_fr.set_motor_power(BP_drive_fr.PORT_C, config.MOTOR_TARGET_POWER)
    BP_drive_fr.set_motor_power(
        BP_drive_fr.PORT_D, config.MOTOR_TARGET_POWER * 1.5)
    BP_drive_m.set_motor_power(BP_drive_m.PORT_A, -config.MOTOR_TARGET_POWER)
    BP_drive_m.set_motor_power(BP_drive_m.PORT_D, config.MOTOR_TARGET_POWER)


# disable all motors and wait a little
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

    # first turn the wheels a little too far in order to overcome friction
    # between wheel and floor
    set_steering_orientation(75, -60, 60, -75)
    set_steering_orientation(60, -45, 45, -60)

    # drive for some time (iterations * sleep) and readjust steering motor
    # positions with every iteration
    # With a fully loaded corpus, the wheels are not able to turn while
    # standing! So the wheels are being driven a little - with different factors
    # than in the drive_forward function.
    for i in range(15):
        BP_drive_fr.set_motor_power(
            BP_drive_fr.PORT_A, config.MOTOR_TARGET_POWER * 1.25)
        BP_drive_fr.set_motor_power(
            BP_drive_fr.PORT_B, config.MOTOR_TARGET_POWER * 1.75)
        BP_drive_fr.set_motor_power(
            BP_drive_fr.PORT_C, config.MOTOR_TARGET_POWER * 1.5)
        BP_drive_fr.set_motor_power(
            BP_drive_fr.PORT_D, config.MOTOR_TARGET_POWER * 1.25)
        BP_drive_m.set_motor_power(
            BP_drive_m.PORT_A, config.MOTOR_TARGET_POWER * 1)
        BP_drive_m.set_motor_power(
            BP_drive_m.PORT_D, config.MOTOR_TARGET_POWER * 1)
        time.sleep(0.1)

        # not using set_steering_orientation to avoid stops
        BP_steer.set_motor_position(BP_steer.PORT_A, 45)
        BP_steer.set_motor_position(BP_steer.PORT_B, -45)
        BP_steer.set_motor_position(BP_steer.PORT_C, 45)
        BP_steer.set_motor_position(BP_steer.PORT_D, -45)

    stop_driving()

    # gradually adjust steering positions back to 0 (not using
    # set_steering_orientation to avoid stops)
    for i in range(3):
        BP_steer.set_motor_position(BP_steer.PORT_A, -45 + (15 * (i + 1)))
        BP_steer.set_motor_position(BP_steer.PORT_B, 30 - (10 * (i + 1)))
        BP_steer.set_motor_position(BP_steer.PORT_C, -30 + (10 * (i + 1)))
        BP_steer.set_motor_position(BP_steer.PORT_D, 45 - (15 * (i + 1)))
        drive_forward()
        time.sleep(0.1)

    stop_driving()


def turn_right():

    print("[DRIVE] Yes, Master! Turning right...")

    # first turn the wheels a little too far in order to overcome friction
    # between wheel and floor
    set_steering_orientation(75, -60, 60, -75)
    set_steering_orientation(60, -45, 45, -60)

    # drive for some time (iterations * sleep) and readjust steering motor
    # positions with every iteration
    # With a fully loaded corpus, the wheels are not able to turn while
    # standing! So the wheels are being driven a little - with different factors
    # than in the drive_forward function.
    for i in range(15):
        BP_drive_fr.set_motor_power(
            BP_drive_fr.PORT_A, -config.MOTOR_TARGET_POWER * 1.25)
        BP_drive_fr.set_motor_power(
            BP_drive_fr.PORT_B, -config.MOTOR_TARGET_POWER * 1.75)
        BP_drive_fr.set_motor_power(
            BP_drive_fr.PORT_C, -config.MOTOR_TARGET_POWER * 1.5)
        BP_drive_fr.set_motor_power(
            BP_drive_fr.PORT_D, -config.MOTOR_TARGET_POWER * 1.25)
        BP_drive_m.set_motor_power(
            BP_drive_m.PORT_A, -config.MOTOR_TARGET_POWER * 1)
        BP_drive_m.set_motor_power(
            BP_drive_m.PORT_D, -config.MOTOR_TARGET_POWER * 1)
        time.sleep(0.1)

        # not using set_steering_orientation to avoid stops
        BP_steer.set_motor_position(BP_steer.PORT_A, 45)
        BP_steer.set_motor_position(BP_steer.PORT_B, -45)
        BP_steer.set_motor_position(BP_steer.PORT_C, 45)
        BP_steer.set_motor_position(BP_steer.PORT_D, -45)

    stop_driving()

    # gradually adjust steering positions back to 0 (not using
    # set_steering_orientation to avoid stops)
    for i in range(3):
        BP_steer.set_motor_position(BP_steer.PORT_A, -45 + (15 * (i + 1)))
        BP_steer.set_motor_position(BP_steer.PORT_B, 30 - (10 * (i + 1)))
        BP_steer.set_motor_position(BP_steer.PORT_C, -30 + (10 * (i + 1)))
        BP_steer.set_motor_position(BP_steer.PORT_D, 45 - (15 * (i + 1)))
        drive_forward()
        time.sleep(0.1)

    stop_driving()


def test_drive():
    try:
        set_steering_orientation(0, 0, 0, 0)
        time.sleep(3)
        drive_forward()
        time.sleep(1)
        stop_driving()
        turn_left()
        turn_right()
        drive_forward()
        time.sleep(1)
        stop_driving()
    except brickpi3.FirmwareVersionError as error:
        print(error)
    except:
        print("Communication with BrickPi3 unsuccessful")
