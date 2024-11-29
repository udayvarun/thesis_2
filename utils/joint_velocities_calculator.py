import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataset_extractor import DataSet
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

folder = (r"data_sets/two_waves")
files = DataSet(folder, "left").single_dataset()

# joint_angles = np.array(files[0])
# file_name = "experiment_data_set/figures/data_set_acceleration_filter.png"
# # file_name = "experiment_data_set/figures/data_set_joint_angles.png"

# joint_angles_1 = np.load(f'experiment_data_set/exp3_1_1.npy')
# joint_angles_2 = np.load(f'experiment_data_set/exp3_1_2.npy')
# joint_angles = np.append(joint_angles_1, joint_angles_2, axis=0)
# file_name = "experiment_data_set/figures/exp3_acceleration_filter.png"

# joint_angles_1 = np.load(f'experiment_data_set/exp2_1_1.npy')
# joint_angles_2 = np.load(f'experiment_data_set/exp2_1_2.npy')
# joint_angles = np.append(joint_angles_1, joint_angles_2, axis=0)
# file_name = "experiment_data_set/figures/exp2_acceleration_filter.png"

joint_angles_1 = np.load(f'experiment_data_set/exp1_1_1.npy')
joint_angles_2 = np.load(f'experiment_data_set/exp1_1_2.npy')
joint_angles = np.append(joint_angles_1, joint_angles_2, axis=0)
file_name = "experiment_data_set/figures/exp1_acceleration_filter.png"

time_steps = np.arange(0, joint_angles.shape[0], 1)
joint_velocities = np.diff(joint_angles, axis=0) / np.diff(time_steps)[:, None]
joint_velocities_stack = np.vstack([joint_velocities, np.zeros((1, joint_angles.shape[1]))])

joint_velocities_stack = gaussian_filter(joint_velocities_stack, 10)

joint_accelerations = np.diff(joint_velocities_stack, axis=0) / np.diff(time_steps)[:, None]
joint_accelerations_stack = np.vstack([joint_accelerations, np.zeros((1, joint_velocities_stack.shape[1]))])

joint_accelerations_stack = gaussian_filter(joint_accelerations_stack, 10)

time_in_seconds = time_steps * 0.01

plt.rcParams.update({'font.size': 15})

# plt.figure(figsize=(14, 4), dpi=600)
# for i in range(joint_angles.shape[1]):
#     plt.plot(time_in_seconds, joint_angles[:, i], label=f'Joint {i+1} Angle')
# # plt.title("Joint Angles vs. Time")
# plt.xlabel("Time [sec]")
# plt.ylabel("Joint Angle [rad]")
# plt.grid(True)
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.tight_layout()
# plt.subplots_adjust(right=0.8)  # Adjust layout to fit legends outside
# plt.savefig(file_name)
# plt.show()

fig, ax = plt.subplots(3, 1, figsize=(14, 10), dpi=600)

for i in range(joint_angles.shape[1]):
    ax[0].plot(time_in_seconds, joint_angles[:, i], label=f'Joint {i+1} Angle')
# ax[0].set_title("Joint Angles vs. Time")
ax[0].set_xlabel("Time [sec]")
ax[0].set_ylabel("Joint Angle [rad]")
ax[0].grid(True)
ax[0].legend(loc='upper left', bbox_to_anchor=(1, 1))

# for i in range(joint_velocities_stack.shape[1]):
ax[1].plot(time_in_seconds, joint_velocities_stack[:, joint_velocities_stack.shape[1]-1], label=f'Joints 1 - 7  \n Velocity')
# ax[1].set_title("Joint Velocities vs. Time")
ax[1].set_xlabel("Time [sec]")
ax[1].set_ylabel("Joint Velocity [rad/sec]")
ax[1].grid(True)
ax[1].legend(loc='upper left', bbox_to_anchor=(1, 1))

# for i in range(joint_accelerations_stack.shape[1]):
ax[2].plot(time_in_seconds, joint_accelerations_stack[:, joint_accelerations_stack.shape[1]-1], label=f'Joints 1 - 7 \n Acceleration')
# ax[2].set_title("Joint Accelerations vs. Time")
ax[2].set_xlabel("Time [sec]")
ax[2].set_ylabel("Joint Acceleration [rad/sec²]")
ax[2].grid(True)
ax[2].legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.subplots_adjust(right=0.8)  # Adjust layout to fit legends outside
plt.savefig(file_name)
plt.show()
