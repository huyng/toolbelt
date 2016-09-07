import pylab as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.linspace(0, 10, 1000)

plt.clf()
plt.hexbin(x,y, gridsize=20, cmap=plt.cm.jet)
plt.colorbar()
raw_input('press ENTER to exit')
