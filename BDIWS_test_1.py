# =============================================================================
# This is a Python-BDIWS basic function testing program.
# The project is yet in early development.
# The code does not represent the final condition.
# =============================================================================

# including the necessary libraries
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from skimage.io import imread, imsave, imshow, show, imread_collection, imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl, rescale
from skimage.util import invert, random_noise, montage
import matplotlib.image as mpimg
import matplotlib.pylab as pylab
from scipy.ndimage import affine_transform, zoom
from scipy import ndimage, misc, signal
# from scipy.stats import signaltonoise

import scipy.fftpack as fp
from skimage.color import rgb2gray
import numpy.fft
import timeit


# open an image (using PIL)
# im = Image.open('egimg.jpg')
# print(im.width, im.height, im.mode, im.format, type(im))
# im.show()

# open an image (using matplotlib)
# im = mpimg.imread('egimg.jpg')
# print(im.shape, im.dtype, type(im))
# plt.figure(figsize=(10,10))
# plt.imshow(im)
# plt.axis('off')
# plt.show()

# 打印频域图像
im = np.array(Image.open('egimg2.png').convert('L'))
pylab.figure(figsize=(10,10))
pylab.imshow(im, cmap=pylab.cm.gray)
pylab.axis('off')
pylab.show()

freq = fp.fft2(im)
(w, h) = freq.shape
half_w, half_h = int(w/2), int(h/2)
freq1 = np.copy(freq)
freq2 = fp.fftshift(freq1)
pylab.figure(figsize = (10,10)), pylab.imshow((20*np.log10(0.1+freq2)).astype(int)), pylab.show()