from PCA import PCA
from dataset_manipulator import *
from dataset_extractor import DataSet
from robot_synergy_input import minimize_dataset
from map_to_robot import map_to_robot

folders = []
folders.append(r".\DataSets\two_waves")
folders.append(r".\DataSets\hand_to_mouth")
folders.append(r".\DataSets\hand_through_hair_right_arm")

data = []
for folder in folders:
    data.extend(DataSet(folder, "right").single_dataset()[0])

data = np.array(data)
dataset_manipulator_without_offset(data)

n_components = 7
pca = PCA(data, n_components)

# Calculation of PCA
pca_components = pca.pca_calculation()

print(pca.get_pca_components())

min = minimize_dataset(pca_components)

initial_position =  np.array([1.0, 0.5, 0.6, 0.4, 0.3, 0.1, 0.0]) 
goal_position = np.array([1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

dataset_manipulator_without_offset(q_optimal)

map_to_robot(q_optimal)