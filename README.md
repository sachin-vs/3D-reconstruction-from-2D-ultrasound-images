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


![uS](https://user-images.githubusercontent.com/85213549/149622467-5ff5004b-c6c7-40ad-bcb6-7eef933aa9c7.jpeg)


# Pre-processing
## K Means clustering
K means clustering is an unsupervised algorithm used to identify clusters in the data. K
means clustering can be used in image data to segment interesting areas from the back-
ground. It clusters given data into K clusters using the k centroids.This algorithm is used
when we have unlabelled data. The goal is to find certain groups based on some kind of
similarity in the data with the number of groups represented by K.

![K Means](https://user-images.githubusercontent.com/85213549/149622520-381d1dcc-3008-40b2-8ba0-24e8a03e1a09.png)


## Canny edge detection
OpenCV provides cv2.Canny(image, threshold1,threshold2) function for edge detec-
tion.The first argument is our input image. Second and third arguments are our min and
max threshold respectively. Using the Canny algorithm, the function discovers edges in
the input image (8-bit input picture) and marks them in the output map edges. For edge
linking, the least value between threshold1 and threshold2 is chosen. The biggest value is
used to locate the beginnings of strong edge segments.

![canny](https://user-images.githubusercontent.com/85213549/149622526-cefb26df-ff8a-404c-a182-c5cb7840d57a.png)
# Output
## Open3D output

![Screenshot from 2022-01-05 17-41-32](https://user-images.githubusercontent.com/85213549/149622575-dee531e2-c198-4703-bc7d-7eb53c9b5862.png)
## pyvista Output

![Screenshot from 2022-01-05 18-35-05](https://user-images.githubusercontent.com/85213549/149622613-ccd204c7-3e29-41fe-9737-798c11fe5fbd.png)


# How to run the code

1. Clone the repository.
2. Go inside the folder 
3. Install requirements using command ```pip install requirements```
4. Run the code 3D_plot.py in python 3 , ```python3 3D_plot.py```

# About code base

1. The ultrasound image data are stored in folder "data" in png format
2. The filtered images are stored in folder "output"
3. filter.py filter US images
4. 3D_plot.py convert 2D into 3D
5. data2.py is a point cloud file formed by running 3D_plot.py
6. dummy.py run 3D reconstruction on dummy images