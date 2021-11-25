# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 09:10:50 2019

@author: nihar
"""

import matplotlib.pyplot as plt
plt.rcParams['font.size']=28
plt.rcParams['font.family']='consolas'
labels='Maruti','Toyota','Hundayi','Ferrari','Lamborghini','others'
sizes=[42.5,18.5,7.9,8.2,9.8,13.8]
colors=['red','blue','green','gold','cyan','pink']
explode=(0,0,0,0,0,0)
plt.figure(figsize=(10,10))
plt.pie(sizes,explode=explode,labels=labels,colors=colors,
autopct = '%3.1f%%',shadow='True',startangle=0,
textprops={'fontsize':20})
plt.title('Car Market Shares in India')
plt.axis('equal')
plt.show()
