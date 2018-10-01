import numpy as np
import sys
import matplotlib.pylab as plt
import math
from skimage import color
from scipy import ndimage, misc
from PIL import Image
#fig = plt.figure()

def energy_image(im):
    #ax1 = fig.add_subplot(121)
    #ax2 = fig.add_subplot(122)
    input = color.rgb2gray(plt.imread(im))
    #ax1.imshow(input, cmap='gray')
    grad_x = np.gradient(input, axis=0)
    grad_x = np.absolute(grad_x)
    grad_y = np.gradient(input, axis=1)
    grad_y = np.absolute(grad_y)
    final = grad_x + grad_y
    #ax2.imshow(final, cmap='gray')
    return final
    #plt.show()

energy_image("riv.jpg")


"""
    for x in range(1,width, step=1):
        for y in range(1,height):
            grad = 0
            for c in range(channels)
                grad+= math.abs(input[y][x][c] - input[y-1][x][c])
                grad+=math.abs(input[y][x][c] - input[y])
"""








