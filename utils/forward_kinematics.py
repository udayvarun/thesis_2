import modern_robotics as mr
import numpy as np

def forward_kinematics(joint_angles):
    # Define the home configuration (end-effector position and orientation when all joints are at zero)
    M = np.array([[0, -1, 0, 0.088],
                [0, 0, -1, 0.926],
                [1, 0, 0, 0.132],
                [0, 0, 0, 1]])

    # Define the screw axes for the 7 joints in the space frame (Slist)
    Slist = np.array([[0, 0, 1, 0, 0, 0],
                    [0, 1, 0, -0.088, 0, 0],
                    [0, 1, 0, -0.088, 0, 0.425],
                    [0, 1, 0, -0.088, 0, 0.817],
                    [1, 0, 0, 0, 0.817, 0],
                    [0, 1, 0, 0.005, 0, 1.092],
                    [1, 0, 0, 0, 1.092, 0]]).T

    T = mr.FKinSpace(M, Slist, joint_angles)
    return T
