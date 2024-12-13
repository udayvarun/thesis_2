import roboticstoolbox as rtb
import swift
import numpy as np
from utils.dataset_extractor import DataSet

class Simulation:
    def __init__(self):
        self.env = swift.Swift()
        self.env.launch(realtime=True)
        self.panda = rtb.models.Panda()
        self.env.add(self.panda)

    def map_to_robot(self, data, time):
        q_array = np.load(f'./experiment_data_set/{data}.npy')
        DataSet.joint_angles_plot(q_array)
        dt = 0.01
        for q in q_array:
            self.panda.q = q
            self.env.step(dt)
            print(q)
        # env.hold()
    def get_position(self):
        return self.panda.q
    def forward_kinematics(self, q):
        return self.panda.fkine(q)