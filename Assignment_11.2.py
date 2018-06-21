# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 15:25:52 2018

@author: vamshi
"""
from skimage import io
from sklearn.cluster import KMeans
import numpy as np
import numpy as np
from sklearn import cluster, datasets
from scipy import misc

import scipy as sp
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image = io.imread('tiger.png')
io.imshow(image)
io.show()

rows = image.shape[0]
cols = image.shape[1]
 
image = image.reshape(image.shape[0]*image.shape[1],3)
kmeans = KMeans(n_clusters = 128, n_init=10, max_iter=200)
kmeans.fit(image)

clusters = np.asarray(kmeans.cluster_centers_,dtype=np.uint8) 
labels = np.asarray(kmeans.labels_,dtype=np.uint8 )  
labels = labels.reshape(rows,cols); 

np.save('codebook_tiger.npy',clusters)    
io.imsave('compressed_tiger.png',labels);