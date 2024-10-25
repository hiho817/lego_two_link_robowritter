#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

def read_motor_inputs(filename):
    motor_inputs = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove any leading/trailing whitespace and split the line by commas
                angle_strings = line.strip().split(',')
                # Convert each string to a float
                motor_angle = [float(angle) for angle in angle_strings]
                # Append the motor angles to the list
                motor_inputs.append(motor_angle)
        # print(f"Motor inputs have been loaded from '{filename}'.")
        return motor_inputs
    except Exception as e:
        # print(f"An error occurred while reading the file: {e}")
        return None

def handle_arm(joint1, joint2, joint3,motor_inputs, ev3):
    arm_speed = 100 #deg/s
    pen_speed = 60  #deg/s
    pen_angle = [30, 0] #[down, up]
    change_write_path = [1, 4, 6] #日
    magic_offset = 5
    path_count = 0

    for angle in motor_inputs:
        joint1.run_target(arm_speed + magic_offset, angle[0], wait = False)
        joint2.run_target(arm_speed, angle[1], wait = False)
        while not (joint1.control.done() & joint2.control.done()):
            wait(1)
        current_path = angle[2]
        if((current_path not in change_write_path)):
            joint3.run_target(pen_speed, pen_angle[0], then=Stop.HOLD, wait=True)
        else:
            joint3.run_target(pen_speed, pen_angle[1], then=Stop.HOLD, wait=True)
        # if(int(current_path) == path_count):
        #     path_count += 1
        #     wait(1000)
        #     ev3.speaker.beep()
    
    #reset
    joint3.run_target(pen_speed, pen_angle[1], then=Stop.HOLD, wait=True)
    joint1.run_target(50, 0)
    joint2.run_target(50, 0)

def main():
    ev3 = EV3Brick()
    # ev3.speaker.beep()

    motor_inputs = read_motor_inputs('motor_inputs.txt')

    joint1 = Motor(Port.A, positive_direction = Direction.CLOCKWISE)
    joint1.reset_angle(0)
    joint1.hold()
    joint2 = Motor(Port.B, positive_direction = Direction.CLOCKWISE)
    joint2.reset_angle(0)
    joint2.hold()
    joint3 = Motor(Port.C, positive_direction = Direction.CLOCKWISE)
    joint3.reset_angle(0)
    joint3.hold()

    handle_arm(joint1, joint2, joint3, motor_inputs, ev3)

    ev3.speaker.beep()

if __name__ == "__main__":
    main()