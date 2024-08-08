import xml.etree.ElementTree as ET
from sklearn.preprocessing import StandardScaler
from scipy.interpolate import interp1d
from sklearn.decomposition import PCA
import numpy as np
import os
import matplotlib.pyplot as plt

class DataSet:
    def __init__(self, folder, side):
        self.folder = folder
        if (side == "left"):
            self.side = self.dataset_extractor_left
        if (side == "right"):
            self.side = self.dataset_extractor_right

    def dataset_pca(self):
        data = []
        for file in os.listdir(self.folder):
            if file.endswith(".xml"):
                data.append(self.side(os.path.join(self.folder, file)))
        
        total = sum(i.shape[0] for i in data)
        avg_time = total//len(data)

        # Interpolate all arrays to the common time basis
        interpolated_arrays = [self.interpolate_to_common_time(array, avg_time) for array in data]

        # Standardize each dataset individually
        scaler = StandardScaler()
        standardized_data = [scaler.fit_transform(d) for d in interpolated_arrays]

        # Compute the average of the standardized datasets
        average_data = np.mean(standardized_data, axis=0)

        # Apply PCA to the averaged data
        number_of_components = 7
        pca = PCA(n_components=number_of_components)
        final_data = pca.fit_transform(average_data)

        # Output the final set
        return final_data
    
    def single_dataset(self):
        data = []
        for file in os.listdir(self.folder):
            if file.endswith(".xml"):
                data.append(self.side(os.path.join(self.folder, file)))
        return data
    
    def plot_data(self):
        data = self.single_dataset()
        data_pca = self.dataset_pca()
        # Plotting original vs reconstructed for the first joint
        fig, axes = plt.subplots(7, figsize=(15,30), sharex=True)
        plt.suptitle('Single vs PCA Joint Angle for Joints')
        for i, ax in enumerate(axes.flatten()):
            for d in data:
                ax.plot(d[:, i], label=f'Single Joint {i+1}')
            ax.plot(data_pca[:, i], label=f'PCA Joint {i+1}', linestyle='--')
            ax.legend(loc='best')
            ax.grid(True)
        plt.xlabel('Time Step')
        plt.ylabel('Joint Angle')
        plt.show()

    def dataset_extractor_right(self, file_path):
        root = ET.parse(file_path).getroot()

        joint_order = root.find(".//JointOrder")
        joint_names = [joint.get('name') for joint in joint_order.findall('Joint')]

        data = []
        for motion_frame in root.findall('Motion/MotionFrames/MotionFrame'):
            time_step = motion_frame.find('Timestep').text
            joint_positions = motion_frame.find('JointPosition').text.split(" ")
            RSx_joint = float(joint_positions[joint_names.index('RSx_joint')])
            RSy_joint = float(joint_positions[joint_names.index('RSy_joint')])
            RSz_joint = float(joint_positions[joint_names.index('RSz_joint')])
            RWx_joint = float(joint_positions[joint_names.index('RWx_joint')])
            RWy_joint = float(joint_positions[joint_names.index('RWy_joint')])
            REx_joint = float(joint_positions[joint_names.index('REx_joint')])
            REz_joint = float(joint_positions[joint_names.index('REz_joint')])
            RS_joint = np.array([RSx_joint, RSy_joint, RSz_joint])
            RE_joint = np.array([REx_joint, REz_joint])
            RW_joint = np.array([RWx_joint, RWy_joint])

            data.append([RSx_joint, RSy_joint, RSz_joint, REx_joint, REz_joint, RWx_joint, RWy_joint])

        return np.array(data)
    
    def dataset_extractor_left(self, file_path):
        root = ET.parse(file_path).getroot()

        joint_order = root.find(".//JointOrder")
        joint_names = [joint.get('name') for joint in joint_order.findall('Joint')]

        data = []
        for motion_frame in root.findall('Motion/MotionFrames/MotionFrame'):
            time_step = motion_frame.find('Timestep').text
            joint_positions = motion_frame.find('JointPosition').text.split(" ")
            LSx_joint = float(joint_positions[joint_names.index('LSx_joint')])
            LSy_joint = float(joint_positions[joint_names.index('LSy_joint')])
            LSz_joint = float(joint_positions[joint_names.index('LSz_joint')])
            LWx_joint = float(joint_positions[joint_names.index('LWx_joint')])
            LWy_joint = float(joint_positions[joint_names.index('LWy_joint')])
            LEx_joint = float(joint_positions[joint_names.index('LEx_joint')])
            LEz_joint = float(joint_positions[joint_names.index('LEz_joint')])
            LS_joint = np.array([LSx_joint, LSy_joint, LSz_joint])
            LE_joint = np.array([LEx_joint, LEz_joint])
            LW_joint = np.array([LWx_joint, LWy_joint])

            data.append([LSx_joint, LSy_joint, LSz_joint, LEx_joint, LEz_joint, LWx_joint, LWy_joint])

        return np.array(data)
    
    def interpolate_to_common_time(self, array, avg_time):
        common_time = np.linspace(0, 1, avg_time)
        time_points = np.linspace(0, 1, array.shape[0])
        interpolated_array = np.zeros((len(common_time), array.shape[1]))
        for i in range(array.shape[1]):
            interp_func = interp1d(time_points, array[:, i], kind='linear', fill_value="extrapolate")
            interpolated_array[:, i] = interp_func(common_time)
        return interpolated_array
