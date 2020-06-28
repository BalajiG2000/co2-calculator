#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 17:50:22 2020

@author: hannahjohnson
"""

from co2properties import ServerProperties

def total_datatrans_energy(data):
    serverprop = ServerProperties()
    energy = 0
    hours = data['Hours']
    operating_seconds = hours * 3600
    if data['Bound'] == 'upper':
        #network opex
        energy += serverprop.power_video_high * operating_seconds
        #embodied energy
        energy += serverprop.embodied_energy_intensity_high * serverprop.video_bandwidth_high * operating_seconds * 10**3
    else:
        #network opex
        energy += serverprop.power_video_low * operating_seconds
        #embodied energy
        energy += serverprop.embodied_energy_intensity_low * serverprop.video_bandwidth_low * operating_seconds * 10**3
        
    return energy