import numpy as np
from utils.real_robot_mapper import Panda
import time

goal_joint_position = np.array([0.14657515533891577, 1.5838447781278373, -1.5818225305216425, -0.38852626337635504, 1.5798191279371578, 3.1866216808557506, 0.8204606715504958])
Panda().move_to_joint_position(goal_joint_position)

#Shake hand
goal_position = np.array([[0.9996, 0.02393, -0.01562, 0.5821],
                          [-0.01083, -0.1883, -0.9821, -0.6462],
                          [-0.02644, 0.9818, -0.1879, 0.04599],
                          [0, 0, 0, 1]])

Panda().move_to_pose(goal_position)

time.sleep(2)

goal_position = np.array([[-0.03248, -0.2398, 0.9703, 0.919],
                         [-0.01228, -0.9706, -0.2403, -0.09703],
                         [0.9994,-0.01972, 0.02858, 0.4165],
                         [0, 0, 0, 1]])
Panda().move_to_pose(goal_position)