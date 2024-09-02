from robot_synergy_input import minimize_dataset
from map_to_robot import map_to_robot
import pickle as pk
import numpy as np
from dataset_extractor import DataSet
from forward_kinematics import forward_kinematics as fk

pca_reload = pk.load(open("pca.pkl",'rb'))
pca_components = pca_reload.pca.components_

min = minimize_dataset(pca_components, 100)

initial_position =  np.array([1.0, 0.5, 0.6, 0.4, 0.3, 0.1, 0.0]) 
goal_position = np.array([1.2, 1.2, 1.2, -1.2, 1.2, 1.2, 1.2])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

DataSet.joint_angles_plot(q_optimal)

print(fk(goal_position))

map_to_robot(q_optimal)