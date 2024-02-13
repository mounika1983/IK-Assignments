import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Line plot
plt.plot(x, y)
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.show()

# Bar plot
labels = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 5, 2, 8]
plt.bar(labels, values)
plt.show()
