import matplotlib.pyplot as plt
from numpy import *

__author__ = "Matt Carney"
__copyright__ = "Copyright 2014"
__credits__ = [""]
__license__ = "MIT"
__maintainer__ = "Matt Carney"
__email__ = "matt.carney@cba.mit.edu"
__status__ = "Prototype"

y_0 = 10  # initial height
ydot_0 = 0  # initial velocity
yddot = -9.81  # accel due to gravity
x_0 = 0
xdot_0 = 1
xddot_0 = 0
dt = 0.01  # delta time
COR = .8  # coefficient of restitution <1 is realistic-ish elastic with some energy loss

time = arange(0, 20, dt)
y = zeros(size(time))
y[0] = y_0
y_prev = 0
t_local = 0
cntr = 0

for idx, t in enumerate(time):
    t_local = dt * cntr

    y[idx] = y_0 + ydot_0 * t_local + yddot * t_local ** 2 / 2

    if y[idx] <= 0.0:
        ydot_0 = COR * (y_prev - y[idx]) / dt
        y_0 = 0  # must be at edge, reset height to this value
        t_local = 0  # reset time
        cntr = 0  # reset counter
        """
        print "y pos testing condition %02f" % y[idx]
        print "y prev. pos %02f" % y_prev
        print "time %01f" % t
        print "new velocity %02f" % ydot_0
        print "next"
        """

    # calculate position

    y_prev = y[idx]  # store previous time value
    cntr = cntr + 1  # increment counter
    """
    print "y pos outside if %02f" % y[idx]
    print "current time %02f" % t_local
    print "counter value %d" % cntr
    """

plt.plot(time, y, 'bo')
plt.ylabel("Height [m]")
plt.xlabel("Time [sec]")
plt.title("Bouncing Ball Trajectory dt = %0.2f sec" % dt)
plt.show()

