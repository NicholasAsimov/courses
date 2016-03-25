import matplotlib.pyplot as pylab
import numpy as np


def load_data():
    with open('julyTemps.txt', 'r') as f:
        raw_data = f.readlines()[6:]
        high = []
        low = []

        for line in raw_data:
            fixed_line = line.strip().split()
            high.append(int(fixed_line[1]))
            low.append(int(fixed_line[2]))

        return (low, high)


def produce_plot(low, high):
    diffTemps = np.array(high) - np.array(low)
    pylab.plot(diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()


(low, high) = load_data()
produce_plot(low, high)
