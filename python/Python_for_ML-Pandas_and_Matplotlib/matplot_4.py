import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Customizing marker styles in scatter plots
plt.scatter(x, y, marker='x', color='red', s=100)
plt.show()

# Customizing line styles and width in line plots
plt.plot(x, y, linestyle='--', linewidth=3, color='blue')
plt.show()

# Adding markers to line plots
plt.plot(x, y, marker='o', markersize=8, markerfacecolor='red',
         markeredgecolor='black', color='blue')
plt.show()
