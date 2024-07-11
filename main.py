from PCA import PCA
from map_to_robot import map_to_robot
from dataset_extractor import DataSet

# file = r".\DataSets\two_waves\Trial_75.xml"
# data = dataset_extractor(file)

folder = r".\DataSets\two_waves"
# folder = r".\DataSets\hand_to_mouth"
# folder = r".\DataSets\hand_through_hair_right_arm"

# side = "left"
side = "right"

# data = DataSet(folder).dataset_pca()
data = DataSet(folder, side).single_dataset()


n_components = 3
pca = PCA(data, n_components)

# Print Original data with joint angles
pca.print_original_data()

# Calculation of PCA
pca.pca_calculation()
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