import numpy as np
import matplotlib as mpl
from matplotlib import patches
from matplotlib import pyplot

mpl.rcParams["figure.figsize"] = [100,100]
figure = pyplot.figure()
ax = figure.add_subplot(111)
ax.set_aspect('equal')
#box = patches.Rectangle(xy=(1.5, 5), width=0.2, height=0.2, linewidth=0.1)
#ax.add_patch(box)
ax.plot([0, 3], [1, 2])
ax.text(1, 1, 'haha', fontsize=30)



print(figure)
pyplot.show()