from robot_synergy_input import minimize_dataset
from map_to_robot import map_to_robot
import pickle as pk
import numpy as np
from dataset_extractor import DataSet
from real_robot_mapper import Panda
from real_robot_mapper_example import Panda2

pca_reload = pk.load(open("pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
steps = 500 
min = minimize_dataset(pca_components, steps)

#initial_position =  np.array([1.0, 0.5, 0.6, -0.4, 0.3, 0.1, 0.0])
#goal_position = np.array([1.2, 1.2, 1.2, -1.2, 1.2, 1.2, 1.2])
initial_position = np.array([-0.00867367069998331, -0.7859290811555426, 0.0014189809690487837, -2.356400179186334, 0.003559221795097906, 1.5683314154592496, 0.7770764079358842])
goal_position = np.array([0.001568545241126775, 0.17793127173708195, 0.00021185316024098454, -1.9908741206979375, 0.0036642521352818628, 2.1848327512100245, 0.7768719775144666])
#goal_position = initial_position * 1.05
q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

DataSet.joint_angles_plot(q_optimal)

#map_to_robot(q_optimal)

Panda().robot_mapper(q_optimal,5)
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)

print(joint_postion, cartesian_position)

#Panda2().robot_mapper(np.pi * 2)
#joint_postion = Panda2().get_robot_position()
#cartesian_position = Panda2().forward_kinematics(joint_postion)
#
#print(joint_postion, cartesian_position)