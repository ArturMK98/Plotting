from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/mullingar_weather_2024_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract temperature data
dates, rain = [], []
for row in reader:
    date = datetime.strptime(str(row[0]), '%d-%b-%Y')
    try:
        rainfall = float(row[1])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        rain.append(rainfall)


# Plot high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rain, color='purple', label="Rainfall", alpha=0.5)

# Format plot
ax.set_title("Daily Rainfall, Mullingar 2024", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rain (mm)", fontsize=16)
ax.tick_params(labelsize=16)

ax.legend()

plt.show()