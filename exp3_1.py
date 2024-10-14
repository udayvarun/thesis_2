import numpy as np
from utils.real_robot_mapper import Panda
from utils.move_position import move_to_position
import time
from utils.calculate_q import calculate_q

Panda().move_to_start()

#initial_position = Panda().get_robot_position()
#goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
#                          [-0.9976, -0.05895, 0.0368, 0.01286],
#                          [0.05798, -0.998,-0.02681, 0.4007],
#                          [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp3_1_1', 10)

move_to_position('exp3_1_1', 10)

time.sleep(5)

#initial_position = Panda().get_robot_position()
#goal_position = np.array([[0.0305, -0.9993, 0.02121, 0.6728],
#                    [0.9765, 0.02526, -0.2141, 0.05834],
#                    [0.2134, 0.02724, 0.9766, 0.8438],
#                    [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp3_1_2', 5)

move_to_position('exp3_1_2', 5)

time.sleep(5)

#initial_position = Panda().get_robot_position()
#goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
#                          [-0.9976, -0.05895, 0.0368, 0.01286],
#                          [0.05798, -0.998,-0.02681, 0.4007],
#                          [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp3_1_3', 5)

move_to_position('exp3_1_3', 5)

time.sleep(5)

Panda().move_to_start()