from robot_synergy_input import minimize_dataset
from map_to_robot import map_to_robot
import pickle as pk
import numpy as np
from dataset_extractor import DataSet
from real_robot_mapper import Panda

pca_reload = pk.load(open("pca.pkl",'rb'))
pca_components = pca_reload.pca.components_

min = minimize_dataset(pca_components, 100)

initial_position =  np.array([1.0, 0.5, 0.6, 0.4, 0.3, 0.1, 0.0]) 
goal_position = np.array([1.2, 1.2, 1.2, -1.2, 1.2, 1.2, 1.2])

q_optimal = min.minimize_function()
min.plot_variables()

DataSet.joint_angles_plot(q_optimal)

#map_to_robot(q_optimal)

#Panda().robot_mapper(np.pi * 2)
#joint_postion = Panda().get_robot_position()
#cartesian_position = Panda().forward_kinematics(joint_postion)
#
#print(joint_postion, cartesian_position)