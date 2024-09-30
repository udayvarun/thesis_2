import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.robot_synergy_input import minimize_dataset
from utils.interpolate_array import interpolate
from utils.real_robot_mapper import Panda
import pickle as pk
import numpy as np
import time

runtime = 10
frequency = 1e2

start_time = time.time()
pca_reload = pk.load(open("utils/pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
min = minimize_dataset(pca_components, runtime*5)

Panda().move_to_start()

initial_position = Panda().get_robot_position()
# initial_position = np.array([-0.00867367069998331, -0.7859290811555426, 0.0014189809690487837, -2.356400179186334, 0.003559221795097906, 1.5683314154592496, 0.7770764079358842])

##Reach for cup
#goal_position = np.array([[0.7805, -0.04214, 0.6237, 0.6662],
#                          [-0.06911, -0.9974, 0.01909, 0.01705],
#                          [0.6213, -0.05801, -0.7814, -0.2516],
#                          [0, 0, 0, 1]])

#Reach for bottle
goal_position = np.array([[0.9958, 0.0003533, 0.0915, 0.7214],
                          [0.0003214, -1, 0.0003641, 0.03942],
                          [0.0915, -0.0003331, -0.9958, -0.1145],
                          [0, 0, 0, 1]])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

new_q_optimal = interpolate(q_optimal, int(runtime * frequency))
np.save('./experiment_data_set/exp1.npy', new_q_optimal)

total_time= time.time()-start_time
print(f"Total_time = {total_time}")