import matplotlib.pyplot as plt
import numpy as np
import pylab as p

plt.figure(figsize=(12,9))
plt.rcParams['font.size']=18
plt.rcParams['font.family']='consolas'
plt.title('Trigonometry')
x= p.arange(-1.0,1.0,0.1)
y= (p.sin(2*p.pi*x)) / (p.cos(2*p.pi*x))

p.plot(x,y,'g-',lw=2)
p.show()
plt.xlabel('Angle in rad')
plt.ylabel('Tangent\Cotangent Functions')
plt.text(0,1,'Maxima')
plt.axis([-7,7,-2,2])
plt.annotate('zero',(0,0))
plt.legend()
plt.grid(color='green',lw=1,ls='-',alpha=0.4)
plt.show()