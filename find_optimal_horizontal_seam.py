import numpy as np
from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
def find_optimal_horizontal_seam(cumulativeEnergyMap):
    last_col = cumulativeEnergyMap[:,-1]
    height, width = cumulativeEnergyMap.shape
    start = np.argmin(last_col)
    final = list()
    final = [start] + final
    x_axis = width -1
    while(x_axis>0):
        i = final[0] -1 #these are indices
        j = final[0]
        k = final[0] +1
        if(i < 0):
            i = final[0]
        if(k >= height):
            k = final[0]
        min_ind = np.argmin([cumulativeEnergyMap[i][x_axis-1],
                      cumulativeEnergyMap[j][x_axis-1],
                      cumulativeEnergyMap[k][x_axis-1]])
        if(min_ind == 0):
            final = [i] + final
        elif(min_ind == 1):
            final = [j] + final
        else:
            final = [k] + final
        x_axis -=1
    return final





