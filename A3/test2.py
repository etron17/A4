from matplotlib.pylab import *

# Use the Euler method to compute the trajectory of a bouncing
# ball assuming perfect reflection at the surface x=0.
# Use SI units (meters and seconds)

steps = 300    # number of time steps computed
endtime = 3.0   # end time of simulations
g = 9.8         # acceleration due to gravity

# create 1D arrays of length steps+1 for time (t), position (x), velocity (v)

t = zeros(steps+1)
x = zeros(steps+1)
v = zeros(steps+1)

# initialize variables at time = 0.0

x[0] = 1.0
v[0] = 0.0
t[0] = 0.0

dt = endtime / float(steps)

for i in range (steps):
   t[i+1] = t[i] + dt
   x[i+1] = x[i] + v[i]*dt
   v[i+1] = v[i] - g*dt
   if x[i+1] < 0.0:    # if ball is below surface, reflect it
      x[i+1] = -x[i+1]
      v[i+1] = -v[i+1]

plot(t, x,'bo')
show()