import numpy as np
from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map

def find_optimal_vertical_seam(cumulativeEnergyMap):
    last_row = cumulativeEnergyMap[-1]
    height, width = cumulativeEnergyMap.shape
    start = np.argmin(last_row)
    final = list()
    final = [start] + final
    y_axis = height -1
    while(y_axis>0):
        i = final[0] -1 #these are indices
        j = final[0]
        k = final[0] +1
        if(i < 0):
            i = final[0]
        if(k >= width):
            k = final[0]
        min_ind = np.argmin([cumulativeEnergyMap[y_axis -1][i],
                      cumulativeEnergyMap[y_axis -1][j],
                      cumulativeEnergyMap[y_axis -1][k]])
        if(min_ind == 0):
            final = [i] + final
        elif(min_ind == 1):
            final = [j] + final
        else:
            final = [k] + final
        y_axis -=1
    return final





