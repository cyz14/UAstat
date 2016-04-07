import numpy as np
from pylab import *
import matplotlib.pyplot as plt

# Create some test data
dx = .01
X  = np.arange(-2,2,dx)
Y  = np.exp(-X**2)

# Normalize the data to a proper PDF
Y /= (dx*Y).sum()

# Compute the CDF
CY = np.cumsum(Y*dx)

# Plot both
plt.plot(X,Y)
plt.plot(X,CY,'r--')

plt.show()