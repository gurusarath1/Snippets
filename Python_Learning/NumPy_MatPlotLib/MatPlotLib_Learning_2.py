import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(1,100,100)
y = np.linspace(1,100,100)
z = np.random.random(10000)
z.shape = (100,100)
print(z)

ax.plot_surface(x,y,z)

plt.show()