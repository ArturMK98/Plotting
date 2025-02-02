import matplotlib.pyplot as plt
from die import Die

# Create a D6
sides = 6
die_1 = Die(sides)
die_2 = Die(sides)

# Make some random rolls and store results in a list
num_of_rolls = 100000
results = [die_1.roll() + die_2.roll() for roll_num in range(num_of_rolls)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result+1)
frequencies = [results.count(value) for value in possible_results]

# Visualize the results
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
ax.bar(possible_results, frequencies, color='blue')
plt.xticks(range(min(possible_results), max(possible_results) + 1, 1))
for i, frequency in enumerate(frequencies):
    ax.text(possible_results[i], frequency + 1, str(frequency), ha='center', va='bottom')

# Further customize chart
#fig.update_layout(xaxis_dtick=1)

plt.show()

print(frequencies)