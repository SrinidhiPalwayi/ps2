import numpy as np
import sys
import matplotlib.pylab as plt
import math
from skimage import color
from skimage import feature
from reduceWidth import reduceWidth
import scipy
from PIL import Image
#fig = plt.figure()

def fun_energy_image(im):
    input = color.rgb2gray(plt.imread(im))
    edges = feature.canny(input, sigma=3)
    #plt.imshow(edges)
    #plt.show()
    return edges

ei = fun_energy_image("inputSeamCarvingPrague.jpg")
image_array = np.asarray(plt.imread("inputSeamCarvingPrague.jpg"))

for i in range(0,100):
    image_array, ei = reduceWidth(image_array, ei)

#scipy.misc.imsave('outputEnergyReduceHeightPrague.png', ei)
scipy.misc.imsave('fun.png', image_array)