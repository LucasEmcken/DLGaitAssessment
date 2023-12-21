# DLGaitAssessment

Deep learning for assessment of gait parameters such as assymmetry, double support time and stride length.

You are free to use this code by forking this repository.

## Get started

To get started, ensure you have a pkl file of the video you want to assess gait. You can do that by running the script found in https://colab.research.google.com/drive/1nmbWslWQdANCqDGTZnwjDNkZogfzkEDw on your own video or by following the instructions on 4D humans, found here: https://shubham-goel.github.io/4dhumans/. which also contains a link to a notebook

To get the best result, make you can:

- Wear clothes that makes it easy to differentiate between body parts.
- Ensure the subjects entire body is visible in every frame of the video.
- Use a static camera, i.e make sure the camera does not move during the recording.
- Record the subject walking from the side.
- The subject is walking on flat ground.

The output will be a folder containing a "your-video-title.pkl". This returns contains data from 4D humans on your video.

## Getting result

Next steps are regarding feeding your data to the model.

- First insert your .pkl file to the demo_data directory.
- Then, in demo.ipynb change the value of the file variable to the path to your .pkl file.
- Run the demo.

## Training your own model

We have provided a subset of our training data, as well as our test data for you to train your own model on.
The NN.ipynb notebook contains the code we used to train our model, and should provide a sufficient starting point for your own experimentation

## Annotating your own data
For annotating the data, we also have an annotate_data.ipynb notebook, that contains the code used for annotation
Here you can load your pkl file, and select how many frames to drop from the frames to drop tuple.
 - The first element of the tuple is the amount of frames to cut before the video
 - The second element is the amount of frames to cut at the end of the video
 - The final DF size will then be [frames_to_cut[0], -frames_to_cut[1]]
 - As such, a tuple of value (0,0) will cut no frames, and retain all data from the video

Further down there is two variables, the right_int and left_int. The variables determines the intervals in frames when the foot makes contact. Here you insert the frames where the foot makes contact to the ground, as can be seen by a yellow number in the top left corner of the PHALP video. frame cutting is taken into account, so you dont need to do anything other than look at the frame number.
When annotating, it can be useful to run the current cell, as the output will show if the foot is currently in contact (1) or not (0) with the ground
