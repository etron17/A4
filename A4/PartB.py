import math
from typing import List, Tuple
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

DATA_FILENAME = "A04_sfwr_data_03.txt"


def getInputs(filename: str) -> List[float]:
    """
    Read data from file and return list of points
    :param: filename Name of file to read from
    :return: List of points from file
    """
    res: List[float] = []
    with open(filename) as file:
        for line in file:
            res.append(float(line))
    return res


def s_t(t: float, A: float, B: float, C: float, mu: float) -> float:
    """
    Calculate an equation
    :param t: time
    :param A: A constant
    :param B: B constant
    :param C: C constant
    :param mu: mu constant
    :return: Value of equation
    """
    value = 2 * math.pi * t / 120
    return -1 * (A * math.sin(value) + mu) * (math.e ** (B * value / C))


def getFit(data: List[float], A: float, B: float, C: float, mu: float) -> float:
    """
    Calculate fit (MSE) for set of data and A, B and mu
    :param data: Data to check MSE on
    :param A: A for equation
    :param B: B for equation
    :param C: C for equation
    :param mu: mu for equation
    :return: MSE on set of data with A, B, C and mu
    """
    mse = 0
    for i in range(len(data)):
        mse += (s_t(i + 1, A, B, C, mu) - data[i]) ** 2
    return mse / len(data)


def setParameter(data: List[float]) -> \
        Tuple[List[float], float, float, float, float]:
    """
    Find A, B, C, and mu that gives MSE less than 0.5
    :param data: Data to check MSE on
    :return: Tuple with List of MSE on the way to find MSE < 0.5 and A. B, C and mu
    """
    mse: List[float] = []
    step = 5
    A = 0
    B = 0
    C = 10
    mu = 0
    found = False
    for mu in range(0, 201, step):
        if found:
            break
        for A in range(0, 201, step):
            if found:
                break
            for B in range(0, 201, step):
                if found:
                    break
                for C in range(10, 201, step):
                    an_mse = getFit(data, A / 100, B / 100, C / 100, mu / 100)
                    if len(mse) == 0 or mse[-1] > an_mse:
                        mse.append(an_mse)
                    if an_mse < 0.5:
                        found = True
                        break  # Found A, B and mu
    print("The value of A is:", A / 100)
    print("The value of B is:", B / 100)
    print("The value of C is:", C / 100)
    print("The value of mu is:", mu / 100)
    print("The MSE predicted by our model is:", round(mse[-1], 3))
    return mse, A / 100, B / 100, C / 100, mu / 100


def plot_data(data: List[float],
              mse_data: Tuple[List[float], float, float, float, float]) -> None:
    """
    Plot data in 2 subplots
    :param data: Data for left subplot
    :param mse_data: Data for right subplot and line on left one
    :return: None
    """
    mse = mse_data[0]
    A = mse_data[1]
    B = mse_data[2]
    C = mse_data[3]
    mu = mse_data[4]

    model = []
    for i in range(120):
        model.append(s_t(i + 1, A, B, C, mu))

    times = []
    for i in range(120):
        times.append(i / 20)

    tries = []
    for i in range(len(mse)):
        tries.append(i)

    plt.subplot(1, 2, 1)  # the figure has 1 row, 2 columns, and this plot is the first plot.
    plt.title('Login Attempts')
    plt.xlabel('Time')
    plt.ylabel('No. of Attempts')
    plt.xlim([-0.5, 6.5])
    plt.ylim([min(min(data), min(data) - 1), max(max(data), max(data) + 0.5)])

    plt.plot(times, data, 'bo', label='Data')
    plt.plot(times, model, '--r', label='Model')
    plt.legend(loc=2)

    plt.subplot(1, 2, 2)  # the figure has 1 row, 2 columns, and this plot is the second plot.
    plt.title('Model Tuning')
    plt.xlabel('Iterations')
    plt.ylabel('MSE')
    plt.xlim([-1, len(mse) + 1])
    plt.ylim([-1, max(mse) + 1])
    plt.plot(tries, mse, '-b')

    plt.show()


if __name__ == '__main__':
    data = getInputs(DATA_FILENAME)
    mse_data = setParameter(data)

    # Plot the data
    plot_data(data, mse_data)
