import numpy as np
from utils.dataset_extractor import DataSet
from utils.real_robot_mapper import Panda

runtime = 5
frequency = 1e2

Panda().move_to_start()

q = np.load('./experiment_data_set/exp2.npy')
DataSet.joint_angles_plot(q, "./experiment_data_set/figures/exp2.png")

Panda().robot_mapper(q, runtime, frequency)
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)
print(joint_postion, cartesian_position)

Panda().move_to_start()