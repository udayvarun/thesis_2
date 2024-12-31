from utils.PCA import PCA
from utils.dataset_extractor import DataSet
import pickle as pk
import numpy as np
import os

def generate_pca_file(n_components):
    folders = [x.path for x in os.scandir(r"data_sets")]

    data = []
    for folder in folders:
        files = DataSet(folder, "left").single_dataset()
        for file in files:
            data.extend(file)

    data = np.array(data)
    DataSet.joint_angles_plot(data)

    pca = PCA(data, n_components)

    # Calculation of PCA
    pca.pca_calculation()

    # print(pca.pca.components_)

    pk.dump(pca, open("utils/pca.pkl","wb"))