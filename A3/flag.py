def main():
    getInput()


def getInput():
    state = input('Enter the name of the state: ')
    cars(state)


def cars(name):
    if name.lower() == 'texas':
        print('The number of cars in Texas is 120,000')
    elif name.lower() == 'california':
        print('The number of cars in California is 190,000')
    else:
        print('I do not know about this state')


main()