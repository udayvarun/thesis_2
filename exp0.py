import numpy as np
from utils.real_robot_mapper import Panda
from utils.move_position import move_to_position
import time
from utils.calculate_q import calculate_q

Panda().move_to_start()

initial_position = Panda().get_robot_position()
goal_position = np.array([[<desired_matrix>],
                          [0, 0, 0, 1]])
calculate_q(initial_position, goal_position, 'exp0_1', 10)

move_to_position('exp0_0', 10)

time.sleep(5)

initial_position = Panda().get_robot_position()
goal_position = np.array([[<desired_matrix>],
                          [0, 0, 0, 1]])
calculate_q(initial_position, goal_position, 'exp0_2', 5)

move_to_position('exp0_2', 5)

time.sleep(5)

initial_position = Panda().get_robot_position()
goal_position = np.array([[<desired_matrix>],
                          [0, 0, 0, 1]])
calculate_q(initial_position, goal_position, 'exp0_3', 5)

move_to_position('exp0_3', 5)

time.sleep(5)

Panda().move_to_start()