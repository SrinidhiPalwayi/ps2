from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from find_optimal_horizontal_seam import find_optimal_horizontal_seam
#from greedyEnergy import gready_seam
import numpy as np
import matplotlib.pyplot as plt


def displaySeam(im, seam, type):
    im = np.asarray(plt.imread(im))

    if(type == 'HORIZONTAL'):
        x = np.arange(im.shape[1])
        y = seam
    else:
        x = seam
        y = np.arange(im.shape[0])

    plt.plot(x,y)
    plt.imshow(im)
    plt.show()


#ei =energy_image('inputSeamCarvingPrague.jpg')
#e = gready_seam(ei, "VERTICAL")
#displaySeam('inputSeamCarvingPrague.jpg', e, "VERTICAL")




