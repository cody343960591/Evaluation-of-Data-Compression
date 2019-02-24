#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# Created on Feb-24-19 22:06
# pca.py
# @author: Cody Xu
'''
import pandas as pd

def pca(df, num, **kw): 
    max_value = df.max()[0]
    min_value = df.min()[0]
    window_size = int(kw['algorithm_param']['PCA']['window_size'])

    dl_out = []

    loc = 0
    while loc < len(df):
        x = [i for i in df[0][loc:loc + window_size]]
        window_max = max(x)
        window_min = min(x)
        if window_max - window_min < (max_value - min_value) * 0.1 * 2:
            x = [(window_max + window_min) / 2] * window_size
        else:
            pass
        new_data = pd.DataFrame(x)
        dl_out.append(new_data)
        loc += window_size
    df_out = pd.concat(dl_out)
    df_out.to_csv('result.csv', header=0, index=0)