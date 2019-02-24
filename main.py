#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# Created on Feb-23-19 15:13
# main.py
# @author: Cody Xu
'''

import read_config
import sys
sys.path.append('./Algorithms')
import algo_select

if __name__ == "__main__":
    config = read_config.getConfig()   #get parameters from config.ini
    algo_select.algo(**config)
    