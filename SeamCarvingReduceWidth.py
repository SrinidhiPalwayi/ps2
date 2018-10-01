from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from energy_image import energy_image
from reduceWidth import reduceWidth
import matplotlib.pylab as plt
import numpy as np
import scipy.misc



image = 'inputSeamCarvingPrague.jpg'
ei =energy_image(image)
image_array = np.asarray(plt.imread(image))

for i in range(0,100):
    image_array, ei = reduceWidth(image_array, ei)

scipy.misc.imsave('outputReduceWidthPrague.png', image_array)

image = 'inputSeamCarvingMall.jpg'
ei =energy_image(image)
image_array = np.asarray(plt.imread(image))

for i in range(0,100):
    image_array, ei = reduceWidth(image_array, ei)

scipy.misc.imsave('outputReduceWidthMall.png', image_array)