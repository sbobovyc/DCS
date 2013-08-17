#!/usr/bin/env python
import random
import sys
from gimpfu import *

def python_generate_camo(image, drawable, palette, width, height, tilable, auto_threshold, detail, xsize, ysize):
    image.disable_undo()
    image = pdb.gimp_image_new(width, height, RGB)
    num_colors, colors = pdb.gimp_palette_get_colors(palette)
    random.seed()

    # for each color in palette
    # create new black layer
    # render clouds
    # threshold
    # replace black with color
    # replace white with transparency
    # generate camo palette
    i = 0    
    for color in colors:
        name = "color%i" % i
        #pdb.gimp_message(color)
        layer = pdb.gimp_layer_new(image, width, height, RGBA_IMAGE, name, 100, NORMAL_MODE)
        pdb.gimp_image_insert_layer(image, layer, None, -1)
        seed = random.randint(0, sys.maxint)
        pdb.plug_in_solid_noise(image, layer, tilable, FALSE, seed, detail, xsize, ysize)
        low_threshold = 125
        high_threshold = 255
        if auto_threshold:
            pdb.gimp_threshold(layer, low_threshold, high_threshold)
        i += 1

    display = pdb.gimp_display_new(image)
    image.enable_undo() 

register(
    "python_fu_generate_camo",
    "DCS",
    "DCS",
    "Stan",
    "Stan",
    "2013",
    "<Image>/Filters/DCS/Generate camo...",
    "INDEXED*",
    [     
        (PF_PALETTE, "palette", "Palette:", 0),
        (PF_SPINNER, "width", "Width:", 400, (1, 1000, 50)),
        (PF_SPINNER, "height", "Height:", 400, (1, 1000, 50)),
        (PF_TOGGLE, "tilable",   "Tilable:", 1),
        (PF_TOGGLE, "auto_threshold",   "Auto threshold:", 0),
        (PF_SPINNER, "detail", "Detail:", 4, (1, 10, 1)),
        (PF_SLIDER, "xsize", "Horizontal texture size:", 1, (0, 20, 0.1)),
        (PF_SLIDER, "ysize", "Vertical texture size:", 1, (0, 20, 0.1)),

    ],
    [],
    python_generate_camo)

main()
