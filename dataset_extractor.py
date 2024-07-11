import xml.etree.ElementTree as ET
from sklearn.preprocessing import StandardScaler
from scipy.interpolate import interp1d
from sklearn.decomposition import PCA
import numpy as np
import os

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
        print(final_data.shape)
        return final_data
    
    def single_dataset(self):
        for file in os.listdir(self.folder):
            if file.endswith(".xml"):
                data = self.side(os.path.join(self.folder, file))
                break
        return data

    def dataset_extractor_right(self, file_path):
        root = ET.parse(file_path).getroot()
        data = []
        for motion_frame in root.findall('Motion/MotionFrames/MotionFrame'):
            time_step = motion_frame.find('Timestep').text
            joint_positions = motion_frame.find('JointPosition').text.split(" ")
            RSx_joint = float(joint_positions[37])
            RSy_joint = float(joint_positions[38])
            RSz_joint = float(joint_positions[39])
            RWx_joint = float(joint_positions[40])
            RWy_joint = float(joint_positions[41])
            REx_joint = float(joint_positions[31])
            REz_joint = float(joint_positions[32])
            RS_joint = np.array([RSx_joint, RSy_joint, RSz_joint])
            RE_joint = np.array([REx_joint, REz_joint])
            RW_joint = np.array([RWx_joint, RWy_joint])

            data.append([RSx_joint, RSy_joint, RSz_joint, REx_joint, REz_joint, RWx_joint, RWy_joint])

        return np.array(data)
    
    def dataset_extractor_left(self, file_path):
        root = ET.parse(file_path).getroot()
        data = []
        for motion_frame in root.findall('Motion/MotionFrames/MotionFrame'):
            time_step = motion_frame.find('Timestep').text
            joint_positions = motion_frame.find('JointPosition').text.split(" ")
            LSx_joint = float(joint_positions[21])
            LSy_joint = float(joint_positions[22])
            LSz_joint = float(joint_positions[23])
            LWx_joint = float(joint_positions[24])
            LWy_joint = float(joint_positions[25])
            LEx_joint = float(joint_positions[15])
            LEz_joint = float(joint_positions[16])
            RS_joint = np.array([LSx_joint, LSy_joint, LSz_joint])
            RE_joint = np.array([LEx_joint, LEz_joint])
            RW_joint = np.array([LWx_joint, LWy_joint])

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