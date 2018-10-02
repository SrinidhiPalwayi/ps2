import numpy as np
from energy_image import energy_image
import sys
import matplotlib.pylab as plt
from displaySeam import  displaySeam

def gready_seam(energyImage, seamDirection):
    height, width = energyImage.shape
    if(seamDirection == "VERTICAL"):
        final_list = list()
        start = np.argmin(energyImage[0])
        final_list = [start] + final_list
        for index_y in range(1, height):
            start = final_list[-1]

            i = start-1
            j =start
            k =start+1

            if(start == 0):
                #print("came in ")
                min_loc = np.argmin([sys.maxint, energyImage[index_y][j], energyImage[index_y][k]])
                #print(m)
            elif(start+1 == width):
                min_loc = np.argmin([energyImage[index_y][i], energyImage[index_y][j], sys.maxint])
            else:
                min_loc = np.argmin([energyImage[index_y][i], energyImage[index_y][j], energyImage[index_y][k]])

            if(min_loc == 0):
                final_list.append(start-1)
            elif(min_loc==1):
                final_list.append(start)
            else:
                final_list.append(start+1)
        return final_list

    if (seamDirection == "HORIZONTAL"):
        final_list = list()
        start = np.argmin(energyImage[:,0])
        final_list = [start] + final_list
        for index_x in range(1, width):
            start = final_list[-1]

            i = start - 1
            j = start
            k = start + 1

            if (start == 0):
                min_loc = np.argmin([sys.maxint, energyImage[j][index_x], energyImage[k][index_x]])
            elif (start + 1 == height):
                min_loc = np.argmin([energyImage[i][index_x], energyImage[j][index_x], sys.maxint])
            else:
                min_loc = np.argmin([energyImage[i][index_x], energyImage[j][index_x], energyImage[k][index_x]])

            if (min_loc == 0):
                final_list.append(start - 1)
            elif (min_loc == 1):
                final_list.append(start)
            else:
                final_list.append(start + 1)
        return final_list

ei =energy_image('inputSeamCarvingPrague.jpg')
e = gready_seam(ei, "VERTICAL")
displaySeam('inputSeamCarvingPrague.jpg', e, "VERTICAL")

