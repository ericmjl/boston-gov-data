from pyproj import Proj, transform
from bokeh.models import (Range1d, Circle, ColumnDataSource)
from bokeh.plotting import figure, curdoc
from bokeh.tile_providers import STAMEN_TONER
from bokeh.layouts import row
from bokeh.models.widgets import RadioGroup

import pandas as pd

data_urls = {
    'Water Sprays': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/5409b7735d384798b2a360aa47c9b128_0.csv',
    'Parking': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/962da9bb739f440ba33e746661921244_9.csv',
    'Fire Boxes': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/3a0f4db1e63a4a98a456fdb71dc37a81_4.csv',
    'Fire Hydrants': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/1b0717d5b4654882ae36adc4a20fd64b_0.csv',
    'EV Chargers': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/465e00f9632145a1ad645a27d27069b4_2.csv',
    'Fire Depts': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/092857c15cbb49e8b214ca5e228317a1_2.csv',
    'Police Stations': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/e5a0066d38ac4e2abbc7918197a4f6af_6.csv',
    'WickedWiFi': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/4b803745fedd4e88861967d16a1e07fb_0.csv',
    'Trees': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/ce863d38db284efe83555caf8a832e2a_1.csv',
    'Snow Emergency Parking': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/53ebc23fcc654111b642f70e61c63852_0.csv',
    'Hubway Stations': 'http://bostonopendata-boston.opendata.arcgis.com/datasets/ee7474e2a0aa45cbbdfe0b747a5eb032_0.csv',
}


def make_plot():
    # Load data
    selected_source = sorted(data_urls)[select.active]
    data = pd.read_csv(data_urls[selected_source])

    # Convert EPSG code
    p1 = Proj(init='epsg:4326')  # this is the EPSG code of the original
    p2 = Proj(init='epsg:3857')  # this is the EPSG code of the tiles
    transformed_coords = [transform(p1, p2, x1, y1)
                          for x1, y1 in zip(data['X'], data['Y'])]
    data['X'], data['Y'] = (zip(*transformed_coords))

    # Convert to coordinates
    src = ColumnDataSource(data)

    # Set x-range and y-range of map
    x_range = Range1d(start=data['X'].min(), end=data['X'].max(),
                      bounds=None)
    y_range = Range1d(start=data['Y'].min(), end=data['Y'].max(),
                      bounds=None)

    # Plot figure
    p = figure(x_range=x_range, y_range=y_range)
    p.axis.visible = False
    circs = Circle(x='X', y='Y', size=10, line_color=None, fill_alpha=0.8,
                   fill_color="blue")
    p.add_glyph(src, circs)
    p.add_tile(STAMEN_TONER)

    return p


def update(attr, old, new):
    r1.children[1] = make_plot()

menu = [(k, k) for k in data_urls.keys()]
select = RadioGroup(active=0,
                    labels=sorted(data_urls.keys()))
select.on_change('active', update)

r1 = row(select, make_plot())

curdoc().add_root(r1)
curdoc().title = "Boston Geo Data Explorer"
