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
    counts = nations.value_counts()
    print(type(counts), counts.shape, counts.name)
    print(counts[:5])
    count_inds = counts.index
    print(type(count_inds), count_inds.shape)
    cinds = count_inds.values
    print(type(cinds), cinds.shape, cinds[:5])
    nations = nations[:4]
    print(nations.shape)
    counts.plot.pie(label="sample label", autopct="%.2f%%", title="Nationality Distribution: FIFA 19 Players")
    plt.savefig('f19_nationality.png')
    plt.show()

if __name__ == '__main__':
    main()
