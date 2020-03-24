import brickpi3
import time

# set volatile addresses for attached BrickPis using their serial numbers
brickpi3.set_address(2, "07976FB6515035524E202020FF101B0C")
brickpi3.set_address(3, "45C31FAF514D3937304B2020FF15122B")

# instantiate both BrickPis
BP_drive = brickpi3.BrickPi3(2)
BP_steer = brickpi3.BrickPi3(3)

# test by reading values from created BrickPi objects
print(BP_drive.get_manufacturer())
print(BP_steer.get_manufacturer())
   
# get motor status for both MD
print(BP_drive.get_motor_status(BP_drive.PORT_D))
print(BP_steer.get_motor_status(BP_steer.PORT_D))
    
# reset all sensors/motors for the BrickPis
BP_drive.reset_all()
BP_steer.reset_all()
    
# start up motor MD for both BrickPis
BP_drive.reset_motor_encoder(BP_drive.PORT_D)
BP_steer.reset_motor_encoder(BP_steer.PORT_D)
BP_drive.set_motor_power(BP_drive.PORT_D, 50)
BP_steer.set_motor_power(BP_steer.PORT_D, 25)
#BP_drive.set_motor_dps(BP_drive.PORT_D, 100)
#BP_steer.set_motor_dps(BP_steer.PORT_D, 100)
   
# wait for some time
time.sleep(3)

# disable both motors again
BP_drive.set_motor_dps(BP_drive.PORT_D, 0)
BP_steer.set_motor_dps(BP_steer.PORT_D, 0)
BP_drive.set_motor_power(BP_drive.PORT_D, 0)
BP_steer.set_motor_power(BP_steer.PORT_D, 0)

#try:
    
    
#except IOError as error:
    #print(error)
#except brickpi3.FirmwareVersionError as error:
    #print(error)
#except Exception as e:
    #print("Communication with BrickPi3 unsuccessful " + str(e))