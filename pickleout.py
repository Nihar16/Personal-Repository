# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:50:35 2019

@author: Shrikant
"""

import pickle

# open a file, where you stored the pickled data
file = open('important', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

print('Showing the pickled data:')

cnt = 0
for item in data:
    print('The data ', cnt, ' is : ', item)
    cnt += 1
    
    pickle.