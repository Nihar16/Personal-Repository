import matplotlib.pyplot as plt
x=[2011,2013,2015,2019]
Fe=[77,86,89,98]
Al=[21,24,29,33]
Cu=[68,72,77,85]
plt.figure(figsize=(12,9))
plt.xlabel('Years')
plt.ylabel('Metal')
plt.bar(x,Fe,color='r',label='Fe')
plt.bar(x,Al,color='b',label='Al')
plt.bar(x,Cu,color='g',label='Cu')
plt.rcParams['font.size']=18
plt.rcParams['font.family']='consolas'
plt.legend()
plt.grid(color='red',lw=1,ls='-',alpha=0.4)
plt.show()