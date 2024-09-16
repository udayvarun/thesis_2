from utils.real_robot_mapper import Panda

Panda().move_to_start()
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)
print(joint_postion, cartesian_position)
