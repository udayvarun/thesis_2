import numpy as np
from utils.real_robot_mapper import Panda
from utils.move_position import move_to_position
from utils.calculate_q import calculate_q
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

##Reach for bottle
#goal_position = np.array([[0.9958, 0.0003533, 0.0915, 0.7214],
#                          [0.0003214, -1, 0.0003641, 0.03942],
#                          [0.0915, -0.0003331, -0.9958, -0.1145],
#                          [0, 0, 0, 1]])
#
#Panda().move_to_pose(goal_position)

goal_joint_position = np.array([-0.523148800243411, 1.3312862962451937, 0.7010700294570069, -1.5641113046528288, -1.3308128481905404, 2.4757381047672693, 1.6670983050866366])

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