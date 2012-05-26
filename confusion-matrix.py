import numpy as np
from matplotlib import pyplot as plt


# inputs
klasses = [i*5 for i in  'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
conf_arr = [[33,2,0,0,0,0,0,0,0,1,3], 
            [3,31,0,0,0,0,0,0,0,0,0], 
            [0,4,41,0,0,0,0,0,0,0,1], 
            [0,1,0,30,0,6,0,0,0,0,1], 
            [0,15,0,0,38,0,0,0,0,0,0], 
            [0,9,0,3,1,39,0,0,0,0,4], 
            [0,2,2,0,4,1,31,0,0,0,2],
            [0,1,0,0,0,0,0,36,0,2,0], 
            [0,0,0,0,0,0,1,5,37,5,1], 
            [3,0,0,0,0,0,0,0,0,39,0], 
            [0,0,0,0,0,0,0,0,0,0,38]]



width = len(conf_arr)
height = len(conf_arr[0])

narr = np.array(conf_arr, dtype=float)
row_max_arr = np.array(conf_arr).max()
# norm_conf = narr / row_max_arr
norm_conf = narr


# creat figure
fig = plt.figure()
# clear figure
fig.clf()

ax = fig.add_subplot(111)


res = ax.imshow(
        np.array(norm_conf), 
        cmap=plt.cm.gnuplot, 
        interpolation='nearest',
        )

# add annotations
for x in xrange(width):
    for y in xrange(height):
        ax.annotate(
            "%.2f" % norm_conf[x][y], 
            xy=(y, x), 
            horizontalalignment='center',
            verticalalignment='center')

# turn of grid
ax.grid(False)

# show color bar
fig.colorbar(res)

# setup xticks
plt.xticks(np.arange(width), klasses[:width])
plt.yticks(np.arange(height), klasses[:height])

# extend y limit to half a square above and below 
plt.ylim(ymin=height-.5, ymax=-.5)

# move x axis to top
for tick in ax.xaxis.iter_ticks():
    tick[0].label2On = True
    tick[0].label1On = False
    tick[0].label2.set_rotation(45)

raw_input('press ENTER to exit')
