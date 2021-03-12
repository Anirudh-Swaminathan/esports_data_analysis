#!/usr/bin/env python3
import unicodedata

import numpy as np
import seaborn as sn
import pandas as pd
from matplotlib import pyplot as plt

def main():
    dat = pd.read_csv("../../../datasets/fifa19/data.csv")
    wages = dat['Wage']
    # remove euro sign
    wages = wages.apply(lambda x: x[1:])
    # convert M and K by their respective multipliers
    wages = wages.apply(lambda x: float(x[:-1])*1e6 if "m" in x.lower() else (float(x[:-1])*1000 if "k" in x.lower() else float(x)))

    # scatter plot for the correlation
    sn.set(rc={'figure.figsize':(11.7,8.27)})
    ax = sn.scatterplot(x=dat['Overall'], y=wages)
    ytics = ["{}{}K".format(unicodedata.lookup("EURO SIGN"), i*100) for i in range(6)]
    ax.set_yticks([i*1e5 for i in range(6)], ytics)
    ax.set_xlabel("Player OVR")
    ax.set_ylabel("Player Wage")
    ax.set_title("Player Wage vs Player OVR")
    plt.tight_layout()
    plt.savefig("../images/wage_vs_ovr.png")
    plt.show()

if __name__ == '__main__':
    main()
