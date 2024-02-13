import matplotlib.pyplot as plt
import numpy as np

# use NumPy to randomly generate an array with 100 values,
# where the values will concentrate around 80, and the standard deviation is 5.

# In probability theory this kind of data distribution is known as the
# normal data distribution, or the Gaussian data distribution

x = np.random.normal(80, 5, 100)

plt.hist(x)
plt.show()