#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# Created on Feb-24-19 15:13
# algo_select.py
# @author: Cody Xu
'''

def algo(**kw):
    print(kw)
    if 'PCA' in kw['algorithm']:
        #pca()
        print(1)
    if 'APCA' in kw['algorithm']:
        #apca()
        print(2)
    if 'PWLH' in kw['algorithm']:
        #pwlh()
        print(3)
    if 'SF' in kw['algorithm']:
        #sf()
        print(4)
    if 'CHEB' in kw['algorithm']:
        #cheb()
        print(5)
    if 'GAMPS' in kw['algorithm']:
        #gamps()
        print(6)