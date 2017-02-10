import pandas as pd

from bokeh.layouts import row
from bokeh.models.widgets import CheckboxGroup, Button
from bokeh.charts import Line
from bokeh.plotting import curdoc

df = pd.read_csv('https://data.boston.gov/dataset/c8b8ef8c-dd31-4e4e-bf19-af7e4e0d7f36/resource/29e74884-a777-4242-9fcc-c30aaaf3fb10/download/economic-indicators.csv',
                 parse_dates=[['Year', 'Month']])
df.drop(24, inplace=True)
print(df.columns)
output_cols = [i for i in df.columns][1:]


def make_plot():
    sel_cols = [output_cols[i] for i in chkbx.active]
    p = Line(data=df, x='Year_Month', y=sel_cols, plot_height=400)
    return p


def update(attr, old, new):
    r1.children[1] = make_plot()


def clear():
    chkbx.active = [0]


def sel_all():
    chkbx.active = [i for i in range(len(df.columns)-1)]

chkbx = CheckboxGroup(labels=output_cols, active=[0])
chkbx.on_change('active', update)

clr_button = Button(label='Clear Selections', button_type='success')
clr_button.on_click(clear)

all_button = Button(label='Select All', button_type='success')
all_button.on_click(sel_all)


r1 = row(chkbx, make_plot())
# r1 = row(chkbx)

curdoc().add_root(r1)
curdoc().title = "Qualitative Variable Explorer"
