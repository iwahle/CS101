from PIL import Image
import requests
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


imgs = []	
for incl in [10, 30, 50, 70, 89]:
	print(incl)
	for spin in [10, 30, 50, 70, 90]:
		str_incl = '%03d' % incl
		str_spin = '%03d' % spin
		url = "http://vlbiimaging.csail.mit.edu/static/data/targetImgs/sgraBroderick/pmap_bs_%s_%s_2.png" % (str_spin, str_incl)
		response = requests.get(url)
		imgs.append(Image.open(BytesIO(response.content)))

# get the image size
x,y = imgs[0].size

# generate new large image
ncol = 5
nrow = 5
cvs = Image.new('RGB',(x*ncol,y*nrow))

for i in range(len(imgs)):
    px, py = x*int(i/nrow), y*(i%nrow)
    cvs.paste(imgs[i],(px,py))

fig, ax = plt.subplots()
ax.imshow(cvs)
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/5))
ax.xaxis.set_major_formatter(ticks_x)

ticks_y = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(np.abs(500 - y)/5))
ax.yaxis.set_major_formatter(ticks_y)

ax.set_xlabel("inclination")
ax.set_ylabel('spin')
#cvs.save('/Users/Sun/Documents/Caltech/Sophomore Year/CS101/spin_vs_inclination.bmp')
plt.savefig("/Users/Sun/Documents/Caltech/Sophomore Year/CS101/spin_vs_inclination.png")