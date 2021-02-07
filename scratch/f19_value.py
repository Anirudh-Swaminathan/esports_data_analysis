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
    print(values[:3], values[-3:])
    values = values.apply(lambda x: x[1:])
    print(values[:3], values[-3:])
    # values = values.apply(lambda x: float(x[:-1]))
    values = values.apply(lambda x: float(x[:-1])*1e6 if "m" in x.lower() else (float(x[:-1])*1000 if "k" in x.lower() else float(x)))
    # values = values.apply(lambda x: float(x[:-1])*1000 if "k" in x.lower() else float(x))
    print(values[:3], values[-3:])
    print(type(values), values.shape, values.dtype)
    counts = pd.cut(values, bins=5, labels=False, retbins=True)
    print(type(counts))#, counts.shape, counts.name)
    print(len(counts))
    print(type(counts[0]), type(counts[1]))
    print(counts[0].shape, counts[1].shape)
    print(counts[1])

if __name__ == '__main__':
    main()
