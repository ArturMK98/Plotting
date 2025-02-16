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

magnitudes, longitudes, latitudes, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict['properties']['mag'])
    longitudes.append(eq_dict['geometry']['coordinates'][0])
    latitudes.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=magnitudes, 
                    title=all_eq_data['metadata']['title'],
                    color=magnitudes, color_continuous_scale='Viridis',
                    labels={'color': 'Magnitude'},
                    projection='natural earth',
                    hover_name=eq_titles,
                    )
fig.show()