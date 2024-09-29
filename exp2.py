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

#Shake hand
goal_position = np.array([[0.9996, 0.02393, -0.01562, 0.5821],
                          [-0.01083, -0.1883, -0.9821, -0.6462],
                          [-0.02644, 0.9818, -0.1879, 0.04599],
                          [0, 0, 0, 1]])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()


new_q_optimal = interpolate(q_optimal, int(runtime * frequency))
DataSet.joint_angles_plot(new_q_optimal, "./figures/exp2.png")
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