import numpy as np
import cv2
import matplotlib.pyplot as plt
def kmeans(original_image):
    #original_image = cv2.imread("data/conicalfrustum/image_110321_222205.png")
    crop_img = original_image[50:400, 50:650]
    img=cv2.cvtColor(crop_img,cv2.COLOR_BGR2RGB)
    vectorized = img.reshape((-1,3))
    vectorized = np.float32(vectorized)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    attempts=10
    ret,label,center=cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    result_image = res.reshape((img.shape))
    figure_size = 15
    '''plt.figure(figsize=(figure_size,figure_size))
    plt.subplot(1,2,1),plt.imshow(img)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(result_image)
    plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])
    plt.show()'''
    edges = cv2.Canny(result_image,150,200)
    '''plt.figure(figsize=(figure_size,figure_size))
    plt.subplot(1,2,1),plt.imshow(result_image)
    plt.title('Clustered Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()'''
    return edges

import glob
cv_img = []
i=0
for i in range(0,17):
 for img in glob.glob(f"data/conicalfrustum/{i}.png"):
    n = cv2.imread(img)
    cv_img.append(n)
    img=kmeans(n)
    cv2.imwrite(f'tester/crop{i}.png',img)
    i=i+1




