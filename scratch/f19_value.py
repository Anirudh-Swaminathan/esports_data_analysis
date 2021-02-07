#!/usr/bin/env python3
import numpy as np
import seaborn as sn
import pandas as pd
from matplotlib import pyplot as plt


def main():
    # dat = np.load("../../../datasets/fifa19/data.csv", allow_pickle=True)
    dat = pd.read_csv("../../../datasets/fifa19/data.csv")
    col_names = list(dat.columns.values)
    values = dat['Value']
    print(type(values), values.shape, values.dtype)
    counts = pd.cut(values, bins=5, labels=False, retbins=True)
    print(type(counts), counts.shape, counts.name)
    print(counts[:5])
    count_inds = counts.index
    print(type(count_inds), count_inds.shape)
    cinds = count_inds.values
    print(type(cinds), cinds.shape, cinds[:5])
    counts.plot.pie(label="sample label", autopct="%.2f%%", title="Positional Distribution: FIFA 19 Players")
    plt.savefig('f19_positions.png')
    plt.show()

if __name__ == '__main__':
    main()
