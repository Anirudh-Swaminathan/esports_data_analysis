#!/usr/bin/env python3
import numpy as np
import seaborn as sn
import pandas as pd
from matplotlib import pyplot as plt


def scatter_position(x):
    """
    Function to compute the x and y coordinates on background image given position string
    """
    # weak asserts
    assert isinstance(x, str)
    assert len(x) in [2, 3]
    if len(x) == 2:
        xpos = dict()
        xpos['L'] = 104
        xpos['C'] = 312
        xpos['R'] = 520
        ypos = dict()
        ypos['S'] = 700
        ypos['F'] = 600
        ypos['W'] = 500
        ypos['M'] = 400
        ypos['B'] = 200
        if x == 'ST':
            return [312, 700]
        if x == 'GK':
            return [312, 20]
        return [xpos[x[0]], ypos[x[1]]]
    ypos = dict()
    ypos['AM'] = 500
    ypos['DM'] = 300
    ypos['CM'] = 400
    ypos['CB'] = 200
    ypos['WB'] = 300
    if x[1:] == 'WB':
        if x[0] == 'L':
            return [104, ypos['WB']]
        return [520, ypos['WB']]
    xpos = dict()
    xpos['L'] = 208
    xpos['C'] = 312
    xpos['R'] = 416
    return [xpos[x[0]], ypos[x[1:]]]

def main():
    # load background image
    img = plt.imread("high-resolution-soccer-grass-field-19318961.jpg")
    print(img.shape)
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0,800, 0,533])

    # read data on position
    dat = pd.read_csv("../../../datasets/fifa19/data.csv")
    col_names = list(dat.columns.values)
    positions = dat['Position']
    # get percentages
    counts = positions.value_counts(normalize=True)
    print(type(counts), counts.shape, counts.name)
    print(counts[:5])
    count_inds = counts.index
    print(type(count_inds), count_inds.shape)
    cinds = count_inds.values
    print(type(cinds), cinds.shape, cinds)
    plot_x = list()
    plot_y = list()
    for cin in cinds:
        xyl = scatter_position(cin)
        plot_x.append(xyl[0])
        plot_y.append(xyl[1])
    print(len(plot_x), len(plot_y))
    print(plot_x)
    print(plot_y)
    ax.plot(plot_x, plot_y, color='firebrick')


if __name__ == '__main__':
    main()
