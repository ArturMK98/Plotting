from pathlib import Path
import plotly.express as px
import json

# Import data as a string and convert to a Python object
path = Path('eq_data/1.0_month.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset
all_eq_dicts =  all_eq_data['features']
print(len(all_eq_dicts))

magnitudes, longitudes, latitudes = [], [], []
for eq_dict in all_eq_dicts:
    magnitude = eq_dict['properties']['mag']
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)

print(magnitudes[:10])
print(longitudes[:10])
print(latitudes[:10])

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=latitudes, lon=longitudes, title=title)
fig.show()