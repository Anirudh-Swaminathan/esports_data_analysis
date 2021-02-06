#!/usr/bin/env python3
import numpy as np
import seaborn as sn
import pandas as pd
from matplotlib import pyplot as plt


def main():
    # dat = np.load("../../../datasets/fifa19/data.csv", allow_pickle=True)
    dat = pd.read_csv("../../../datasets/fifa19/data.csv")
    print(dat.shape)
    print(type(dat))
    headers = dat.head()
    print(type(headers), headers.shape)
    col_names = list(dat.columns.values)
    print(len(col_names))
    print(col_names[:5], col_names[-5:])
    nations = dat['Nationality']
    print(nations.shape)
    nations.apply(pd.value_counts).plot.pie(subplots=True)
    plt.show()

if __name__ == '__main__':
    main()
