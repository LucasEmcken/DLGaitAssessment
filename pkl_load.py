import joblib


def load_pkl(pkl_path):
    return joblib.load(pkl_path)
#results = joblib.load('data/demo_Run-close.pkl')
#print(results)

"""
results = {
  # A dictionary for each frame.
  'vid_frame0.jpg': {
    '2d_joints':       List[np.array(90,)],   # 45x 2D joints for each detection
    '3d_joints':       List[np.array(45,3)],  # 45x 3D joints for each detection
    'annotations':     List[Any],             # custom annotations for each detection
    'appe':            List[np.array(4096,)], # appearance features for each detection
    'bbox':            List[[x0 y0 w h]],     # 2D bounding box (top-left corner and dimensions) for each track (detections + ghosts)
    'camera':          List[[tx ty tz]],      # camera translation (wrt image) for each detection
    'camera_bbox':     List[[tx ty tz]],      # camera translation (wrt bbox) for each detection
    'center':          List[[cx cy]],         # 2D center of bbox for each detection
    'class_name':      List[int],             # class ID for each detection (0 for humans)
    'conf':            List[float],           # confidence score for each detection
    'frame_path':      'vid_frame0.jpg',      # Frame identifier
    'loca':            List[np.array(99,)],   # location features for each detection
    'mask':            List[mask],            # RLE-compressed mask for each detection
    'pose':            List[np.array(229,)],  # pose feature (concatenated SMPL params) for each detection
    'scale':           List[float],           # max(width, height) for each detection
    'shot':            int,                   # Shot number
    'size':            List[[imgw imgh]],     # Image dimensions for each detection
    'smpl':            List[Dict_SMPL],       # SMPL parameters for each detection: betas (10), body_pose (23x3x3), global_orient (3x3)
    'tid':             List[int],             # Track ID for each detection
    'time':            int,                   # Frame number
    'tracked_bbox':    List[[x0 y0 w h]],     # 2D bounding box (top-left corner and dimensions) for each detection
    'tracked_ids':     List[int],             # Track ID for each detection
    'tracked_time':    List[int],             # for each detection, time since it was last seen
  },
  'vid_frame1.jpg': {
    ...
  },
  ...
}
"""