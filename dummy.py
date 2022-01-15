import cv2
import numpy as np
import matplotlib.pyplot as plt

w=100
l=100

z_cordinate=[]
x_cordinate=[]
s=1.5
y_axis=[]
for i in range(2,40,2):

  z=[]
  x=[]
  img=np.zeros((l,w,3), np.uint8)
  img[::]=(255,255,255)
  cv2.circle(img, (w//2,l//2), i, (255,0,0), thickness=1, lineType=8, shift=0)
  for k in range(0,l):
    for j in range(0,w):
      b,g,r=img[k,j]
      if (b,g,r)!=(255,255,255):
        z.append(j)
        x.append(k)
  #z.append(h)
  #x.append(w)
  z_cordinate.append(z)
  x_cordinate.append(x)
  y_axis.append(s)
  s=s+1.5


'''s=1.5
y_axis=[]
for i in range(0,10):
  y_axis.append(s)
  s=s+1.5
'''

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

# syntax for 3-D projection
ax = plt.axes(projection ='3d')

# defining axes
test=[]
for i in range(0,len(y_axis)):

  ax.scatter(x_cordinate[i], y_axis[i], z_cordinate[i], color='red',s=1)
  for k in range(len(x_cordinate[i])):
    test.append([x_cordinate[i][k],z_cordinate[i][k],y_axis[i]])


# syntax for plotting
ax.set_title('3d Scatter conical flask')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


import open3d as o3d
#xyz = np.random.rand(100, 3)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(test)
o3d.io.write_point_cloud('data2.ply', pcd)
o3d.visualization.draw_geometries([pcd])


import numpy as np
import pyvista as pv

# points is a 3D numpy array (n_points, 3) coordinates of a sphere
cloud = pv.PolyData(test)
cloud.plot()

volume = cloud.delaunay_3d(alpha=2.)
shell = volume.extract_geometry()
shell.plot()