import numpy as np
import cv2
from sklearn.cluster import MeanShift, estimate_bandwidth
originImg = cv2.imread('pic/me.jpg')
originShape = originImg.shape
flatImg=np.reshape(originImg, [-1, 3])
bandwidth = estimate_bandwidth(flatImg, quantile=0.1, n_samples=100)
ms = MeanShift(bandwidth = bandwidth, bin_seeding=True)
ms.fit(flatImg)
cluster_centers = ms.cluster_centers_
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
print("number of estimated clusters : %d" % n_clusters_)
segmentedImg = np.reshape(labels, originShape[:2])

cv2.imshow('Image',segmentedImg)

cv2.waitKey(0)

cv2.destroyAllWindows()
