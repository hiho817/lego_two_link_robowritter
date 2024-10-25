#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
def read_motor_inputs(filename):
    motor_inputs = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove any leading/trailing whitespace and split the line by commas
            angle_strings = line.strip().split(' ')
            # Convert each string to a float
            motor_angle = [int(angle) for angle in angle_strings]
            # Append the motor angles to the list
            motor_inputs.append(motor_angle)
    # print(f"Motor inputs have been loaded from '{filename}'.")
    return motor_inputs
# Initialize motors
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)

def handle_arm(joint1, joint2, joint3,motor_inputs, ev3):
    arm_speed = 100 #deg/s
    pen_speed = 60  #deg/s

    for angle in motor_inputs:
        joint1.run_target(arm_speed, angle[0], wait = False)
        joint2.run_target(arm_speed, angle[1], wait = False)
        joint3.run_target(pen_speed, angle[2], then=Stop.HOLD, wait=True)
        while not (joint1.control.done() & joint2.control.done()):
            wait(1)

ev3 = EV3Brick()
ev3.speaker.beep()
# Open a file to write the angles
motor_inputs = read_motor_inputs('motor_angles.txt')
motor_a = Motor(Port.A, positive_direction = Direction.CLOCKWISE)
motor_a.reset_angle(0)
motor_a.hold()
motor_b = Motor(Port.B, positive_direction = Direction.CLOCKWISE)
motor_b.reset_angle(0)
motor_b.hold()
motor_c = Motor(Port.C, positive_direction = Direction.CLOCKWISE)
motor_c.reset_angle(0)
motor_c.hold()
handle_arm(motor_a, motor_b, motor_c, motor_inputs, ev3)


ev3.speaker.say("fuck that shit")