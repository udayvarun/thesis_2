import numpy as np
from utils.real_robot_mapper import Panda
from utils.move_position import move_to_position
from utils.calculate_q import calculate_q

Panda().move_to_start()

#initial_position = Panda().get_robot_position()

##Reach for cup
#goal_position = np.array([[0.7805, -0.04214, 0.6237, 0.6662],
#                          [-0.06911, -0.9974, 0.01909, 0.01705],
#                          [0.6213, -0.05801, -0.7814, -0.2516],
#                          [0, 0, 0, 1]])

#Reach for bottle
#goal_position = np.array([[0.9958, 0.0003533, 0.0915, 0.7214],
#                          [0.0003214, -1, 0.0003641, 0.03942],
#                          [0.0915, -0.0003331, -0.9958, -0.1145],
#                          [0, 0, 0, 1]])
#
#calculate_q(initial_position, goal_position, 'exp1', 10)

move_to_position('exp1', 10)

Panda().move_to_start()