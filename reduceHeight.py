import numpy as np

from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_horizontal_seam import find_optimal_horizontal_seam
def reduceHeight(im, energyImage):

    map=cumulative_minimum_energy_map(energyImage, 'HORIZONTAL')
    y = find_optimal_horizontal_seam(map)
    height, width, channels = im.shape
    e_height, e_width = energyImage.shape

    final_im = np.zeros((height -1, width, channels), dtype=np.uint8)
    energy_im = np.zeros((e_height-1, e_width), dtype=float)

    for x_index in range(0, width):
        left = im[:y[x_index], x_index]
        right = im[y[x_index]+1:, x_index]
        total = np.concatenate((left, right), axis=0)
        final_im[:, x_index] = total

        left_e= energyImage[:y[x_index], x_index]
        right_e = energyImage[y[x_index]+1:, x_index]
        total_e = np.concatenate((left_e, right_e), axis=0)
        energy_im[:, x_index] = total_e

    return (final_im, energy_im)




