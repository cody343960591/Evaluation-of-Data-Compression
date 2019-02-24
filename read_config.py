#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# Created on Feb-23-19 15:14
# read_config.py
# @author: Cody Xu
'''
from configparser import ConfigParser

def getConfig():
    config = ConfigParser()
    config.read('config.ini')

    config_data = {}

    algorithm = config['RUN']['algorithm'].split(';')
    config_data['algorithm'] = algorithm
    config_data['data_category'] = config['RUN']['data_category']
    config_data['outlier'] = config['RUN']['outlier']
    config_data['esp'] = config['INPUT']['esp']
    config_data['numOfEsp'] = config['INPUT']['numOfEsp']
    config_data['numOfUpdateFrequency'] = config['INPUT']['numOfUpdateFrequency']
    config_data['update_frequency'] = config['INPUT']['update_frequency']

    algorithm_param = {}
    for x in algorithm:
        algorithm_param[x] = {}
        algorithm_param[x]['folderPath_input'] = config[x]['folderPath_input'].replace('"','')
        algorithm_param[x]['folderPath_output'] = config[x]['folderPath_output'].replace('"','')
        if x == 'GAMPS':
            algorithm_param[x]['prefix_baseSignal'] = config[x]['prefix_baseSignal'].replace('"','')
            algorithm_param[x]['prefix_ratioSignal'] = config[x]['prefix_ratioSignal'].replace('"','')
            algorithm_param[x]['prefix_Approx'] = config[x]['prefix_Approx'].replace('"','')
        else:
            algorithm_param[x]['prefix_compressedData'] = config[x]['prefix_compressedData'].replace('"','')
            algorithm_param[x]['prefix_approxData'] = config[x]['prefix_approxData'].replace('"','')
            if x == 'CHEB':
                algorithm_param[x]['seg_length'] = config[x]['seg_length']
            elif x == 'PCA':
                algorithm_param[x]['window_size'] = config[x]['window_size']
            else:
                pass
    config_data['algorithm_param'] = algorithm_param

    return config_data
