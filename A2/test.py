import math
import numpy

displacement = 0

distance = float(input('Enter your distance 5-10: '))
while distance < 5 or distance > 10:
    distance = float(input('Please enter distance 5-10: '))

initial_velocity = float(input('Enter initial velocity 1 - 10: '))
while initial_velocity < 1 or initial_velocity > 10:
    initial_velocity = float(input('Please enter initial velocity 1 - 10: '))

travel_time = float(input('Enter travel time less than 10: '))
while travel_time > 10:
    travel_time = float(input('Please enter travel time less than 10: '))
print('\n=================================================================================================')
print('Distance', '\t', 'Displacement', '\t\t', 'Acceleration', '\t\t\t', 'Description')
while True:
    for acc in numpy.arange(-50.0, 0.0, 0.2):
        displacement = (round(initial_velocity, 2) * round(travel_time, 2)) + (0.5 * round(acc, 2)) * (round(math.pow(travel_time, 2), 2))
        round(displacement, 2)
        if displacement < distance:
            print(round(distance, 2), 'm', '\t\t', round(displacement, 2), 'm', '\t\t', round(acc, 2), 'm/s^2', '\t\t', 'Object A will not hit object B')
        elif displacement >= distance:
            print(round(distance, 2), 'm', '\t\t', round(displacement, 2), 'm', '\t\t', round(acc, 2), 'm/s^2', '\t\t', 'Object A will hit object B')
    print('=================================================================================================')
    break


