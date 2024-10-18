import numpy as np
from utils.map_to_robot_simulation import map_to_robot
import time
from utils.calculate_q import calculate_q

# Panda().move_to_start()

initial_position = np.array([-0.00867367069998331, -0.7859290811555426, 0.0014189809690487837, -2.356400179186334, 0.003559221795097906, 1.5683314154592496, 0.7770764079358842])
# initial_position = Panda().get_robot_position()
goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
                          [-0.9976, -0.05895, 0.0368, 0.01286],
                          [0.05798, -0.998,-0.02681, 0.4007],
                          [0, 0, 0, 1]])
calculate_q(initial_position, goal_position, 'exp3_2_1', 10, 6, 10)

map_to_robot('exp3_2_1', 10)

# [ 0.09716867  1.48433345 -0.23680977 -0.15389766  0.83117871  3.18532188
#   1.70467048] 7 50
# [ 0.98102371 -1.75947782 -2.89730111 -3.0718003   1.52449856  2.51959141
#   2.89730086] 4 50
# [-2.89730004 -1.31578573 -2.84931011 -0.0698     -0.92204531  2.80603439
#   2.89730001] 6 50
# [ 0.10189843  1.44140758 -0.05750118 -0.20747688  0.85980888  3.2154006
#   1.49830078] 7 200

time.sleep(5)

# initial_position = Panda().get_robot_position()
# goal_position = np.array([[0.0305, -0.9993, 0.02121, 0.6728],
#                     [0.9765, 0.02526, -0.2141, 0.05834],
#                     [0.2134, 0.02724, 0.9766, 0.8438],
#                     [0, 0, 0, 1]])
# calculate_q(initial_position, goal_position, 'exp3_2_2', 5, 3)

# map_to_robot('exp3_2_2', 5)

# time.sleep(5)

# initial_position = Panda().get_robot_position()
# goal_position = np.array([[0.0383, -0.02461, 0.999, 0.9191],
#                           [-0.9976, -0.05895, 0.0368, 0.01286],
#                           [0.05798, -0.998,-0.02681, 0.4007],
#                           [0, 0, 0, 1]])
# calculate_q(initial_position, goal_position, 'exp3_2_3', 5, 3)

# map_to_robot('exp3_2_3', 5)

# time.sleep(5)

# Panda().move_to_start()