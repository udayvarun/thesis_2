from utils.robot_synergy_input import minimize_dataset
import pickle as pk
import numpy as np
from utils.dataset_extractor import DataSet
from utils.interpolate_array import interpolate
from utils.real_robot_mapper import Panda
import time

runtime = 10
frequency = 1e2

start_time = time.time()
pca_reload = pk.load(open("utils/pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
min = minimize_dataset(pca_components, runtime*5)

Panda().move_to_start()

initial_position = Panda().get_robot_position()

##Reach for cup
#goal_position = np.array([[0.7805, -0.04214, 0.6237, 0.6662],
#                          [-0.06911, -0.9974, 0.01909, 0.01705],
#                          [0.6213, -0.05801, -0.7814, -0.2516],
#                          [0, 0, 0, 1]])

#Reach for bottle
goal_position = np.array([[0.9958, 0.0003533, 0.0915, 0.7214],
                          [0.0003214, -1, 0.0003641, 0.03942],
                          [0.0915, -0.0003331, -0.9958, -0.1145],
                          [0, 0, 0, 1]])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

new_q_optimal = interpolate(q_optimal, int(runtime * frequency))
DataSet.joint_angles_plot(new_q_optimal, "./figures/exp1.png")

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