from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/mullingar_weather_december_2024.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract temperature data
highs = []
lows = []
for row in reader:
    high = float(row[2])
    low = float(row[3])
    highs.append(high)
    lows.append(low)


# Plot high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(range(1, len(highs) +1), highs, color='red', label="Highs")
ax.plot(range(1, len(lows) + 1), lows, color='blue', label="Lows") 

# Format plot
ax.set_title("Daily High Temperatures, December 2024", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(labelsize=16)

ax.legend()

plt.show()