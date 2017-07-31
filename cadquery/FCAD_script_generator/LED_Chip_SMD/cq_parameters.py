# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

from collections import namedtuple

destination_dir="/Resistors_SMD"

### Parametric Values
##
Params = namedtuple("Params", [
    'L',   # package length
    'W',   # package width
    'T',   # package height

    'pb',   # pin band
    'pt',   # pin thickness
    'ph',    # pin height

    'pintype',   # can be 'concave' or 'convex'
    'ef',    # fillet of edges
    'modelName', # modelName
    'rotation' # rotation if required
])

all_params_res = {
    "0402_h040" : Params(
        L = 1.07,  # package length
        W = 0.55,  # package width
        T = 0.40,  # package height

        pb = 0.32,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.40,  # pin height

        pintype = 'concave',
        ef = 0.02, # fillet of edges
        modelName = 'r_0402_h040',  # Model Name
        rotation = 0   # rotation
    ),
}   

kicad_naming_params_res = {
    "0402_h040" : Params(
        L = 1.07,  # package length
        W = 0.55,  # package width
        T = 0.40,  # package height

        pb = 0.32,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.40,  # pin height

        pintype = 'concave',
        ef = 0.02, # fillet of edges
        modelName = 'r_0402_h040',  # Model Name
        rotation = 0   # rotation
    ),
    "0603_LED_GREEN" : Params(
        L = 1.6,  # package length
        W = 0.77,  # package width
        T = 0.8,  # package height

        pb = 0.25,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.28,  # pin height

        pintype = 'convex',
        ef = 0.02, # fillet of edges
        modelName = 'lala',  # Model Name
        rotation = 0   # rotation
    ),
}   
