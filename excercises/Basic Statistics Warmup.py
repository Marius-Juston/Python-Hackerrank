input()
import numpy as np
from scipy.stats import mode

array = np.array(list(map(int, input().split())))

mean = np.mean(array)
print(mean)
print(np.median(array))

print(sorted(mode(array)[0])[0])

standard_deviation = np.std(array)
print("{0:0.1f}".format(standard_deviation))

confidence_error = 1.96 * (standard_deviation / np.sqrt(array.shape[0]))

print("{0:0.1f} {1:0.1f}".format(mean - confidence_error, mean + confidence_error))
