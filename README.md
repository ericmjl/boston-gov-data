# boston-gov-data

Visually explore data from Boston's [open data](http://data.boston.gov/).

MIT Licensed code.

<!-- Launch on Binder: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/ericmjl/boston-gov-data) -->

# requirements

Check the [`requirements.txt`](./requirements.txt) file to see what packages you need to install.

# running the code

You'll first have to clone or download the repository.

To clone:

```bash
$ git clone https://github.com/ericmjl/boston-gov-data.git
```

To download, click on the green button in the top-right corner above the file list.

## geospatial data

To view the geospatial data, run:

```bash
$ bokeh serve --show boston_geo.py
```

## timeseries data

To view the timeseries data, run:

```bash
$ bokeh serve --show boston911.py  # will load the 911 calls data.
```

or

```bash
$ bokeh serve --show boston_ei_explorer.py  # will load the economic indicators data.
```

# TODOs

1. [ ] Make Jupyter widgets work on Binder.
1. [ ] Deploy Bokeh apps on a server somewhere.
