#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# Initialize motors
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)

ev3 = EV3Brick()
ev3.speaker.beep()
# Open a file to write the angles
with open("motor_angles.txt", "w") as file:
    for _ in range(150):  # 100 iterations to log data for 10 seconds
        angle_a = motor_a.angle()
        angle_b = motor_b.angle()
        angle_c = motor_c.angle()
        
        # Write angles to file
        file.write(str(angle_a) + ' ' + str(angle_b) + ' ' + str(angle_c) + '\n')
        
        # Wait for 0.1 seconds (10Hz)
        time.sleep(0.1)

ev3.speaker.say("fuck that shit")