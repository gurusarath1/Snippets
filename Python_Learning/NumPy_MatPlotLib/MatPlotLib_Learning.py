import matplotlib.pyplot as plt
import numpy as np
import random


def plotStyle(pltX, grid=True, Title='', xlabel='', ylabel=''):
    pltX.legend()
    pltX.grid(grid)
    pltX.title(Title)
    pltX.xlabel(xlabel)
    pltX.ylabel(ylabel)


x = np.linspace(-10 * np.pi, 10 * np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = [random.random()*500 for k in range(40)]

plt.figure(1)
plt.subplot(2, 2, 1)
plt.plot(x, y1, 'r', label = 'Sine')
plotStyle(plt, xlabel='X -------->', ylabel = 'Magnitude', Title = 'Sin')

plt.subplot(2, 2, 2)
plt.plot(x, y2, 'g', label = 'Cosine')
plotStyle(plt, xlabel='X -------->', ylabel = 'Magnitude', Title  = 'Cos')

plt.subplot(2, 2, 3)
plt.plot(x, y3, 'g', label = 'Tangent')
plotStyle(plt, xlabel='X -------->', ylabel = 'Magnitude', Title  = 'Tan' )

plt.subplot(2, 2, 4)
plt.plot([x for x in range(len(y4))], y4, 'v', label = 'random')
plotStyle(plt, xlabel='X -------->', ylabel = 'Magnitude', Title = 'random')

plt.show()

#---------------------------------------------------------------------------------------------------------

plt.figure(2)

x_vals = ['apples', 'oranges', 'pineapples', 'grapes', 'papaya']
y_vals = [2,4,1,5,8]

plt.subplot(1,2,1)
plt.bar(x_vals, y_vals)
plotStyle(plt, xlabel='Fruits -------->', ylabel = 'Number -----> ', Title = 'Number of Fruits chart', grid = False)


plt.subplot(1,2,2)
sliceNames = ['apples', 'oranges', 'pineapples', 'grapes', 'papaya']
slices = [3,7,4,9,5]
Explode_Slice = [0,0.1,0,0,0.5]
slice_colors = ['r','b','m','g','y']
plt.pie(slices,
        labels = sliceNames,
        explode = Explode_Slice,
        shadow = True,
        colors = slice_colors)

plt.show()

#---------------------------------------------------------------------------------------------------------

plt.figure(3)
bins = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
vals = [55,62,83,34,17,2,3,1,1,93,42,8,77,545,7,434,67,45,94,56,45,56,34,73,36,78,27,97,45,80,33,77,46,37,98]
plt.hist(vals, bins, color = 'r', label = 'hist')
plotStyle(plt, xlabel='bins -------->', ylabel = 'frequency -----> ', Title = 'Histogram', grid=False)

plt.show()

#---------------------------------------------------------------------------------------------------------