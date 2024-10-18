import roboticstoolbox as rtb
import swift
import numpy as np
from utils.dataset_extractor import DataSet

def map_to_robot(data, time):
    q_array = np.load(f'./experiment_data_set/{data}.npy')
    DataSet.joint_angles_plot(q_array)
    env = swift.Swift()
    env.launch(realtime=True)
    panda = rtb.models.Panda()
    env.add(panda)
    dt = 0.01
    for q in q_array:
        panda.q = q
        env.step(dt)
        print(q)
    # env.hold()