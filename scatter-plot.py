import matplotlib.pyplot as plt

# use this if your data is already split into x and y vectors
data_x = [1,2,3,4,5]
data_y = [1,3,2,1,5]

# use this if your data is combined as a list of (x,y) tuples
# data_xy = [(1,1), (2,3), (3,2), (4,1), (5,5)]
# data_x, data_y = zip(*data_xy)

# create figure
plt.plot(data_x, data_y, '-o')
plt.show()
raw_input('press ENTER to exit')



