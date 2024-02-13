import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


# Creating subplots
fig, axes = plt.subplots(nrows=2, ncols=2)

# Top-left plot (line plot)
axes[0, 0].plot(x, y)
axes[0, 0].set_title('Line Plot')

# Top-right plot (scatter plot)
axes[0, 1].scatter(x, y)
axes[0, 1].set_title('Scatter Plot')

# Bottom-left plot (bar plot)
labels = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 5, 2, 8]
axes[1, 0].bar(labels, values)
axes[1, 0].set_title('Bar Plot')

# Bottom-right plot (histogram)
x = np.random.normal(80, 5, 100)
axes[1, 1].hist(x)
axes[1, 1].set_title('Histogram')

# Adjust layout to prevent overlapping labels
plt.tight_layout()

# Show subplots
plt.show()
