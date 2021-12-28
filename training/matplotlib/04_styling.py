import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,11,10)

# legends
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x, label='X vs X')
ax.plot(x,x**2, label='X vs X^2')
#ax.legend(loc='lower left')
ax.legend(loc=(1.1, 0.5)) # outside the canvas
plt.show()
fig.savefig('ex4.png', bbox_inches='tight') # includes legend out of canvas

# colors, line styles
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x, x, color='lightblue', linewidth=1.5, ls='-.', 
    marker='o', 
    markersize=5,
    markerfacecolor='red',
    markeredgewidth=4,
    markeredgecolor='orange')
ax.plot(x, x**3, color='#650dbd', lw=10, ls='--')
lines = ax.plot(x, -x, color='red', lw=5)
lines[0].set_dashes([1,1,1,2,3,5]) # custom dahs-white space sequence
ax.legend()
plt.show()