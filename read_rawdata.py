#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# Created on Feb-23-19 15:14
# read_rawdata.py
# @author: Cody Xu
'''
import pandas as pd
import os 

def read_rawdata():
    rawdata_name = os.listdir('./testingData/_DATA_')
    num_file = len(rawdata_name)

    dl = []
    for f_path in rawdata_name:
        dl.append(pd.read_csv('./testingData/_DATA_/'+ f_path, header=None))  #未处理开头问题
    df = pd.concat(dl)
    #df.to_csv('result.csv', header=0, index=0)

    return df, num_file
