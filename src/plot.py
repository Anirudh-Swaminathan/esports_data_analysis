from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
# Though the following import is not directly being used, it is required
# for 3D projection to work
from mpl_toolkits.mplot3d import Axes3D


# estimators = [('k_means_3', KMeans(n_clusters=3))]
#
# fig = plt.figure()
# ax = plt.axes(projection="3d")
#
# est = KMeans(n_clusters=3)
# est.fit(X)
# labels = est.labels_
#
# ax.scatter(X[:, 0], X[: , 1], X[:, 2],
#            c=labels.astype(float), edgecolor='k')
# ax.text(X[:,0],X[:,1],X[:,2],  '%s' % (str(i)), size=20, zorder=1,
#  color='k')
#
# ax.set_xlabel('Age')
# ax.set_ylabel('Overall Rating')
# ax.set_zlabel('Wage')
# ax.set_title('Clubs')
#
# plt.show()

import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import proj3d

def visualize3DData (X, labels, indexes):
    """Visualize data in 3d plot with popover next to mouse position.

    Args:
        X (np.array) - array of points, of shape (numPoints, 3)
    Returns:
        None
    """

    plt.rc('font', size=20)          # controls default text sizes
    plt.rc('axes', titlesize=20)     # fontsize of the axes title
    plt.rc('axes', labelsize=18)
    plt.rcParams.update({'font.size': 8})

    fig = plt.figure(figsize = (16,10))
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels.astype(float), edgecolor='k', depthshade = False, picker = True)

    ax.set_xlabel('Age')
    ax.set_ylabel('Overall Rating')
    ax.set_zlabel('Wage')
    ax.set_title('FIFA Clubs')

    def distance(point, event):
        """Return distance between mouse position and given data point

        Args:
            point (np.array): np.array of shape (3,), with x,y,z in data coords
            event (MouseEvent): mouse event (which contains mouse position in .x and .xdata)
        Returns:
            distance (np.float64): distance (in screen coords) between mouse pos and data point
        """
        assert point.shape == (3,), "distance: point.shape is wrong: %s, must be (3,)" % point.shape

        # Project 3d data space to 2d data space
        x2, y2, _ = proj3d.proj_transform(point[0], point[1], point[2], plt.gca().get_proj())
        # Convert 2d data space to 2d screen space
        x3, y3 = ax.transData.transform((x2, y2))

        return np.sqrt ((x3 - event.x)**2 + (y3 - event.y)**2)


    def calcClosestDatapoint(X, event):
        """"Calculate which data point is closest to the mouse position.

        Args:
            X (np.array) - array of points, of shape (numPoints, 3)
            event (MouseEvent) - mouse event (containing mouse position)
        Returns:
            smallestIndex (int) - the index (into the array of points X) of the element closest to the mouse position
        """
        distances = [distance (X[i, 0:3], event) for i in range(X.shape[0])]
        return np.argmin(distances)


    def annotatePlot(X, index):
        """Create popover label in 3d chart

        Args:
            X (np.array) - array of points, of shape (numPoints, 3)
            index (int) - index (into points array X) of item which should be printed
        Returns:
            None
        """
        # If we have previously displayed another label, remove it first
        if hasattr(annotatePlot, 'label'):
            annotatePlot.label.remove()
        # Get data point from array of points X, at position index
        x2, y2, _ = proj3d.proj_transform(X[index, 0], X[index, 1], X[index, 2], ax.get_proj())
        annotatePlot.label = plt.annotate( "%s" % indexes[index],
            xy = (x2, y2), xytext = (-20, 20), textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
        fig.canvas.draw()


    def onMouseMotion(event):
        """Event that is triggered when mouse is moved. Shows text annotation over data point closest to mouse."""
        closestIndex = calcClosestDatapoint(X, event)
        annotatePlot (X, closestIndex)

    fig.canvas.mpl_connect('motion_notify_event', onMouseMotion)  # on mouse motion
    plt.show()


if __name__ == '__main__':
    fifa = pd.read_csv('fifa.csv')

    teams_fifa = fifa[['Club', 'Age', 'Overall', 'Wage']] # Value, Wage, Height, Weight, Release Clause

    # convert player wages to sensible units
    # remove euro sign
    wages = teams_fifa.Wage.apply(lambda x: x[1:])
    # convert M and K by their respective multipliers
    teams_fifa.Wage = wages.apply(lambda x: float(x[:-1])*1e6 if "m" in x.lower() else (float(x[:-1])*1000 if "k" in x.lower() else float(x)))

    teams = teams_fifa.groupby('Club').median()

    X = teams.values

    est = KMeans(n_clusters=3)
    est.fit(X)
    labels = est.labels_
    indexes = teams.index
    visualize3DData (X, labels, indexes)
