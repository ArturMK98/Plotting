from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/mullingar_weather_2024_full_missing_data.csv')
path = Path('weather_data/mullingar_weather_2024_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract temperature data
dates, highs, lows = [], [], []
for row in reader:
    date = datetime.strptime(str(row[0]), '%d-%b-%Y')
    try:
        high = float(row[2])
        low = float(row[3])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)


# Plot high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', label="Highs", alpha=0.5)
ax.plot(dates, lows, color='blue', label="Lows", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title("Daily High and Low Temperatures, Mullingar 2024", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(labelsize=16)

ax.legend()

plt.show()