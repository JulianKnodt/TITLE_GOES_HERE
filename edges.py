import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# global settings
img_file = sys.argv[1]

width, height = 1920, 1080

img = cv.imread(img_file, 0)
img = cv.resize(img, (width, height))
edges = cv.Canny(img, 100, 200)
plt.imshow(np.invert(edges),cmap='gray')
path = Path(img_file)
new_path = path.parent / (path.stem + "_edges.png")
plt.savefig(new_path)

