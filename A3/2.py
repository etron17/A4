import math
MASS = 10
GRAVITY = 9.8


def main():
    velocity = float(input('Enter the value of velocity: '))
    height = float(input('Enter the value of height: '))
    kinetic_energy(velocity)
    potential_energy(height)


def kinetic_energy(velocity):
    kenergy = 0.5 * MASS * math.pow(velocity, 2)
    print('Kinetic energy = ', kenergy)


def potential_energy(height):
    penergy = MASS * GRAVITY * height
    print('potential energy = ', penergy)


main()
