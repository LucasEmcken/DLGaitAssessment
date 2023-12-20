# DLGaitAssessment

Deep learning for assessment of gait parameters such as assymmetry, double support time and stride length.

You are free to use this code by forking this repository.

## Get started

To get started, ensure you have a pkl file of the video you want to assess gait. You can do that by running the script found in https://colab.research.google.com/drive/1nmbWslWQdANCqDGTZnwjDNkZogfzkEDw on your video or by following the instructions on 4D humans, found here: https://shubham-goel.github.io/4dhumans/.

To get the best result, make you can:

- Wear clothes that makes it easy to differentiate between body parts.
- Ensure the subjects entire body is visible in every frame of the video.
- Use a static camera, i.e make sure the camera does not move during the recording.
- Record the subject walking from the side.
- The subject is walking on flat ground.

The output will be a folder containing a "your-video-title.pkl". This returns contains data from 4D humans on your video.

## Getting result

Next steps are regarding feeding your data to the model.

- First insert your .pkl file to the data directory.
- Insert the path to your .pkl file on line 4 in the 15th code cell in nn.ipynb
- Run every cell in nn.ipnyb
