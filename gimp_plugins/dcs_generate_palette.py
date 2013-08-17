#!/usr/bin/env python
from gimpfu import *

def python_dcs(image, drawable, colors):
    image.disable_undo()         
    c  = image.layers
    #pdb.gimp_message(c)

    # convert image to indexed colors, limit to 3 colors, optimized palette
    # a better algo is change to HSV, median filter, then histogram
    #pdb.gimp_message('Generate palette')
    pdb.gimp_image_convert_indexed(image, NO_DITHER, MAKE_PALETTE, colors, False, False, False)

    image.enable_undo() 

register(
    "python_fu_dcs",
    "DCS",
    "DCS",
    "Stan",
    "Stan",
    "2013",
    "<Image>/Filters/DCS/_Generate palette...",
    "RGB*",
    [
        (PF_SPINNER, "colors", "Colors:", 3, (1, 10, 1)),        
    ],
    [],
    python_dcs)

main()
