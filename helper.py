import urllib.request

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from skimage import measure


def plot_hyperplane(clf, ax: Axes = None, interval: float = .05, alpha=.3,
                    colors: list = ('r', 'b'), y=None) -> Line3DCollection:
    """
Plots the hyperplane of the model in an axes
    :param clf: the classifier to use to find the hyperplane
    :param ax: the axes to plot the hyperplane into
    :param interval: the precision of the the hyperplane rendering.
    :return: the mesh of the created hyperplane that was added to the axes
    """

    is_3d = False

    if ax is None:
        try:
            clf.predict([[0, 0, 0]])
            is_3d = True
            ax = plt.gca(projection="3d")
        except ValueError:
            is_3d = False
            ax = plt.gca()

    elif isinstance(ax, Axes3D):
        is_3d = True

    interval = int(1 / interval)

    # get the separating hyperplane
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    # create grid to evaluate model
    xx = np.linspace(x_min, x_max, interval)
    yy = np.linspace(y_min, y_max, interval)

    if is_3d:
        z_min, z_max = ax.get_zlim()

        zz = np.linspace(z_min, z_max, interval)

        yy, xx, zz = np.meshgrid(yy, xx, zz)

        if hasattr(clf, "decision_function"):
            z = clf.decision_function(np.c_[xx.ravel(), yy.ravel(), zz.ravel()])
        elif hasattr(clf, "predict_proba"):
            z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel(), zz.ravel()])[:, 1]
        z = z.reshape(xx.shape)

        vertices, faces, _, _ = measure.marching_cubes(z, 0)
        # Scale and transform to actual size of the interesting volume
        vertices = vertices * [x_max - x_min, y_max - y_min, z_max - z_min] / interval
        vertices += [x_min, y_min, z_min]
        # and create a mesh to display
        mesh = Line3DCollection(vertices[faces],
                                facecolor=colors, alpha=alpha)

        ax.add_collection3d(mesh)

        return mesh
    else:
        xx, yy = np.meshgrid(xx,
                             yy)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        return ax.contourf(xx, yy, Z, 10, colors=colors, alpha=alpha)


def download_file(url, file_name):
    urllib.request.urlretrieve(url, file_name)


def plot_fitting_plane(clf, ax, number: int = 50, color=None, manipulation=None):
    x_min, x_max = ax.get_xlim()

    if isinstance(ax, Axes3D):
        y_min, y_max = ax.get_ylim()
        yy, xx = np.meshgrid(np.linspace(y_min, y_max, number), np.linspace(x_min, x_max, number))

        predict = np.c_[xx.ravel(), yy.ravel()]

        if manipulation is not None:
            predict = manipulation.fit_transform(predict)

        z = clf.predict(predict)
        z = z.reshape(xx.shape)

        return ax.plot_wireframe(xx, yy, z, facecolors=color)
    else:
        x = np.linspace(x_min, x_max, number)
        x = x.reshape(-1, 1)
        y = clf.predict(x)

        return ax.plot(x, y, c=color)
