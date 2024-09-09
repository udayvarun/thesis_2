from utils.robot_synergy_input import minimize_dataset
import pickle as pk
import numpy as np
from utils.dataset_extractor import DataSet
from utils.interpolate_array import interpolate
from utils.real_robot_mapper import Panda
import time
start_time = time.time()
pca_reload = pk.load(open("utils/pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
min = minimize_dataset(pca_components, 50)

Panda().move_to_start()

initial_position = Panda().get_robot_position()

#goal_position = np.array([[0.2091, 0.1494, 0.9664, 0.9337],
#                          [0.4318,0.9859, -0.1617, -0.08624],
#                          [-0.9769,0.07555,0.1997,0.3445],
#                          [0, 0, 0, 1]])

goal_position = np.array([[-0.1055, 0.2828, 0.9533, 0.7498],
                          [ 0.8206, -0.5168, 0.2441, 0.5587],
                          [0.5617, 0.8081, -0.1776, 0.3542],
                          [0, 0, 0, 1]])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

DataSet.joint_angles_plot(q_optimal)
new_q_optimal = interpolate(q_optimal, 25000)
DataSet.joint_angles_plot(new_q_optimal)
total_time= time.time()-start_time
print(f"Total_time = {total_time}")

Panda().robot_mapper(new_q_optimal,50)
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)

print(joint_postion, cartesian_position)