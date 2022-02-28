# Student name: Dojae Kim
# Student number: 400420323
# Student email: kim408@mcmaster.ca
# Lecture: SFWRTECH 3PR3
# Assignment 2 Part 2

import math
import numpy

displacement = 0

distance = float(input('\nPlease enter distance [5 - 10]: '))
while distance < 5 or distance > 10:
    distance = float(input('\nDistance is out of bounds, please enter distance [5 - 10]: '))

initial_velocity = float(input('\nPlease enter initial velocity [1 - 10]: '))
while initial_velocity < 1 or initial_velocity > 10:
    initial_velocity = float(input('\nVelocity is out of bounds, please enter initial velocity [1 - 10]: '))

print('\n===============================================================================================================')
print('Distance', '\t', 'Displacement', '\t\t', 'Acceleration', '\t\t', 'Travel Time', '\t\t\t', 'Description')
print('===============================================================================================================')
while True:
    for acc in numpy.arange(-50.0, 0.0, 0.2):
        for time in numpy.arange(0.0, 10.0, 0.1):
            displacement = (round(initial_velocity, 2) * round(time, 2)) + (0.5 * round(acc, 2)) * (round(math.pow(time, 2), 2))
            round(displacement, 2)
            if displacement < distance:
                print(round(distance, 2), 'm', '\t\t', round(displacement, 2), 'm', '\t\t', round(acc, 2), 'm/s^2', '\t\t', round(time, 2), '\t\t', 'Object A will not hit object B')
            elif displacement >= distance:
                print(round(distance, 2), 'm', '\t\t', round(displacement, 2), 'm', '\t\t', round(acc, 2), 'm/s^2', '\t\t', round(time, 2), '\t\t', 'Object A will hit object B')
    print('===============================================================================================================')
    break


