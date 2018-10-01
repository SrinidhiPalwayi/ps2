import numpy as np

from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
def reduceWidth(im, energyImage):

    map=cumulative_minimum_energy_map(energyImage, 'VERTICAL')
    x = find_optimal_vertical_seam(map)
    y = np.arange(im.shape[0])
    height, width, channels = im.shape
    e_height, e_width = energyImage.shape

    final_im = np.zeros((height, width-1, channels), dtype=np.uint8)
    energy_im = np.zeros((e_height, e_width-1), dtype=float)

    for y_index in range(0, height):
        left = im[y_index][:x[y_index]][:]
        right = im[y_index][x[y_index]+1:][:]
        total = np.concatenate((left, right), axis=0)
        final_im[y_index] = total

        left_e= energyImage[y_index][:x[y_index]]
        right_e = energyImage[y_index][x[y_index]+1:]
        total_e = np.concatenate((left_e, right_e), axis=0)
        energy_im[y_index] = total_e

    return (final_im, energy_im)




