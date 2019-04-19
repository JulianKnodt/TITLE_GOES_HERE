import sys
import numpy as np
import matplotlib.pyplot as plt

# Global Settings
file_name = sys.argv[1]

img = plt.imread(file_name)

print(img.shape)
u, s, v = np.linalg.svd(intensities, full_matrices=False)

def truncated_product(u, s, v, k: int):
  return u[:,:k].dot(np.diag(s[:k])).dot(v[:k,:])

for k in [32, 50, 750, 900, 1100]:
  plt.imshow(truncated_product(u, s, v, k))
  plt.savefig("./references/%d_trunc_pca"%k)
