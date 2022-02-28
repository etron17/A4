# Student name: Dojae Kim
# Student number: 400420323
# Student email: kim408@mcmaster.ca
# Lecture: SFWRTECH 3PR3
# Assignment 2 Part 1

import math

distance = float(input('Enter your distance [5 - 10]: '))
while distance < 5 or distance > 10:
    distance = float(input('Please enter distance [5 - 10]: '))

initial_velocity = float(input('Enter initial velocity [1 - 10]: '))
while initial_velocity < 1 or initial_velocity > 10:
    initial_velocity = float(input('Please enter initial velocity [1 - 10]: '))

acceleration = float(input('Enter acceleration [-100 - 0]: '))
while acceleration < -100 or acceleration > 0:
    acceleration = float(input('Please enter acceleration [-100 - 0]: '))

travel_time = float(input('Enter travel time less than 10: '))
while travel_time >= 10:
    travel_time = float(input('Please enter travel time less than 10: '))

displacement = (initial_velocity * travel_time) + (0.5 * acceleration) * (math.pow(travel_time, 2))

print('\n====================================================')

if displacement >= distance:
    print('\tThe object will collide')
    print('====================================================')
    print('Distance \t\t\t Displacement')
    print(distance, 'm', '\t\t\t\t', displacement, 'm')


else:
    print('\tThe object will not collide')
    print('====================================================')
    print('Distance \t\t\t Displacement')
    print(distance, 'm',  '\t\t\t\t', displacement, 'm')
print('====================================================')
