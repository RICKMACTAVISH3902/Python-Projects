# Graph Plotting of Functions

import matplotlib.pyplot as plt
import math as mt
xi = -5
xf = +5
np = 100  # number of points
dx = (xf - xi) / (np - 1)  # range
xx = []
yy = []
for i in range(np):
    x = xi + i * dx
    y = mt.exp(-0.01 * x * x)
    xx.append(x)
    yy.append(y)
print(y)
plt.plot(xx, yy)
plt.show()
