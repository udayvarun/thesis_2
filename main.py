from robot_synergy_input import minimize_dataset
from map_to_robot import map_to_robot
import pickle as pk
import numpy as np
from dataset_manipulator import *

pca_reload = pk.load(open("pca.pkl",'rb'))
pca_components = pca_reload.pca.components_

min = minimize_dataset(pca_components)

initial_position =  np.array([1.0, 0.5, 0.6, 0.4, 0.3, 0.1, 0.0]) 
goal_position = np.array([1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

dataset_manipulator_without_offset(q_optimal)

map_to_robot(q_optimal)