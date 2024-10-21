import numpy as np
from utils.real_robot_mapper import Panda
from utils.move_position import move_to_position
import time
from utils.calculate_q import calculate_q

goal_joint_position = np.array([0.14657515533891577, 1.5838447781278373, -1.5818225305216425, -0.38852626337635504, 1.5798191279371578, 3.1866216808557506, 0.8204606715504958])
Panda().move_to_joint_position(goal_joint_position)

#initial_position = Panda().get_robot_position()
#goal_position = np.array([[0.0305, -0.9993, 0.02121, 0.6728],
#                    [0.9765, 0.02526, -0.2141, 0.05834],
#                    [0.2134, 0.02724, 0.9766, 0.8438],
#                    [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp3_2_1', 3, 5, factor = 10)

move_to_position('exp3_2_1', 3)

time.sleep(2)

#initial_position = Panda().get_robot_position()
#goal_position = np.array([[-0.03248, -0.2398, 0.9703, 0.919],
#                         [-0.01228, -0.9706, -0.2403, -0.09703],
#                         [0.9994,-0.01972, 0.02858, 0.4165],
#                         [0, 0, 0, 1]])
#calculate_q(initial_position, goal_position, 'exp3_2_2', 3, 5, factor = 10)

move_to_position('exp3_2_2', 3)