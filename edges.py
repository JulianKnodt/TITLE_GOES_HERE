import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# global settings
img_file = sys.argv[1]

img = cv.imread(img_file)
edges = cv.Canny(img, 100, 200)
plt.imshow(edges)
plt.axis('off')
path = Path(img_file)
new_path = path.parent / (path.stem + "_edges.png")
plt.savefig(new_path, bbox_inches='tight')

