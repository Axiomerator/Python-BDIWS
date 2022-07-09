# =============================================================================
# This is a Python-BDIWS successful function presenting program.
# The project is yet in early development.
# The code does not represent the final condition.
# =============================================================================

# import warnings
# import numpy as np
# import cv2

# from .bwm_core import WaterMarkCore
# from .version import bw_notes

from blind_watermark import WaterMark

bwm1 = WaterMark(password_wm=1, password_img=1)
bwm1 = WaterMark()

bwm1.read_img('egimg.jpg') # 读取原图

bwm1.read_wm('watermark.png') # 读取水印

bwm1.embed('output_1.png') # 打上盲水印





bwm1 = WaterMark(password_wm=1, password_img=1)

bwm1.extract(filename='output_1.png', wm_shape=(100, 100), out_wm_name='output_watermark.png', )