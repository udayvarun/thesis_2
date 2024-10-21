import numpy as np
from utils.real_robot_mapper import Panda

goal_joint_position = np.array([0.14657515533891577, 1.5838447781278373, -1.5818225305216425, -0.38852626337635504, 1.5798191279371578, 3.1866216808557506, 0.8204606715504958])
Panda().move_to_joint_position(goal_joint_position)