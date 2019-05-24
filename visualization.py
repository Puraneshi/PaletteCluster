from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# configuration variables and loading the image
filename = "totoro.jpg"
outputfile = filename.split('.')[0] + "palette.png"
im = Image.open(filename)
width, height = im.size
pixel_samples = 415
step = int(width*height//pixel_samples)

number_of_clusters = 5


# append only a sample of pixels according to variable 'pixel_samples'
pixels = np.array(im.getdata())
x = []
r = []
g = []
b = []
for pixel in pixels[::step]:
    if np.linalg.norm(pixel) > 50:
        x.append(pixel)
        r.append(pixel[0])
        g.append(pixel[1])
        b.append(pixel[2])
x = np.array(x)


# find the pixel clusters in the image
# if the number of clusters is not close to the real number
# KMeans will average distant pixels, distorting the color
kmean = KMeans(n_clusters=number_of_clusters)
kmean.fit(x)
centers = kmean.cluster_centers_
labels = kmean.labels_

# get coordinates of clusters
rk = []
gk = []
bk = []
for center in kmean.cluster_centers_:
    rk.append(center[0])
    gk.append(center[1])
    bk.append(center[2])

# plotting code
pixel_size = 10
pixel_normalized_color = x/255
cluster_size = 500
cluster_color = "red" # or (255, 0, 0)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r, g, b, s=pixel_size, c=pixel_normalized_color)
ax.scatter(rk, gk, bk, c=cluster_color, s=cluster_size)
ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')

plt.show()
