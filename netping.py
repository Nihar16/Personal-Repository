# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:34:00 2019

@author:Nihar
"""

import os
hostname = input("Enter Host IP Address to Ping:")
response = os.system("ping " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')
