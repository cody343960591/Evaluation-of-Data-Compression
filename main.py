#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# Created on Feb-23-19 15:13
# main.py
# @author: Cody Xu
'''

import read_config
import Algorithms.algo_select

if __name__ == "__main__":
    config = read_config.getConfig()   #get parameters from config.ini
    Algorithms.algo_select.algo(**config)
    