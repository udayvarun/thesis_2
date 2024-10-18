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
#calculate_q(initial_position, goal_position, 'exp1_1_1', 10)

move_to_position('exp1_1_1', 10)

time.sleep(5)

#initial_position = Panda().get_robot_position()
##Reach for bottle
#goal_position = np.array([[0.9958, 0.0003533, 0.0915, 0.7214],
#                          [0.0003214, -1, 0.0003641, 0.03942],
#                          [0.0915, -0.0003331, -0.9958, -0.1145],
#                          [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp1_1_2', 5)

move_to_position('exp1_1_2', 5)

time.sleep(5)

#initial_position = Panda().get_robot_position()
#goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
#                          [-0.9976, -0.05895, 0.0368, 0.01286],
#                          [0.05798, -0.998,-0.02681, 0.4007],
#                          [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp1_1_3', 10)

move_to_position('exp1_1_3', 10)

time.sleep(5)

Panda().move_to_start()