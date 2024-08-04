from PCA import PCA
import numpy as np
from dataset_manipulator import dataset_manipulator
from map_to_robot import map_to_robot
from dataset_extractor import DataSet

folder = r".\DataSets\two_waves"
# folder = r".\DataSets\hand_to_mouth"
# folder = r".\DataSets\hand_through_hair_right_arm"

# side = "left"
side = "right"

# data = DataSet(folder, side).dataset_pca()
# DataSet(folder, side).plot_data()

data = DataSet(folder, side).single_dataset()[0]

# Manipulate joint angles
data_reconstructed = []
for q in data:
    data_reconstructed.append([q[2],q[1],q[0],q[4],q[3],q[5],q[6]])
data_reconstructed = np.array(data_reconstructed)

data_reconstructed = dataset_manipulator(data_reconstructed)

n_components = 1
pca = PCA(data_reconstructed, n_components)

# Print Original data with joint angles
pca.print_original_data()

# Calculation of PCA
pca_components = pca.pca_calculation()
pca.pca_plot()

# Print PCA data
pca.print_pca_data()
print(pca.get_pca_components())

# Calculation of inverse PCA
inverse_result = pca.pca_inverse_calculation()
pca.inverse_pca_plot()

# Print Reconstructed data with joint angles
pca.print_reconstructed_data()

# Map original data
# map_to_robot(data)

# Map inverse PCA data
map_to_robot(inverse_result)