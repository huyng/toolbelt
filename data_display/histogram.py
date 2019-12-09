import pylab as plt
import numpy as np

# Histogram
fig = plt.figure()
fig.clf()
ax = fig.add_subplot(111)
ax.hist(np.random.rand(1000), bins=100)
input('press ENTER to exit')
