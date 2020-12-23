# https://matplotlib.org
# https://matplotlib.org/gallery.html
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y = 2*x
plt.plot(x, y)
plt.title('String Title')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.xlim(0, 6) # limits on x axis
plt.ylim(0, 15) # limits on y axis
plt.savefig('ex.png')
plt.show()

