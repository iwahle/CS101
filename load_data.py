from PIL import Image
import requests
from io import BytesIO
import sys
import os
import numpy as np
import astropy.io.fits as fits
from astropy.utils.data import download_file

def load_data(spin_samp_rate=1, incl_samp_rate=1, verbose=True):
    spins = np.arange(0,101,spin_samp_rate)
    incls = np.arange(0,90,incl_samp_rate)

    urlfoldname = "http://vlbiimaging.csail.mit.edu/static/data/targetImgs/sgraBroderick/"

    X = []
    y = []
    
    for incl in incls:
        if verbose:
            print('loading incl %03d, %d spin images....'%(incl, len(spins)))
        for spin in spins:
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


def load_data_fits(spin_samp_rate=1, incl_samp_rate=1, verbose=True):
    spins = np.arange(0,101,spin_samp_rate)
    incls = np.arange(0,90,incl_samp_rate)
    
    urlfoldname = "http://vlbiimaging.csail.mit.edu/static/data/targetImgs/sgraBroderick/"

    X = []
    y = []
    
    for incl in incls:
        if verbose:
            print('loading incl %03d, %d spin images....'%(incl, len(spins)))
        for spin in spins:
            imname = 'pmap_bs_%03d_%03d_2.fits'%(spin,incl)
            url = urlfoldname + imname
            try:
                response = requests.get(url, allow_redirects=True)
                with open("tmp.fits", 'wb') as f:
                    f.write(response.content)
            except IOError:
                print(imname+' image not exist.')
                continue

            hdul = fits.open("tmp.fits")
            img = hdul[0].data.copy()
            del hdul[0].data
            hdul.close()

            X.append(img)
            y.append([spin, incl])

    os.remove("tmp.fits")
    X_data = np.array(X)
    y_data = np.array(y)
    
    return X_data, y_data

# delete tmp.fits !!!!!
# push code!!!

if __name__ == "__main__": 
    #X_data, y_data = load_data()
    #np.save("X_data.npy",X_data)
    #np.save("y_data.npy",y_data)
    X_data, y_data = load_data_fits()
    np.save("X_data_fits.npy",X_data)
    np.save("y_data_fits.npy",y_data)
