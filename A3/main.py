import math
import energy
import distance

def main():
    choice = 2
    while choice != 0:
        choice = getChoice()
        if choice == 1:
            mass = float(input('Enter mass: '))
            height = float(input('Enter height: '))
            velocity = float(input('Enter velocity: '))

            ke = energy.kineticEnergy(mass, velocity)
            pe = energy.potentialEnergy(mass, height)

            print(ke, pe)

        elif choice == 2:
            velocity_x = float(input('Enter the horizontal velocity: '))
            velocity_y = float(input('Enter the vertical velocity: '))
            time = float(input('Enter the time: '))

            distanceX = distance.horizontal(velocity_x, time)
            distanceY = distance.horizontal(velocity_y, time)

            print(distanceX, distanceY)


def getChoice():
    choice = int(input('Enter 1 for energy 2 for distance calculation and 0 to quit: '))
    return choice

main()





