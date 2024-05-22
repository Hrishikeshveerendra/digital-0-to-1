# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:54:03 2024

@author: Hrish
"""

import matplotlib.pyplot as plt

data = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0]]

plt.imshow(data, cmap= 'gray')
plt.show()