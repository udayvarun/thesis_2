from PCA import PCA
import numpy as np
from dataset_manipulator import *
from dataset_extractor import DataSet
from robot_synergy_input import *

folder = r".\DataSets\two_waves"
# folder = r".\DataSets\hand_to_mouth"
# folder = r".\DataSets\hand_through_hair_right_arm"

# side = "left"
side = "right"

data = DataSet(folder, side).single_dataset()[0]

# Manipulate joint angles
data_reconstructed = dataset_manipulator_without_offset(data)
data_offset = dataset_manipulator_with_offset(data_reconstructed)

n_components = 3
pca = PCA(data_offset, n_components)

# Print Original data with joint angles
pca.print_original_data()

# Calculation of PCA
pca_components = pca.pca_calculation()
pca.pca_plot()

# Print PCA data
pca.print_pca_data()
print(pca.get_pca_components())

q_optimal = minimized(pca_components)
print(q_optimal)