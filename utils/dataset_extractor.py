import xml.etree.ElementTree as ET
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
    
    def single_dataset(self):
        data = []
        for file in os.listdir(self.folder):
            if file.endswith(".xml"):
                data.append(self.side(os.path.join(self.folder, file)))
        return data

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

    def joint_angles_plot(data, label = None):
        joint_limits = [(2.8973,-2.8973), (1.7628,-1.7628), (2.8973,-2.8973), (-0.0698, -3.0718), (2.8973,-2.8973), (3.7525,-0.0175), (2.8973,-2.8973)]
        # Plotting original joint angles
        fig, axes = plt.subplots(7, figsize=(15,30), sharex=True)
        plt.suptitle(f'Original Joint Angles with limits')
        for i, ax in enumerate(axes.flatten()):
            ax.plot(data[:, i], label=f'Original Joint {i+1}', color = 'b')
            ax.hlines(y=joint_limits[i][0], xmin = 0, xmax=data.shape[0], linewidth=1, color='r', linestyle='--')
            ax.hlines(y=joint_limits[i][1], xmin = 0, xmax=data.shape[0], linewidth=1, color='r', linestyle='--')
            ax.legend(loc='best')
            ax.grid(True)
        plt.xlabel('Time Step')
        plt.ylabel('Joint Angle')
        if label != None:
            plt.savefig(label)
        plt.show()