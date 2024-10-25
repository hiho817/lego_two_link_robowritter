#!/usr/bin/env python3
from visual_kinematics.RobotSerial import RobotSerial
from visual_kinematics.RobotTrajectory import RobotTrajectory
from visual_kinematics.Frame import Frame
import numpy as np
from math import pi

def point2frame(points):

    euler_angles = np.array([0., 0., 0.])
    # Create frames using a list comprehension
    frames = [Frame.from_euler_3(euler_angles, pos) for pos in points]

    return frames

def cal_inverse_kinematic(robot, points):
    frames = point2frame(points)
    time_points = time_points = np.arange(0.0, len(frames), 1.0)

    trajectory = RobotTrajectory(robot, frames, time_points)

    inter_values, inter_time_points = trajectory.interpolate(num_segs=300, motion="lin", method="linear")

    trajectory.show(motion="lin")
    

    motor_inputs = []
    for angle, time in zip(inter_values, inter_time_points):
        motor_angle = [ (angle[0] * 180 / pi) , ((angle[0] + angle[1]) * 180 / pi)  , int(time) ]
        motor_inputs.append(motor_angle)
        # print(motor_inputs)

    motor_inputs = np.array(motor_inputs)

    return motor_inputs

def main():
    np.set_printoptions(precision=4, suppress=True)

    dh_params = np.array([[0., .09, 0., 0.],
                          [0., .17, 0., 0.],
                          [0., 0., 0., 0.]])
    
    #workspace
    # points = [
    # np.array([[0.08], [-0.18], [0]]),
    # np.array([[0.08], [-0.08], [0]]),
    # np.array([[0.16], [-0.08], [0]]),
    # np.array([[0.16], [-0.18], [0]]),
    # np.array([[0.08], [-0.18], [0]]),
    # ]

    ######### "日" #########(1, 4, 6)
    # points = [
    # np.array([[0.10], [0.18], [0]]),
    # np.array([[0.10], [0.08], [0]]),

    # np.array([[0.10], [0.18], [0]]),
    # np.array([[0.16], [0.18], [0]]),
    # np.array([[0.16], [0.08], [0]]),

    # np.array([[0.10], [0.13], [0]]),
    # np.array([[0.18], [0.13], [0]]),

    # np.array([[0.10], [0.08], [0]]),
    # np.array([[0.18], [0.08], [0]])
    # ]
    
    ######### "春" #########(1, 3, 5, 11, 13, 15, 18, 20, 22)
    points = [
        np.array([[0.100], [0.170], [0.0]]),
        np.array([[0.150], [0.170], [0.0]]),

        np.array([[0.100], [0.155], [0.0]]),
        np.array([[0.150], [0.155], [0.0]]),

        np.array([[0.101], [0.140], [0.0]]),
        np.array([[0.154], [0.140], [0.0]]),

        np.array([[0.126], [0.18], [0.0]]),
        np.array([[0.124], [0.158], [0.0]]),
        np.array([[0.12], [0.14], [0.0]]),
        np.array([[0.115], [0.127], [0.0]]),
        np.array([[0.109], [0.117], [0.0]]),
        np.array([[0.1], [0.108], [0.0]]),

        np.array([[0.130], [0.140], [0.0]]),
        np.array([[0.16], [0.117], [0.0]]),

        np.array([[0.117], [0.116], [0.0]]),
        np.array([[0.117], [0.08], [0.0]]),

        np.array([[0.117], [0.116], [0.0]]),
        np.array([[0.136], [0.114], [0.0]]),
        np.array([[0.136], [0.08], [0.0]]),

        np.array([[0.136], [0.097], [0.0]]),
        np.array([[0.117], [0.097], [0.0]]),

        np.array([[0.136], [0.08], [0.0]]),
        np.array([[0.117], [0.08], [0.0]]),
    ]
    points[1]*=1.1
    points[0]*=1.1

    

    robot = RobotSerial(dh_params)

    motor_inputs = cal_inverse_kinematic(robot, points)
    
    np.savetxt('C:\workspace\LEGO\RoboWriter\motor_inputs.txt', motor_inputs, fmt='%.3f', delimiter=',')

    # print(motor_inputs)

if __name__ == "__main__":
    main()
