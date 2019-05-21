from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

# configuration variables and loading the image
filename = "totoro.jpg"
outputfile = filename.split('.')[0] + "palette.png"
im = Image.open(filename)
width, height = im.size
steps = 500
step = int(width*height//steps)
# change will result in more or less colors in the palette
number_of_clusters = 5

# append only a sample of pixels according to variable 'steps'
pixels = np.array(im.getdata())
x = []
for pixel in pixels[::step]:
    x.append(pixel)

# find the pixel clusters in the image
# if the number of clusters is not close to the real number
# KMeans will average distant pixels, distorting the color
kmean = KMeans(n_clusters=number_of_clusters)
kmean.fit(x)
centers = kmean.cluster_centers_
labels = kmean.labels_

# calculates frequencies of pixels near the cluster centers
freq = {}
for i in range(len(labels)):
    freq.setdefault(labels[i], 0)
    freq[labels[i]] += 1 / len(labels)

# creates rectangles proportional in height to the presence of the color
palette = []
for i in range(number_of_clusters):
    for j in range(int(freq[i] * height)):
        for k in range(width):
            r, g, b = map(int, centers[i % number_of_clusters])
            palette.append((r, g, b))


# loads pixels into image and saves it in current folder
im2 = Image.new('RGB', im.size)
im2.putdata(palette)

im2.save(outputfile, 'PNG')
