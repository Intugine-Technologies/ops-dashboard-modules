import numpy as np
import sys


def main(val):
    file = open('config_battery', 'r').read().split('\n')
    x, y = list(), list()
    for line in file[1:]:
        x.append(float(line.split(' ')[0]))
        y.append(float(line.split(' ')[1]))
    coeff = np.polyfit(y, x, 7)
    print(round(float(np.polyval(coeff[::], val)), 2))


if __name__ == '__main__':
    main(float(sys.argv[1]))
