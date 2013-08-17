#!/usr/bin/env python
import random
import gtk
from gimpfu import *

def python_colorize_camo(image, drawable, palette):
    image.disable_undo()
    num_colors, colors = pdb.gimp_palette_get_colors(palette)
    num_layers, layer_ids = pdb.gimp_image_get_layers(image)

    if num_colors != num_layers:
        pdb.gimp_message("Number of colors in palette does not match number of layers!")
        gtk.main_quit()

    for color,layer in zip(colors, image.layers):
        #pdb.gimp_message(color)
        #pdb.gimp_message(layer)
        pdb.plug_in_colortoalpha(image, layer, (255, 255, 255))
        pdb.plug_in_exchange(image, layer, 0, 0, 0, color[0], color[1], color[2], 0,0,0)        

    image.enable_undo()

    # now modify camo layers with standard gimp filters, like despecle

register(
    "python_fu_colorize_camo",
    "DCS",
    "DCS",
    "Stan",
    "Stan",
    "2013",
    "<Image>/Filters/DCS/Colorize camo...",
    "RGB*",
    [     
        (PF_PALETTE, "palette", "Palette:", 0)
    ],
    [],
    python_colorize_camo)

main()
