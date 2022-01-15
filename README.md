# Towards 3D Image Reconstruction: 3D Visualization
Three dimensional (3D) ultrasound image reconstruction from two dimensional (2D) images
is a suitable method for analyzing some anatomy related abnormalities.Ultrasound image
reconstruction system is required in order to view the specific part of an object so that
it can be used for analysis purposes. Cost of a 3D Ultrasound machine is high and un
affordable of lower income hospitals. Here we are exploring methods to convert 2D US
images to 3D using basic image processing techniques, K mean clustering and marching
cubes algorithm.

# Data
The objective of this project is to convert 2 D slices of ultrasound image to 3D. For this purpose we require ultrasound images.Ultrasound images of a conical frustum is taken using a linear ultrasound probe. There are 16 images, those are taken as data for this project.Few such images are shown below.


# Pre-processing
# K Means clustering
K means clustering is an unsupervised algorithm used to identify clusters in the data. K
means clustering can be used in image data to segment interesting areas from the back-
ground. It clusters given data into K clusters using the k centroids.This algorithm is used
when we have unlabelled data. The goal is to find certain groups based on some kind of
similarity in the data with the number of groups represented by K.


# Canny edge detection
OpenCV provides cv2.Canny(image, threshold1,threshold2) function for edge detec-
tion.The first argument is our input image. Second and third arguments are our min and
max threshold respectively. Using the Canny algorithm, the function discovers edges in
the input image (8-bit input picture) and marks them in the output map edges. For edge
linking, the least value between threshold1 and threshold2 is chosen. The biggest value is
used to locate the beginnings of strong edge segments.

# Output
