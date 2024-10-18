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

#goal_position = np.array([[0.0305, -0.9993, 0.02121, 0.6728],
#                    [0.9765, 0.02526, -0.2141, 0.05834],
#                    [0.2134, 0.02724, 0.9766, 0.8438],
#                    [0, 0, 0, 1]])
#
#Panda().move_to_pose(goal_position)

goal_joint_position = np.array([0.7346598382958195, 1.4894877553906358, -2.28201947572582, -1.200193514978195, -1.0915415110806093, 2.354833096451229, 2.5619286512004])

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