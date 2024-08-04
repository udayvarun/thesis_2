import matplotlib.pyplot as plt
import numpy as np

def dataset_manipulator(data):
    
    # Plot joint angles
    joint_angles_plot(data, "without offset")

    data_offset = []
    for q in data:
        data_offset.append([q[0],q[1]+0.8,q[2],q[3]-1 ,q[4],q[5]+2 ,q[6]])
    data_offset = np.array(data_offset)

    joint_angles_plot(data_offset, "with offset")

    return data_offset

def joint_angles_plot(data ,message):
        joint_limits = [(2.8973,-2.8973), (1.7628,-1.7628), (2.8973,-2.8973), (-0.0698, -3.0718), (2.8973,-2.8973), (3.7525,-0.0175), (2.8973,-2.8973)]
        # Plotting original joint angles
        fig, axes = plt.subplots(7, figsize=(15,30), sharex=True)
        plt.suptitle(f'Original Joint Angles {message}')
        for i, ax in enumerate(axes.flatten()):
            ax.plot(data[:, i], label=f'Original Joint {i+1}', color = 'b')
            ax.hlines(y=joint_limits[i][0], xmin = 0, xmax=data.shape[0], linewidth=1, color='r', linestyle='--')
            ax.hlines(y=joint_limits[i][1], xmin = 0, xmax=data.shape[0], linewidth=1, color='r', linestyle='--')
            ax.legend(loc='best')
            ax.grid(True)
        plt.xlabel('Time Step')
        plt.ylabel('Joint Angle')
        plt.show()