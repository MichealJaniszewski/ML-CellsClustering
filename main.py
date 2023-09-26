import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage.io import imsave,imread
cells =[]
for i in range(50):
    cell = imread(f"images/{i}.png")
    w,h = cell.shape
    cols = np.reshape(cell/255.0, (w * h))
    plt.plot(cols)
    cells.append(cols)
