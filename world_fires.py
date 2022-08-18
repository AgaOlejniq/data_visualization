import csv 
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


def get_fire_data(filename, lons, lats, brights, dates, hover_texts):

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column in enumerate(header_row):
            print(index, column)

        date_index = header_row.index('acq_date')
        lat_index = header_row.index('latitude')
        lon_index = header_row.index('longitude')
        brightness_index = header_row.index('brightness')

        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')
            lat = (row[lat_index])
            lon = (row[lon_index])
            brightness = float(row[brightness_index])
            label = f"{date} - {brightness}"

            lats.append(lat)
            lons.append(lon)
            brights.append(brightness)
            hover_texts.append(label)
            dates.append(date)

filename = r'python_crash_course\part_2\data_visualization\excersises\data\MODIS_C6_1_Global_24h.csv'
lons, lats, brights, dates, hover_texts = [], [], [], [], []
get_fire_data(filename, lons, lats, brights, dates, hover_texts)

data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [brightness/25 for brightness in brights],
        'color' : brights,
        'colorscale' : 'Hot',
        'colorbar' : {'title' : 'Brightness'},
    },
}]

'''data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brights],
        'color': brights,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]'''

my_layout = Layout(title='Global Fires')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_fires.html')