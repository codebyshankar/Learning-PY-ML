import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

data = np.random.normal(300, 10, 300)

plt.hist(data, bins=50, density=True, alpha=0.6, color='g')

plt.show()

x_axis = np.arange(-30, 30, 0.1)
mean = statistics.mean(x_axis)
stdDev = statistics.stdev(x_axis)

plt.plot(x_axis, norm.pdf(x_axis, mean, stdDev))
plt.show()