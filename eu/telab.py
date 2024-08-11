import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plotting
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Example Line')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()
