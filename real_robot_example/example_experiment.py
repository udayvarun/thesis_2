import numpy as np
from real_robot_mapper_example import Panda


Panda().robot_mapper(np.pi * 2)
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)

print(joint_postion, cartesian_position)