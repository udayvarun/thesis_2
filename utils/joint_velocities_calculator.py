from dataset_extractor import DataSet
import numpy as np
import matplotlib.pyplot as plt

folder = (r"./data_sets/two_waves")
files = DataSet(folder, "left").single_dataset()

# joint_angles = np.array(files[0])
# file_name = "./experiment_data_set/figures/data_set_velocity.png"

joint_angles_1 = np.load(f'./experiment_data_set/exp3_1.npy')
joint_angles_2 = np.load(f'./experiment_data_set/exp3_2.npy')
joint_angles_3 = np.load(f'./experiment_data_set/exp3_3.npy')
joint_angles = np.append(joint_angles_1, joint_angles_2, axis=0)
joint_angles = np.append(joint_angles, joint_angles_3, axis=0)
file_name = "./experiment_data_set/figures/exp3_velocity.png"

time_steps = np.arange(0, joint_angles.shape[0], 1)
joint_velocities = np.diff(joint_angles, axis=0) / np.diff(time_steps)[:, None]
joint_velocities = np.vstack([joint_velocities, np.zeros((1, joint_angles.shape[1]))])

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
plt.savefig(file_name)
plt.show()
