from energy_image import energy_image
from reduceHeight import reduceHeight
import matplotlib.pylab as plt
import numpy as np
import scipy.misc
from reduceWidth import reduceWidth



image = 'statues.jpg'
ei =energy_image(image)
image_array = np.asarray(plt.imread(image))
height, width, channel = image_array.shape

for i in range(0,50):
    image_array, ei = reduceHeight(image_array, ei)


for i in range(0,25):
    image_array, ei = reduceWidth(image_array, ei)

for i in range(0,100):
    image_array, ei = reduceHeight(image_array, ei)

for i in range(0,50):
    image_array, ei = reduceWidth(image_array, ei)

scipy.misc.imsave('statue_crop.png', image_array)
resize = scipy.misc.imresize(np.asarray(plt.imread(image)), (height-150,width-75))
print(type(resize))
np.save('out.txt', np.abs(image_array-resize))
scipy.misc.imsave('statue_resize.png', resize)