from utils.PCA import PCA
from dataset_extractor import DataSet
import pickle as pk
import numpy as np

folders = []
folders.append(r"../data_sets/two_waves")
folders.append(r"../data_sets/hand_to_mouth")
folders.append(r"../data_sets/hand_through_hair_right_arm")
folders.append(r"../data_sets/files_motions_986")
folders.append(r"../data_sets/take_book_from_shelf")

data = []
for folder in folders:
    files = DataSet(folder, "left").single_dataset()
    for file in files:
        data.extend(file)

data = np.array(data)
DataSet.joint_angles_plot(data)

n_components = 7
pca = PCA(data, n_components)

# Calculation of PCA
pca.pca_calculation()

# print(pca.pca.components_)

pk.dump(pca, open("pca.pkl","wb"))