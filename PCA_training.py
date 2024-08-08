from PCA import PCA
from dataset_manipulator import *
from dataset_extractor import DataSet
import pickle as pk

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
pca.pca_calculation()

# print(pca.pca.components_)

pk.dump(pca, open("pca.pkl","wb"))