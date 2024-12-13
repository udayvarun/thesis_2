import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.robot_synergy_input import minimize_dataset
from utils.interpolate_array import interpolate
from utils.PCA_training import generate_pca_file
import pickle as pk
import numpy as np
import time

def calculate_q(initial_position, goal_position, exp_name, runtime, n_components = 7, factor = 5):
    frequency = 1e2

    start_time = time.time()
    generate_pca_file(n_components)
    pca_reload = pk.load(open("./utils/pca.pkl",'rb'))
    pca_components = pca_reload.pca.components_
    pca_reload.pca_plot(".\experiment_data_set\\figures\pca_plot.png")
    min = minimize_dataset(pca_components, runtime*factor)

    q_optimal = min.minimize_function(initial_position, goal_position)

    new_q_optimal = interpolate(q_optimal, int(runtime * frequency))
    np.save(f'./experiment_data_set/simulation/{exp_name}.npy', new_q_optimal)

    total_time= time.time()-start_time
    print(f"Total_time = {total_time}")