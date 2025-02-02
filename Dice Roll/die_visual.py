import plotly.express as px
from die import Die

# Create a D6
sides = 6
die = Die(sides)

# Make some random rolls and store results in a list
num_of_rolls = 1000
results = []
for roll_num in range(num_of_rolls):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
possible_results = range(1, die.num_sides+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = f"Results of Rolling One D{sides} {num_of_rolls} Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.show()

print(frequencies)