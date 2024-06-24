from PCA import PCA
from dataset_extractor import dataset_extractor
from map_to_robot import map_to_robot

file_path = r".\DataSets\take_book_from_shelf\take_book_from_shelf_right_arm_01.xml"

data = dataset_extractor(file_path)
n_components = 3

pca = PCA(data, n_components)

# Print Original data with joint angles
pca.print_original_data()

pca.pca_calculation()
pca.pca_plot()
# Print PCA data
pca.print_pca_data()

inverse_result = pca.pca__inverse_calculation()
pca.inverse_pca_plot()
# Print Reconstructed data with joint angles
pca.print_reconstructed_data()

# Map original data
# map_to_robot(data)

# Map inverse PCA data
map_to_robot(inverse_result)