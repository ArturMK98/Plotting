from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/mullingar_weather_december_2024.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract temperature data
dates, highs = [], []
for row in reader:
    date = datetime.strptime(str(row[0]), '%d-%b-%Y')
    try:
        high = float(row[2])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        highs.append(high)


# Plot high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot
ax.set_title("Daily High Temperatures, December 2024", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(labelsize=16)

ax.legend()

plt.show()