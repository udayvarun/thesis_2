import xml.etree.ElementTree as ET
import numpy as np

def dataset_extractor(file_path):
    root = ET.parse(file_path).getroot()
    data = []
    for motion_frame in root.findall('Motion/MotionFrames/MotionFrame'):
        time_step = motion_frame.find('Timestep').text
        joint_positions = motion_frame.find('JointPosition').text.split(" ")
        RSx_joint = joint_positions[37]
        RSy_joint = joint_positions[38]
        RSz_joint = joint_positions[39]
        RWx_joint = joint_positions[40]
        RWy_joint = joint_positions[41]
        REx_joint = joint_positions[31]
        REz_joint = joint_positions[32]
        RS_joint = np.array([RSx_joint, RSy_joint, RSz_joint])
        RE_joint = np.array([REx_joint, REz_joint])
        RW_joint = np.array([RWx_joint, RWy_joint])

        data.append([RSx_joint, RSy_joint, RSz_joint, REx_joint, REz_joint, RWx_joint, RWy_joint])

    return np.array(data)