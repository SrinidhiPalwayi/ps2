import numpy as np
from energy_image import energy_image
import sys
import matplotlib.pylab as plt
import math
from skimage import color
from scipy import ndimage, misc
fig = plt.figure()
import scipy.misc


def cumulative_minimum_energy_map(energyImage, seamDirection):
    cum_eng_map = np.zeros((energyImage.shape), dtype=float)
    height, width = energyImage.shape
    if(seamDirection == "VERTICAL"):
        cum_eng_map[0] = energyImage[0]
        for index_y in range(1, height):
            for index_x in range(0,width):
                i = index_x -1
                j = index_x
                k = index_x +1
                if(index_x == 0):
                    i = index_x
                if(index_x+1 == width):
                    k = index_x
                cum_eng_map[index_y][index_x]=energyImage[index_y][index_x]+min(cum_eng_map[index_y-1][i],
                                                                                cum_eng_map[index_y-1][j],
                                                                                cum_eng_map[index_y-1][k])

    if(seamDirection == "HORIZONTAL"):
        cum_eng_map[:,0] = energyImage[:,0]
        for index_x in range(1, width):
            for index_y in range(0, height):
                i = index_y -1
                j = index_y
                k = index_y +1
                if(index_y == 0):
                    i = index_y
                if(index_y+1 == height):
                    k = index_y
                cum_eng_map[index_y][index_x]=energyImage[index_y][index_x]+min(cum_eng_map[i][index_x-1],
                                                                                cum_eng_map[j][index_x-1],
                                                                                cum_eng_map[k][index_x-1])
    #plt.imshow(cum_eng_map)
    #plt.show()
    return cum_eng_map



ei =energy_image('inputSeamCarvingPrague.jpg')
#scipy.misc.imsave('EnergyPrague.png', ei)
map=cumulative_minimum_energy_map(ei, "VERTICAL")
#scipy.misc.imsave('EnergyMapPragueVertical.png', map)