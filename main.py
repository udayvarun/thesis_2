from utils.robot_synergy_input import minimize_dataset
import pickle as pk
import numpy as np
from utils.dataset_extractor import DataSet
from utils.interpolate_array import interpolate
from utils.real_robot_mapper import Panda

pca_reload = pk.load(open("utils/pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
steps = 50
min = minimize_dataset(pca_components, steps)

initial_position = np.array([-0.00867367069998331, -0.7859290811555426, 0.0014189809690487837, -2.356400179186334, 0.003559221795097906, 1.5683314154592496, 0.7770764079358842])
#goal_position = np.array([0.001568545241126775, 0.17793127173708195, 0.00021185316024098454, -1.9908741206979375, 0.0036642521352818628, 2.1848327512100245, 0.7768719775144666])

goal_position = np.array([-0.004098935386401984, 1.7310226486148363, -2.86264634947962, -0.3970686869768334, -0.4141652220288912, 3.2029244636332677, 0.8809729020759841])

q_optimal = min.minimize_function(initial_position, goal_position)
min.plot_variables()

DataSet.joint_angles_plot(q_optimal)
new_q_optimal = interpolate(q_optimal, 500)
DataSet.joint_angles_plot(new_q_optimal)

Panda().robot_mapper(new_q_optimal,5)
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)

print(joint_postion, cartesian_position)