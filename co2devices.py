#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:05:42 2020

@author: hannahjohnson
"""
from co2properties import ClientProperties
                  
def total_device_energy(data):
    clientprop = ClientProperties()
    #lifetimes given in hours
    lifetime = {'laptop': 35040, 'desktop' : 35040, 'LED screen': 100000, 'Plasma screen': 45000, 'High performance codec': 87600, 'Low performance codec': 87600, 'Camera': 70080, 'Speaker' : 17520, 'Microphone' : 175200, 'Router' : 30660}    
    energy = 0
    hours = data['Hours']
    operating_seconds = hours * 3600
    # operating energy = power in watts * seconds (in joules)
    #energy from manufacturing = total manufacturing energy * hours used / lifetime (in joules)
    
    # add energy from the laptops
    energy += data['Number of laptops'] * clientprop.laptop.power * operating_seconds
    energy += data['Number of laptops'] * clientprop.laptop.manufacture_energy * hours/lifetime['laptop'] / 10**6
    
    # add energy from the desktops
    energy += data['Number of desktops'] * clientprop.personal_comp.power * operating_seconds
    energy += data['Number of desktops'] * clientprop.personal_comp.manufacture_energy * hours/lifetime['desktop'] / 10**6
    
    # add energy from the desktop screens
    area_desktop = 0.24 #average desktop size approximately 60cmx40cm
    energy += data['Number of desktops'] * (data['Percentage LED and LCD']/100) * clientprop.ledlcd(area_desktop).power
    energy += data['Number of desktops'] * (data['Percentage LED and LCD']/100) * clientprop.ledlcd(area_desktop).manufacture_energy * 10**6 * hours/lifetime['LED screen'] 
    
    energy += data['Number of desktops'] * ((100 - data['Percentage LED and LCD'])/100) * clientprop.plasma(area_desktop).power
    energy += data['Number of desktops'] * ((100 - data['Percentage LED and LCD'])/100) * clientprop.plasma(area_desktop).manufacture_energy * 10**6 * hours/lifetime['Plasma screen']
    
    # add energy from extra screens
    
    energy += data['Number of extra LCD/LED screens'] * clientprop.ledlcd(data['Area of extra LED/LCD screens']).power
    energy += data['Number of extra LCD/LED screens'] * clientprop.ledlcd(data['Area of extra LED/LCD screens']).manufacture_energy * 10**6 * hours/lifetime['LED screen'] 
    
    energy += data['Number of extra plasma screens'] * clientprop.ledlcd(data['Area of extra LED/LCD screens']).power
    energy += data['Number of extra plasma screens'] * clientprop.ledlcd(data['Area of extra plasma screens']).manufacture_energy * 10**6 * hours/lifetime['Plasma screen'] 
    
    # add energy from CODECs
    energy += data['Number of high performance CODECs'] * clientprop.high_codec.power * operating_seconds
    energy += data['Number of high performance CODECs'] * clientprop.high_codec.manufacture_energy * 10**6 * hours/lifetime['High performance codec'] 

    energy += data['Number of low performance CODECs'] * clientprop.low_codec.power * operating_seconds
    energy += data['Number of low performance CODECs'] * clientprop.low_codec.manufacture_energy * 10**6 * hours/lifetime['Low performance codec'] 
    
    # add operating energy from cameras, speakers, microphones and routers
    energy += data['Number of cameras'] * clientprop.camera.power * operating_seconds
    energy += data['Number of speakers'] * clientprop.speaker.power * operating_seconds
    energy += data['Number of microphones'] * clientprop.microphone.power * operating_seconds
    energy += data['Number of routers'] * clientprop.router.power * operating_seconds
    
    # add manufacturing energy from cameras, speakers, microphones and routers
    energy += data['Number of cameras'] * clientprop.camera.manufacture_energy * 10**6 * hours/lifetime['Camera'] 
    energy += data['Number of speakers'] * clientprop.speaker.manufacture_energy * 10**6 * hours/lifetime['Speaker']
    energy += data['Number of microphones'] * clientprop.microphone.manufacture_energy * 10**6 * hours/lifetime['Microphone']
    energy += data['Number of routers'] * clientprop.router.manufacture_energy * 10**6 * hours/lifetime['Router'] 
    
    return energy
    
        
        
        
        
        
        
        
        
        