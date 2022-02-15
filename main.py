
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, io, filters, color, morphology
from skimage.color import rgb2gray
from skimage.segmentation import flood, flood_fill
from skimage.exposure import histogram

import json
#выставляем все необходимые параметры в json
settings= {
    'path_source':'C:/Users/Никита/Desktop/zebra.jpg', #путь к исходному изображению
    'path_res': 'C:/Users/Никита/Desktop/res.jpg', #путь для сохранения результирующего изображения
    'light': .5, #яркость(цвет в черно-белом) в какой мы хотим покрасить
    'tolerance': .3, #допустимый разброс в яркости между соседними, чтобы считать их схожими
    'x': 500, #координата икс(направление у картинки сверху вниз)
    'y': 350, #координата игрек(направление у картинки слева направо)
 }
with open('settings.json', 'w') as fp:
    json.dump(settings, fp)

with open('settings.json') as json_file:
    json_data = json.load(json_file)

img = rgb2gray(io.imread('C:/Users/Никита/Desktop/zebra.jpg'))

#сама заливка(почему-то работает только с черно-белым, цветная в другой библиотеке)
filled_img = flood_fill(img, (json_data['x'], json_data['y']), json_data['light'], tolerance = json_data['tolerance'])

#параметры для гисторамм
hist_light, bins_light = histogram(img)
hist_light_res, bins_light_res = histogram(filled_img)

#вывод исходного изображения
fig =plt.figure(figsize=(10, 10))
fig.add_subplot(2,2,1)
plt.imshow(img, cmap=plt.cm.gray)
plt.axis('off')

#вывод результирующего изображения
fig.add_subplot(2,2,2)
plt.imshow(filled_img, cmap=plt.cm.gray)
plt.axis('off')

#гистограмма исходного
fig.add_subplot(2,2,3)
plt.plot(bins_light,hist_light, color='black', linestyle = '-', linewidth=1)
plt.legend(['light'])

#гистограмма результирующего
fig.add_subplot(2,2,4)
plt.plot(bins_light_res,hist_light_res, color='black', linestyle = '-', linewidth=1)
plt.legend(['light'])

plt.imsave('C:/Users/Никита/Desktop/res.jpg', filled_img, cmap=plt.cm.gray) #сохранение результирующего изображения
plt.show()



