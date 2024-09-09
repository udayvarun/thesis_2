from utils.robot_synergy_input import minimize_dataset
import pickle as pk
import numpy as np
from utils.dataset_extractor import DataSet
from utils.interpolate_array import interpolate
from utils.real_robot_mapper import Panda
import time
start_time = time.time()
pca_reload = pk.load(open("utils/pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
min = minimize_dataset(pca_components, 50)

initial_position = np.array([-0.00867367069998331, -0.7859290811555426, 0.0014189809690487837, -2.356400179186334, 0.003559221795097906, 1.5683314154592496, 0.7770764079358842])
goal_position = np.array([-0.004098935386401984, 1.7310226486148363, -2.86264634947962, -0.3970686869768334, -0.4141652220288912, 3.2029244636332677, 0.8809729020759841])
#goal_position = np.array([0.19106172285163428, -0.6339004201721726, 0.03212551790111338, -2.406772175236767, -1.8665619774522875, 1.9992946169773735, -0.008235102961806453])
#goal_position_2 = np.array([-0.07596041580967525, 1.0889692677655356, -0.02201171513180365, -0.7900208974135555, -0.0012949327255024682, 2.820162479665544, 0.7883632254118937] )
q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

DataSet.joint_angles_plot(q_optimal)
new_q_optimal = interpolate(q_optimal, 25000)
DataSet.joint_angles_plot(new_q_optimal)
total_time= time.time()-start_time
print(f"Total_time = {total_time}")
Panda().robot_mapper(new_q_optimal,50)
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)

print(joint_postion, cartesian_position)