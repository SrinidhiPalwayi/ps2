from energy_image import energy_image
from reduceHeight import reduceHeight
import matplotlib.pylab as plt
import numpy as np
import scipy.misc



image = 'inputSeamCarvingPrague.jpg'
ei =energy_image(image)
image_array = np.asarray(plt.imread(image))

for i in range(0,100):
    image_array, ei = reduceHeight(image_array, ei)

scipy.misc.imsave('outputEnergyReduceHeightPrague.png', ei)
scipy.misc.imsave('outputReduceHeightPrague.png', image_array)

image = 'inputSeamCarvingMall.jpg'
ei =energy_image(image)
image_array = np.asarray(plt.imread(image))

for i in range(0,100):
    image_array, ei = reduceHeight(image_array, ei)

scipy.misc.imsave('outputReduceHeightMall.png', image_array)