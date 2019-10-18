# imports

from PIL import Image
import requests
from io import BytesIO
import numpy as np

X = [] #np.zeros((89*100, 100, 100))
y = [] # np.zeros(89*100)
for incl in range(0,90):
	print incl
	for spin in range(0,101):
		str_incl = '%03d' % incl
		str_spin = '%03d' % spin
		url = "http://vlbiimaging.csail.mit.edu/static/data/targetImgs/sgraBroderick/pmap_bs_%s_%s_2.png" % (str_spin, str_incl)
		response = requests.get(url)
		img = np.asarray(Image.open(BytesIO(response.content)))
		X.append(img) #[cnt,:,:] = img
		y.append(np.floor(spin/10))
		

path = "/Users/imanwahle/Desktop/CS101/"
np.save(path + "X.npy", X)
np.save(path + "y.npy", y)