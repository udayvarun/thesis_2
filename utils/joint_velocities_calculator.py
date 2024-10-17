import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataset_extractor import DataSet
import numpy as np
import matplotlib.pyplot as plt

folder = (r"./data_sets/two_waves")
files = DataSet(folder, "left").single_dataset()

joint_angles = np.array(files[0])
file_name = "./experiment_data_set/figures/data_set_acceleration.png"

# joint_angles_1 = np.load(f'./experiment_data_set/exp3_1_1.npy')
# joint_angles_2 = np.load(f'./experiment_data_set/exp3_1_2.npy')
# joint_angles_3 = np.load(f'./experiment_data_set/exp3_1_3.npy')
# joint_angles = np.append(joint_angles_1, joint_angles_2, axis=0)
# joint_angles = np.append(joint_angles, joint_angles_3, axis=0)
# file_name = "./experiment_data_set/figures/exp3_acceleration.png"

time_steps = np.arange(0, joint_angles.shape[0], 1)
joint_velocities = np.diff(joint_angles, axis=0) / np.diff(time_steps)[:, None]
joint_velocities_stack = np.vstack([joint_velocities, np.zeros((1, joint_angles.shape[1]))])

joint_accelerations = np.diff(joint_velocities_stack, axis=0) / np.diff(time_steps)[:, None]
joint_accelerations_stack = np.vstack([joint_accelerations, np.zeros((1, joint_velocities_stack.shape[1]))])

fig, ax = plt.subplots(3, 1, figsize=(14, 10))

for i in range(joint_angles.shape[1]):
    ax[0].plot(time_steps, joint_angles[:, i], label=f'Joint {i+1} Angle')
ax[0].set_title("Joint Angles vs. Time")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Joint Angle (rad)")
ax[0].legend()
ax[0].grid(True)

for i in range(joint_velocities_stack.shape[1]):
    ax[1].plot(time_steps, joint_velocities_stack[:, i], label=f'Joint {i+1} Velocity')
ax[1].set_title("Joint Velocities vs. Time")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Joint Velocity (rad/s)")
ax[1].legend()
ax[1].grid(True)

for i in range(joint_accelerations_stack.shape[1]):
    ax[2].plot(time_steps, joint_accelerations_stack[:, i], label=f'Joint {i+1} Acceleration')
ax[2].set_title("Joint Accelerations vs. Time")
ax[2].set_xlabel("Time (s)")
ax[2].set_ylabel("Joint Acceleration (rad/s^2)")
ax[2].legend()
ax[2].grid(True)

plt.tight_layout()
plt.savefig(file_name)
plt.show()