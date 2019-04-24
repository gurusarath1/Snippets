import matplotlib.pyplot as plt
import numpy as np
import random


def plotStyle(pltX, grid=True, Title='', xlabel='', ylabel=''):
    pltX.legend()
    pltX.grid(grid)
    pltX.title(Title)
    pltX.xlabel(xlabel)
    pltX.ylabel(ylabel)


x = ['Apples','Oranges','Cars','Bikes']
y1 = [5,6,7,8]


plt.figure(1)
plt.bar(x, y1, label = 'Bars')
plotStyle(plt, xlabel='X -------->', ylabel = 'Magnitude', Title = 'Bar')


plt.show()