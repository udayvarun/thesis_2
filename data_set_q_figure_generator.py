import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.dataset_extractor import DataSet
import numpy as np
import matplotlib.pyplot as plt

folder = (r"../data_sets/two_waves")
files = DataSet(folder, "left").single_dataset()

joint_angles = np.array(files[0])
DataSet.joint_angles_plot(joint_angles, "../experiment_data_set/figures/data_set.png")
time_steps = np.arange(0, len(joint_angles) * 0.01, 0.01)
time_gradients = np.gradient(time_steps).reshape(-1, 1)
joint_velocities = np.gradient(joint_angles, axis=0) / time_gradients

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

for i in range(joint_angles.shape[1]):
    ax[0].plot(time_steps, joint_angles[:, i], label=f'Joint {i+1} Angle')
ax[0].set_title("Joint Angles vs. Time")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Joint Angle (rad)")
ax[0].legend()
ax[0].grid(True)

for i in range(joint_velocities.shape[1]):
    ax[1].plot(time_steps, joint_velocities[:, i], label=f'Joint {i+1} Velocity')
ax[1].set_title("Joint Velocities vs. Time")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Joint Velocity (rad/s)")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()
