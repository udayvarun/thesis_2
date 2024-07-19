import roboticstoolbox as rtb
import swift
import spatialmath as sm
import numpy as np

def map_to_robot(pca_components, data, inverse_pca):
    env = swift.Swift()
    env.launch(realtime=True)
    panda = rtb.models.Panda()
    env.add(panda)
    dt = 0.01
    joint_velocity = np.gradient(data, len(data))
    joint_acceleration = np.gradient(joint_velocity, len(data))
    # panda.q = [2.78,1.78,0,0,0,0,0]
    while True:
        # for i in range(len(data)):
        #     delta_p = pca_components * dt * joint_acceleration[i]
        #     print(joint_acceleration[i])
        #     panda.q = panda.q + delta_p
        # data_1 = data[10]
        # # panda.q = [data_1[2], data_1[1], data_1[0], data_1[4], data_1[3], data_1[5], data_1[6]]
        for q in data:
            # panda.q = q
            joint_angles = [q[2],q[1],q[0],q[4],q[3],q[5],q[6]]
            panda.q = joint_angles
            # panda.q = [2.78,1.78,2.9,q[4],q[3],q[5],q[6]]
            # panda.q = [q[2],q[3],0,0,0,0,0]
            env.step(dt)
    env.hold()