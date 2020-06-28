#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:10:20 2020

@author: hannahjohnson
"""
from co2datatrans import total_datatrans_energy
from co2devices import total_device_energy
from userinterface import get_data
from co2properties import energy_to_co2

data = get_data()
datatrans = total_datatrans_energy(data)
device = total_device_energy(data)
total_energy = datatrans + device
co2 = 0.6*(total_energy/3600000)
print('The carbon dioxide produced by this videoconference (in kgCO2e) is: ')
print(co2)