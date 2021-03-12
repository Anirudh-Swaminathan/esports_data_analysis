#!/usr/bin/env python3
import numpy as np
import seaborn as sn
import pandas as pd
from matplotlib import pyplot as plt



def main():
    # read data on position
    data_19 = pd.read_csv("../../../datasets/fifa20/players_19.csv")
    data_20 = pd.read_csv("../../../datasets/fifa20/players_20.csv")
    # choose the subset of name, wage, value, Overall, Age, Contract Expriy, Club name
    ends_19 = data_19[data_19['contract_valid_until'] == 2019]
    print(data_19.shape)
    print(data_20.shape)
    print(ends_19.shape)
    trans_20 = pd.merge(data_20, ends_19, on='short_name')
    print(trans_20.shape)
    n_retired = ends_19.shape[0] - trans_20.shape[0]
    re = n_retired / ends_19.shape[0] * 100.0
    print("Number retired is {}".format(n_retired))
    print("Percentage retired is {}%".format(re))
    print(trans_20.columns)
    print(trans_20['contract_valid_until_x'])
    print(trans_20['contract_valid_until_y'])
    extended_inds = trans_20['club_x'] == trans_20['club_y']
    print(extended_inds)
    vc = extended_inds.value_counts()
    # 0: false, 1: true
    pe = vc[1] / (ends_19.shape[0]) * 100.0
    print("Percentage of players who extended their contract is {}%".format(pe))

    fig, ax = plt.subplots()
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['text.color'] = '#000000'
    plt.rcParams['axes.labelcolor']= '#909090'
    plt.rcParams['xtick.color'] = '#909090'
    plt.rcParams['ytick.color'] = '#909090'
    plt.rcParams['font.size']=12

    color_palette_list = ['#7d3c98', '#2ecc71' , '#3498db']
    
    labels = ['Retired', 'Extended', 'Transferred']
    percentages = [re, pe, 100.0-re-pe]
    ax.pie(percentages, labels=labels, colors=color_palette_list, autopct='%1.0f%%', shadow=False, pctdistance=1.2, labeldistance=0.4)
    ax.axis('equal')
    ax.set_title("Pie chart for 2019 contract expiries")
    ax.legend(frameon=False, bbox_to_anchor=(1.5,0.8))
    plt.savefig("f19_extensions.png")
    plt.show()


if __name__ == '__main__':
    main()
