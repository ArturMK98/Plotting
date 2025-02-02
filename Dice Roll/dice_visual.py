import plotly.express as px
from die import Die

# Create a D6
sides = 6
die_1 = Die(sides)
die_2 = Die(sides)

# Make some random rolls and store results in a list
num_of_rolls = 10000
results = []
for roll_num in range(num_of_rolls):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = f"Results of Rolling Two D{sides} {num_of_rolls} Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()

print(frequencies)