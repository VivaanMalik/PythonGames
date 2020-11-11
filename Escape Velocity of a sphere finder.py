# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:37:57 2020

@author: ashish
"""

#XD

import math
M = input(print("Enter mass in kg"))
G = 6.67*(math.pow(10,-11))
radius_unit = input(print("Enter unit of radius-km,m"))
R = input(print("Enter Radius"))
if radius_unit == "km":
    Esc_v = math.sqrt((2*G*M)/R)
elif radius_unit == "m" :
    R = R/1000
    Esc_v = math.sqrt((2*G*M)/R)
print(Esc_v)