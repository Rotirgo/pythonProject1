
import json
# settings= {
#    'path_source':'C:/Users/Никита/Desktop/zebra.jpg',
#    'path_res': 'C:/Users/Никита/Desktop/res.jpg',
#    'light': .5,
#    'tolerance': .2,
#    'x': 100,
#    'y': 150,
# }

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, io, filters, color, morphology
from skimage.color import rgb2gray
from skimage.segmentation import flood, flood_fill

img = rgb2gray(io.imread('C:/Users/Никита/Desktop/zebra.jpg'))

# Fill a square near the middle with value 127, starting at index (76, 76)
filled_checkers = flood_fill(img, (0, 100), 0.5, tolerance = 0.2)

fig, ax = plt.subplots(ncols=2, figsize=(10, 5))

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title('Original')

ax[1].imshow(filled_checkers, cmap=plt.cm.gray)
ax[1].set_title('After flood fill')

plt.show()

