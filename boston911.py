import pandas as pd

from bokeh.layouts import row
from bokeh.models.widgets import CheckboxGroup, Button
from bokeh.charts import Line
from bokeh.plotting import curdoc

df = pd.read_csv('https://data.boston.gov/dataset/17129fad-fff9-4eac-ad74-51fb\
                    4bf63c22/resource/2459542e-7026-48e2-9128-ca29dd3bebf8/\
                    download/911-daily-dispatch-count-by-agency.csv',
                 parse_dates=['Date'])
print(df.columns)
output_cols = [i for i in df.columns][4:]


def make_plot():
    sel_cols = [output_cols[i] for i in chkbx.active]
    p = Line(data=df, x='Date', y=sel_cols, plot_height=400)
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

curdoc().add_root(r1)
curdoc().title = "Qualitative Variable Explorer"
