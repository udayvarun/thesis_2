from PCA import PCA
from dataset_extractor import dataset_extractor
from map_to_robot import map_to_robot

file_path = r".\DataSets\take_book_from_shelf\take_book_from_shelf_right_arm_01.xml"

data = dataset_extractor(file_path)
n_components = 3

pca = PCA(data, n_components)
pca.pca_calculation()
pca.plot()
pca.print_data()

map_to_robot(data)