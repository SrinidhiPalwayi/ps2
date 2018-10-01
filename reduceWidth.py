import numpy as np
import matplotlib.pylab as plt

from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from energy_image import energy_image
def reduceWidth(im, energyImage):
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    im = np.asarray(plt.imread(im))
    ax1.imshow(im)

    map=cumulative_minimum_energy_map(energyImage, 'VERTICAL')
    x = find_optimal_vertical_seam(map)
    y = np.arange(im.shape[0])
    height, width, channels = im.shape

    final_im = np.zeros((height, width-1, channels))
    energy_im = np.zeros((height, width-1))

    for y_index in range(0, height):
        left = im[y_index][:x[y_index]][:]
        right = im[y_index][x[y_index]+1:][:]
        total = left + right
        final_im[y_index] = total
        left_e= energy_im[y_index][:x[y_index]]
        right_e = energy_im[y_index][x[y_index]+1:]
        total_e = left_e +right_e
        energy_im[y_index] = total_e
    ax2.imshow(final_im)
    plt.show()
    return (final_im, energy_im)

ei =energy_image('inputSeamCarvingPrague.jpg')
reduceWidth('inputSeamCarvingPrague.jpg' ,ei)


