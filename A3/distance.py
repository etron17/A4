import math

def horizontal(velocity, time):
    distanceX = velocity * time
    return distanceX

def vertical(velocity, time):
    gravity = 9.8
    distanceY = velocity * time + 0.5 * gravity * math.pow(time, 2)
    return distanceY

