import numpy as np
from sklearn.linear_model import LinearRegression

data = np.genfromtxt("trainingdata.txt", delimiter=",")
x, y = data[:, 0], data[:, 1]

x = x.reshape(-1, 1)

left = x[x <= 4]

# s = float(input().strip())
s = .09

clf = LinearRegression()

import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.show()

mask = x.ravel() > 4.0
clf.fit(x[mask], y[mask])
print(clf.coef_[0], clf.intercept_)

mask = x.ravel() <= 4.0
clf.fit(x[mask], y[mask])
print(clf.coef_[0], clf.intercept_)

print("{0:.2f}".format(*clf.predict([[s]])))
