import numpy as np
from utils.real_robot_mapper import Panda
from utils.move_position import move_to_position
import time
from utils.calculate_q import calculate_q

Panda().move_to_start()

initial_position = Panda().get_robot_position()
# initial_position = np.array([-0.00867367069998331, -0.7859290811555426, 0.0014189809690487837, -2.356400179186334, 0.003559221795097906, 1.5683314154592496, 0.7770764079358842])
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