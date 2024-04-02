# Title: Car Detection in Video using OpenCV

# Introduction:
This Python script utilizes OpenCV library for car detection in a video. It employs a pre-trained car detection cascade classifier to identify cars within each frame of the video. The detected cars are then outlined with rectangles, and the resulting video is saved.

# Code Overview:
- Importing Libraries:
  NumPy for numerical computations.
  Matplotlib for plotting graphs.
  Pandas for data manipulation.
  OpenCV (cv2) for image and video processing.
  imutils for convenience functions in OpenCV.
  PIL (Image) for working with images.
- Loading Haar Cascade Classifier:
  The pre-trained Haar Cascade classifier file 'cars.xml' is loaded using cv2.CascadeClassifier.
- Opening Video Source:
  The video file 'Cars.mp4' is opened for processing using cv2.VideoCapture.
- Setting Video Parameters:
  Width, height, and frames per second (fps) of the video are extracted.
  A new video file 'result.avi' is created for writing processed frames.
- Car Detection Loop:
  The script iterates through each frame of the video.
  Frames are converted to grayscale for better processing.
  The car detection algorithm is applied using car_cascade.detectMultiScale.
  Detected cars are outlined with rectangles using cv2.rectangle.
  Processed frames are written to the output video.
- Video Processing:
  The processed video is released and saved once the loop completes.
# Conclusion:
This script demonstrates a simple yet effective method for car detection in videos using OpenCV and a pre-trained Haar Cascade classifier. The same approach can be extended to detect other objects by employing different pre-trained classifiers or training custom ones.

# Dependencies:
- NumPy
- Matplotlib
- Pandas
- OpenCV (cv2)
- imutils
- PIL (Image)

# Instructions:
- Ensure the required video file ('Cars.mp4') and Haar Cascade classifier file ('cars.xml') are in the specified directory.
- Install the required dependencies if not already installed.
- Run the script to process the video and detect cars.
- Adjust parameters or explore other pre-trained classifiers for detecting different objects.

# Author:
Prajesh Tejani

# References:
- OpenCV documentation: https://opencv.org/
- Haar Cascade Classifier: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html





