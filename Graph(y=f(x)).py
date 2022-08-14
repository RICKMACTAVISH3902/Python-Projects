# Graph Plotting of Functions
import math as mt

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


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
