import numpy as np
from utils.real_robot_mapper import Panda
import time

Panda().move_to_start()

#goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
#                          [-0.9976, -0.05895, 0.0368, 0.01286],
#                          [0.05798, -0.998,-0.02681, 0.4007],
#                          [0, 0, 0, 1]])
#
#Panda().move_to_pose(goal_position)

goal_joint_position = np.array([0.10134937966289502, 1.4847908017194735, -0.2787609293678752, -0.1578170727081647, 0.8953194103837013, 3.1768402280410126, 1.6673921329669459])

Panda().move_to_joint_position(goal_joint_position)

time.sleep(5)

##Shake hand
#goal_position = np.array([[0.9996, 0.02393, -0.01562, 0.5821],
#                          [-0.01083, -0.1883, -0.9821, -0.6462],
#                          [-0.02644, 0.9818, -0.1879, 0.04599],
#                          [0, 0, 0, 1]])
#
#Panda().move_to_pose(goal_position)

goal_joint_position = np.array([-0.03521145015285536, 1.4726041290718213, -1.0796322818763098, -1.5118966272250536, -1.495872199030124, 2.8436253060897188, 2.1448536916422833])

Panda().move_to_joint_position(goal_joint_position)

time.sleep(5)

#goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
#                          [-0.9976, -0.05895, 0.0368, 0.01286],
#                          [0.05798, -0.998,-0.02681, 0.4007],
#                          [0, 0, 0, 1]])
#
#Panda().move_to_pose(goal_position)

goal_joint_position = np.array([0.10134937966289502, 1.4847908017194735, -0.2787609293678752, -0.1578170727081647, 0.8953194103837013, 3.1768402280410126, 1.6673921329669459])

Panda().move_to_joint_position(goal_joint_position)

time.sleep(5)

Panda().move_to_start()