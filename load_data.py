from PIL import Image
import requests
from io import BytesIO
import sys
import numpy as np


def load_data(spin_samp_rate=1, incl_samp_rate=1, verbose=True):
    spins = np.arange(0,101,spin_samp_rate)
    incls = np.arange(0,90,incl_samp_rate)

    urlfoldname = "http://vlbiimaging.csail.mit.edu/static/data/targetImgs/sgraBroderick/"

    X = []
    y = []

    for spin in spins:
        if verbose:
            print('loading spin %03d %d incl images....'%(spin, len(incls)))
        for incl in incls:
            imname = 'pmap_bs_%03d_%03d_2.png'%(spin,incl)
            url = urlfoldname + imname
            try:
                response = requests.get(url)
                img = np.asarray(Image.open(BytesIO(response.content)))
            except IOError:
                print(imname+' image not exist.')
                continue
            X.append(img)
            y.append([spin, incl])
    X_data = np.array(X)
    y_data = np.array(y)
    
    return X_data, y_data