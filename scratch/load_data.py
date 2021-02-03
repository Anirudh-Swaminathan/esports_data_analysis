#!/usr/bin/env python3
import numpy as np
import seaborn as sn
import pandas as pd
from matplotlib import pyplot as plt


def main():
    # dat = np.load("../../../datasets/fifa19/data.csv", allow_pickle=True)
    dat = pd.read_csv("../../../datasets/fifa19/data.csv")
    print(dat.shape)

if __name__ == '__main__':
    main()
