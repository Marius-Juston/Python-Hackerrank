from sklearn.kernel_ridge import KernelRidge
from sklearn.preprocessing import PolynomialFeatures

features, rows = map(int, input().split())

x = []
y = []
for _ in range(rows):
    data = list(map(float, input().split()))
    x.append(data[:-1])
    y.append(data[-1])

poly = PolynomialFeatures(degree=2)
x = poly.fit_transform(x)
clf = KernelRidge(.1, "poly")
clf.fit(x, y)

# import matplotlib.pyplot as plt

# ax = plt.gca(projection="3d")
# import numpy as np

# x = np.array(x)
# ax.scatter(x[:, 0], x[:, 1], y)
# plot_fitting_plane(clf, ax, manipulation=poly)
# plt.show()

predictions = []
for _ in range(int(input())):
    data = list(map(float, input().split()))
    predictions.append(data)

predictions = poly.fit_transform(predictions)
print(*clf.predict(predictions), sep='\n')
