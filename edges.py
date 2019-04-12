import numpy as np
import scipy as sp
import scipy.ndimage
import matplotlib.pyplot as plt
import cv2

# global settings
img_file = "church.png"
width, height = 1920, 1080
blur = 13
window_size = 10

img = plt.imread(img_file)
img = img[:, :, :3]
print(img.shape)
img = cv2.resize(img, (width, height)) # TODO determine interpolation type

# apply gaussian filter
blurred_img = sp.ndimage.gaussian_filter(img, sigma=blur)

# find intensity gradients
g_x = sp.ndimage.sobel(blurred_img, axis=0, mode='constant')
g_y = sp.ndimage.sobel(blurred_img, axis=1)

G = np.sqrt(g_x**2 + g_y**2)
Theta = np.arctan2(g_x, g_y)

# apply non-maximum suppression

suppressed = np.zeros(G.shape)

# apply double threshold to determine edges
# hysteris and remove weak edges

plt.imshow(1-Theta)
plt.show()
