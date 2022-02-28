import matplotlib.pyplot as plt
from numpy import *

current_height = 20
g = 10  # gravitational force
u = 0   # initial velocity


time = arange(0, 16, 0.04)
y_axis = zeros(size(time))

plt.plot(time, current_height, 'bo')
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.show()
