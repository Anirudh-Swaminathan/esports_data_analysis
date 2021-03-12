#!/usr/bin/env python3
import numpy as np
import seaborn as sn
import pandas as pd
from matplotlib import pyplot as plt



def main():
    # read data on position
    data_19 = pd.read_csv("../../../datasets/fifa20/players_19.csv")
    data_20 = pd.read_csv("../../../datasets/fifa20/players_20.csv")
    # subset of contracts ending in 2019
    ends_19 = data_19[data_19['contract_valid_until'] == 2019]
    # subset of extended / transferred
    trans_20 = pd.merge(data_20, ends_19, on='short_name')
    n_retired = ends_19.shape[0] - trans_20.shape[0]
    re = n_retired / ends_19.shape[0] * 100.0
    print("Number retired is {}".format(n_retired))
    print("Percentage retired is {}%".format(re))
    extended_inds = trans_20['club_x'] == trans_20['club_y']
    trans_inds = trans_20['club_x'] != trans_20['club_y']
    vc = extended_inds.value_counts()
    # 0: false, 1: true
    pe = vc[1] / (ends_19.shape[0]) * 100.0
    print("Percentage of players who extended their contract is {}%".format(pe))

    # value increases for players who extended their contracts
    n_extends = vc[1]
    v_inds = trans_20.loc[extended_inds]['value_eur_x'] > trans_20.loc[extended_inds]['value_eur_y']
    vic = v_inds.value_counts()
    ve = vic[1] / n_extends * 100.0
    print("The percentage of players who extended their contracts whose value increased is: {}%".format(ve))

    w_inds = trans_20.loc[extended_inds]['wage_eur_x'] > trans_20.loc[extended_inds]['wage_eur_y']
    wic = w_inds.value_counts()
    we = wic[1] / n_extends * 100.0
    print("The percentage of players who extended their contracts whose wage increased is: {}%".format(we))

    n_trans = vc[1]
    va_inds = trans_20.loc[trans_inds]['value_eur_x'] > trans_20.loc[trans_inds]['value_eur_y']
    vaic = va_inds.value_counts()
    vae = vaic[1] / n_trans * 100.0
    print("The percentage of players who transferred to another club whose value increased is: {}%".format(vae))

    wa_inds = trans_20.loc[trans_inds]['wage_eur_x'] > trans_20.loc[trans_inds]['wage_eur_y']
    waic = wa_inds.value_counts()
    wae = waic[1] / n_trans * 100.0
    print("The percentage of players who transferred to another club whose wage increased is: {}%".format(wae))

if __name__ == '__main__':
    main()
