import numpy as np
from utils.real_robot_mapper import Panda
from utils.move_position import move_to_position
from utils.calculate_q import calculate_q
import time

Panda().move_to_start()

#initial_position = Panda().get_robot_position()
#goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
#                          [-0.9976, -0.05895, 0.0368, 0.01286],
#                          [0.05798, -0.998,-0.02681, 0.4007],
#                          [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp2_1_1', 10)

move_to_position('exp2_1_1', 10)

time.sleep(5)

#initial_position = Panda().get_robot_position()
##Shake hand
#goal_position = np.array([[0.9996, 0.02393, -0.01562, 0.5821],
#                          [-0.01083, -0.1883, -0.9821, -0.6462],
#                          [-0.02644, 0.9818, -0.1879, 0.04599],
#                          [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp2_1_2', 5)

move_to_position('exp2_1_2', 5)

time.sleep(5)

#initial_position = Panda().get_robot_position()
#goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
#                          [-0.9976, -0.05895, 0.0368, 0.01286],
#                          [0.05798, -0.998,-0.02681, 0.4007],
#                          [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp2_1_3', 5)

move_to_position('exp2_1_3', 5)

time.sleep(5)

Panda().move_to_start()