import numpy as np

x = np.array([15, 12, 8, 8, 7, 7, 7, 6, 5, 3]).reshape(-1, 1)
y = np.array([10, 25, 17, 11, 13, 17, 20, 13, 9, 15]).reshape(-1, 1)

coef, inter = np.polyfit(x.ravel(), y.ravel(), 1)

print("{0:.1f}".format(coef * 10 + inter))
