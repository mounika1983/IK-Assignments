import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()

# Line style and color
plt.plot(x, y, linestyle='--', color='red')
plt.show()

# Scatter plot with different marker styles
plt.scatter(x, y, marker='x', color='green')
plt.show()

# Bar plot with custom colors
# Bar plot
labels = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 5, 2, 8]
colors = ['red', 'blue', 'green', 'yellow', 'purple']
plt.bar(labels, values, color=colors)
plt.show()


# Titles, labels, and legends
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

plt.plot(x, y, label='Line 1')
plt.plot(y, x, label='Line 2')
plt.legend()
plt.show()


# X-axis values
x = [1, 2, 3, 4, 5]

# Y-axis values
y1 = [1, 2, 3, 4, 5]

# Y-axis values
y2 = [1, 4, 9, 16, 25]

# Function to plot
plt.plot(x, y1, label='Numbers')
plt.plot(x, y2, label='Square of numbers')

# Function add a legend
plt.legend()

# function to show the plot
plt.show()
