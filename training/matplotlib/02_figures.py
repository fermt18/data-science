import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,10,11)
b = a**4
x = np.arange(0,10)
y = 2*x

fig = plt.figure(figsize=(10,8), dpi=100) # blank canvas
axes1 = fig.add_axes([0,0,1,1]) # x0,y0,width ratio,heigt ratio
axes1.plot(a,b)
axes1.set_xlim(0,8)
axes1.set_ylim(0,8000)
axes1.set_xlabel('A')
axes1.set_ylabel('B')
axes1.set_title('Power of 4')

axes2 = fig.add_axes([0.2,0.5,0.25,0.25]) # x0,y0,width ratio,heigt ratio
axes2.plot(a,b)
axes2.set_xlim(1,2)
axes2.set_ylim(0,40)
axes2.set_xlabel('A')
axes2.set_ylabel('B')
axes2.set_title('Zoomed in')
plt.show()

fig.savefig('ex2.png', bbox_inches='tight')

