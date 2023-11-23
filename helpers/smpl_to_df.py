import numpy as np
import joblib
from scipy.spatial import transform
import pandas as pd
import matplotlib.pyplot as plt

def get_smpl(dict):
    frames = list(dict.keys())
    joints_2d = []
    for frame in frames:
        joints_2d.append(dict.get(frame).get('smpl')[0])
    
    return np.array(joints_2d)


def smpl_to_df(path):
    #load pkl file
    results = joblib.load(path)
    
    smpl_frames = np.array([get_smpl(results)[i]['body_pose'] for i in range(len(get_smpl(results)))])

    smpl_joint_frames = []

    for frame in smpl_frames:
        
        joints_x = []
        joints_y = []
        joints_z = []
        
        for joint in frame:
            r = transform.Rotation.from_matrix(joint)
            r = r.as_euler('xyz', degrees=False)

            joints_x.append(r[0])
            joints_y.append(r[1])
            joints_z.append(r[2])
        
        smpl_joint_frames.append([joints_x, joints_y, joints_z])

    smpl_joint_frames = np.array(smpl_joint_frames)
    smpl_joint_frames = np.swapaxes(smpl_joint_frames, 1, 2)
    
    smpl_joint_frames_df = smpl_joint_frames.reshape(smpl_joint_frames.shape[0], -1)
    smpl_joint_frames_df = pd.DataFrame(smpl_joint_frames_df)

    print(smpl_joint_frames_df.shape)
    #get column names from SMPL model joint names
    
    column_names = []

    SMPL_JOINT_NAMES = [
    #    "pelvis",
        "left_hip",
        "right_hip",
        "spine1",
        "left_knee",
        "right_knee",
        "spine2",
        "left_ankle",
        "right_ankle",
        "spine3",
        "left_foot",
        "right_foot",
        "neck",
        "left_collar",
        "right_collar",
        "head",
        "left_shoulder",
        "right_shoulder",
        "left_elbow",
        "right_elbow",
        "left_wrist",
        "right_wrist",
        "left_hand",
        "right_hand",
    ]


    for i in SMPL_JOINT_NAMES:
        column_names.append(f'{i}_x')
        column_names.append(f'{i}_y')
        column_names.append(f'{i}_z')

    smpl_joint_frames_df.columns = column_names
    
    return smpl_joint_frames_df
    


if __name__ == '__main__':
    df = smpl_to_df('../data/demo_gymnasts.pkl')
    
    plot_col = 4    
    
    plt.plot(df.iloc[:,plot_col*3])
    plt.plot(df.iloc[:,plot_col*3+1])
    plt.plot(df.iloc[:,plot_col*3+2])

    plt.title(f'{df.columns[plot_col*3]}')

    plt.show()