import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,10,11)
b = a ** 4
x = np.arange(0,10)
y = 2 * x

(fig,axes) = plt.subplots(nrows=1, ncols=2) # returns figure and 1x2 numpy array
axes[0].plot(x,y)
axes[1].plot(a,b)
plt.show()

(fig,axes) = plt.subplots(nrows=2, ncols=2) # 2x2 mupy array; axes[0] is still a numpy array
fig.suptitle('Figure Level', fontsize=16)
axes[0][0].plot(x,y)
axes[0][0].set_title('Title 0,0')
axes[0][1].plot(a,b)
plt.tight_layout() # provents overlapping between axis numbers
plt.subplots_adjust(wspace=0.9) # manually sets the space occupied by the subplots in the figure
fig.savefig('ex3.png', bbox_inches='tight')
plt.show()

