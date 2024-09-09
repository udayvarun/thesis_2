from utils.robot_synergy_input import minimize_dataset
import pickle as pk
import numpy as np
from utils.dataset_extractor import DataSet
from utils.interpolate_array import interpolate
from utils.real_robot_mapper import Panda
import roboticstoolbox as rtb

pca_reload = pk.load(open("utils/pca.pkl",'rb'))
pca_components = pca_reload.pca.components_
min = minimize_dataset(pca_components, 50)

initial_position = np.array([-0.00867367069998331, -0.7859290811555426, 0.0014189809690487837, -2.356400179186334, 0.003559221795097906, 1.5683314154592496, 0.7770764079358842])
#goal_position = np.array([-0.004098935386401984, 1.7310226486148363, -2.86264634947962, -0.3970686869768334, -0.4141652220288912, 3.2029244636332677, 0.8809729020759841])

panda_rtb = rtb.models.Panda()

goal = np.array([[0.1891, 0.1486, 0.9706, 0.9332],
                 [-0.05766, 0.9885, -0.1401, -0.109],
                 [-0.9803, -0.02948, 0.1955, 0.332],
                 [0, 0, 0, 1]])

goal_ik = panda_rtb.ikine_LM(goal)

print(goal_ik.q)

#goal_position_2 = np.array()
q_optimal = min.minimize_function(initial_position, goal_ik.q)
min.plot_variables()

DataSet.joint_angles_plot(q_optimal)
new_q_optimal = interpolate(q_optimal, 25000)
DataSet.joint_angles_plot(new_q_optimal)

Panda().robot_mapper(new_q_optimal,50)
joint_postion = Panda().get_robot_position()
cartesian_position = Panda().forward_kinematics(joint_postion)

print(joint_postion, cartesian_position)