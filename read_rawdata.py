#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# Created on Feb-24-19 15:14
# read_rawdata.py
# @author: Cody Xu
'''
import pandas as pd
import os 

rawdata_name = os.listdir('./testingData/_DATA_')
#print(rawdata_name)
dl = []
for f_path in rawdata_name:
    dl.append(pd.read_csv('./testingData/_DATA_/'+ f_path))
df = pd.concat(dl)
print(df)

df.to_csv('./testingData/test.csv', index=False, header=False)