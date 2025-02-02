import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

#plt.style.use('classic')
fig, ax = plt.subplots()

#ax.plot(x_values, y_values, color='red', linewidth=2)
scatter = ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of thick labels
ax.tick_params(labelsize=14)

ax.axis([0, 5100, 0, 130_000_000_000])
ax.ticklabel_format(style='sci')

# Add a color bar to show the gradient
# cbar = plt.colorbar(scatter)
# cbar.set_label('Cube of Value', fontsize=14)

#plt.show()
plt.savefig('cubes_plot.png', bbox_inches='tight')