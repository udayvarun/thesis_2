import numpy as np
from utils.dataset_extractor import DataSet
from utils.real_robot_mapper import Panda

def move_to_position(path, runtime):
    frequency = 1e2

    q = np.load(f'./experiment_data_set/{path}.npy')
    DataSet.joint_angles_plot(q, f"./experiment_data_set/figures/{path}.png")

    Panda().robot_mapper(q, runtime, frequency)
    joint_postion = Panda().get_robot_position()
    cartesian_position = Panda().forward_kinematics(joint_postion)
    print(joint_postion, cartesian_position)