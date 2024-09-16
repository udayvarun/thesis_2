from utils.robot_synergy_input import minimize_dataset
import pickle as pk
import numpy as np
from utils.dataset_extractor import DataSet
from utils.interpolate_array import interpolate
from utils.real_robot_mapper import Panda
import time

runtime = 5
frequency = 1e2

start_time = time.time()
pca_reload = pk.load(open("utils/pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
min = minimize_dataset(pca_components, runtime*5)

Panda().move_to_start()

initial_position = Panda().get_robot_position()

#Hai
goal_position = np.array([[-0.2015, -0.9686, 0.1455, 0.4913],
                          [0.7821, -0.2485, -0.5714, -0.3648],
                          [0.5897, -0.001299, 0.8076, 0.7569],
                          [0, 0, 0, 1]])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

DataSet.joint_angles_plot(q_optimal)
new_q_optimal = interpolate(q_optimal, int(runtime * frequency))
DataSet.joint_angles_plot(new_q_optimal)
total_time= time.time()-start_time
print(f"Total_time = {total_time}")

start_time = time.time()
Panda().robot_mapper(new_q_optimal,runtime, frequency)
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)

total_time= time.time()-start_time
print(f"Total_time = {total_time}")
print(joint_postion, cartesian_position)

Panda().move_to_start()