import numpy as np
import pandas as pd

#make a find peaks algorithm, that finds all peaks above a threshold
def find_peaks(data, threshold):
    peaks = []
    for i in range(len(data)-1):
        if data[i] > threshold:
            if data[i] > data[i-1] and data[i] > data[i+1]:
                peaks.append(i)
    return peaks

def compute_threshold(data):
    return np.mean(data) + 2*np.std(data)

#make a function called mark_valid that checks if the current peak is less than 5 frames away from the next peak
def mark_valid(peaks, dist):
    valid = []
    for i in range(len(peaks)-1):
        if peaks[i+1] - peaks[i] < dist:
            valid.append([peaks[i], peaks[i+1]])
    return valid

def remove_points(df, valid):
    for pair in valid:
        df.iloc[pair[0]:pair[1]+1] = np.nan
        
    # #set the right and left touch columns to the correct values of the uninterpolated data
    # df['right_touch'] = df['right_touch'].fillna(df['right_touch'].bfill())
    # df['left_touch'] = df['left_touch'].fillna(df['left_touch'].bfill())
    
    df = df.interpolate()
    
    return df

def fix_legs(df):
    leg_cols = ['hip', 'knee', 'ankle', 'foot']
    #append left_ and right_ to each column name
    left_leg_cols = ['left_' + col for col in leg_cols]
    right_leg_cols = ['right_' + col for col in leg_cols]

    leg_cols = left_leg_cols + right_leg_cols 

    #append x, y, z to each column name
    x_leg_cols = [col + '_x' for col in leg_cols]
    y_leg_cols = [col + '_y' for col in leg_cols]
    z_leg_cols = [col + '_z' for col in leg_cols]

    leg_cols = x_leg_cols + y_leg_cols + z_leg_cols
    
    #make a list called dist that shows the euclidean distance between each point and the next point
    dist = []
    for i in range(len(df)-1):
        dist.append(np.linalg.norm(df[leg_cols].iloc[i] - df[leg_cols].iloc[i+1]))
        
    thresh = compute_threshold(dist)
    peaks = find_peaks(dist, thresh)
    valid = mark_valid(peaks, 5)
    
    df_fix = remove_points(df, valid)
    
    return df_fix


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    df = pd.read_csv('../wip/demo_walk_22_train.csv')
    df_fix = fix_legs(df.copy())
    
    leg_cols = ['hip', 'knee', 'ankle', 'foot']
    #append left_ and right_ to each column name
    left_leg_cols = ['left_' + col for col in leg_cols]
    right_leg_cols = ['right_' + col for col in leg_cols]

    leg_cols = left_leg_cols + right_leg_cols 

    #append x, y, z to each column name
    x_leg_cols = [col + '_x' for col in leg_cols]
    y_leg_cols = [col + '_y' for col in leg_cols]
    z_leg_cols = [col + '_z' for col in leg_cols]

    leg_cols = x_leg_cols + y_leg_cols + z_leg_cols
    
    dist_old = []
    dist_fix = []
    for i in range(len(df)-1):
        dist_old.append(np.linalg.norm(df[leg_cols].iloc[i] - df[leg_cols].iloc[i+1]))
        dist_fix.append(np.linalg.norm(df_fix[leg_cols].iloc[i] - df_fix[leg_cols].iloc[i+1]))
    
    plt.plot(dist_old)
    plt.plot(dist_fix)
    plt.show()
    
    
    print("done")