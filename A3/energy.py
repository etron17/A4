import math


def kineticEnergy(mass, velocity):
    ke = 0.5 * mass * math.pow(velocity, 2)
    return ke


def potentialEnergy(mass, height):
    gravity = 9.8
    return mass * height * gravity
