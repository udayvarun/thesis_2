import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.robot_synergy_input import minimize_dataset
from utils.interpolate_array import interpolate
from utils.real_robot_mapper import Panda
import pickle as pk
import numpy as np
import time

runtime = 5
frequency = 1e2

start_time = time.time()
pca_reload = pk.load(open("utils/pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
min = minimize_dataset(pca_components, runtime*5)

Panda().move_to_start()

initial_position = Panda().get_robot_position()
# initial_position = np.array([-0.00867367069998331, -0.7859290811555426, 0.0014189809690487837, -2.356400179186334, 0.003559221795097906, 1.5683314154592496, 0.7770764079358842])


#Shake hand
goal_position = np.array([[0.9996, 0.02393, -0.01562, 0.5821],
                          [-0.01083, -0.1883, -0.9821, -0.6462],
                          [-0.02644, 0.9818, -0.1879, 0.04599],
                          [0, 0, 0, 1]])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()


new_q_optimal = interpolate(q_optimal, int(runtime * frequency))
np.save('./experiment_data_set/exp2.npy', new_q_optimal)

total_time= time.time()-start_time
print(f"Total_time = {total_time}")