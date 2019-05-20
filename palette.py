from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


def euclidean(pixel):
    ref = np.array((0, 0, 0))
    pix = np.array(pixel)
    return np.linalg.norm(pix - ref)


im = Image.open("totoro.jpg")

pixels = list(im.getdata())
r = []
g = []
b = []
x = []
for pixel in pixels[0:-1:5000]:
    r.append(pixel[0])
    g.append(pixel[1])
    b.append(pixel[2])
    x.append(np.array(pixel))
print(len(r))
num = 5
kmean = KMeans(n_clusters=num)
kmean.fit(x)
rk = []
gk = []
bk = []
for center in kmean.cluster_centers_:
    rk.append(center[0])
    gk.append(center[1])
    bk.append(center[2])

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(r, g, b)
ax.scatter(rk, gk, bk, color='red', s=500)
ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')

plt.show()

# print(kmean.labels_)
# print(kmean.cluster_centers_)
# centers = kmean.cluster_centers_
# labels = sorted(kmean.labels_)
# freq = {}
# for i in range(len(labels)):
#     freq.setdefault(labels[i], 0)
#     freq[labels[i]] += 1 / len(labels)
# print(freq)
#
# palette = []
# for i in range(num):
#     for j in range(int(freq[i] * im.size[1])):
#         for k in range(im.size[0]):
#             r, g, b = centers[i % num]
#             r, g, b = int(r), int(g), int(b)
#             palette.append((r, g, b))
# print(len(palette))
# im2 = Image.new('RGB', im.size)
# im2.putdata(palette)
#
# im2.save("totoropalette.png", 'PNG')
