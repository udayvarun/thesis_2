import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.real_robot_mapper import Panda

joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)

print(joint_postion, cartesian_position)