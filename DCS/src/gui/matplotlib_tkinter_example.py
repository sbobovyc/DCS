#!/usr/bin/env python
import numpy.numarray as na
import Tkinter as Tk
from matplotlib.colors import colorConverter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from pylab import *

colors = [(0,0,0,34), (0.5,0.5,0,56), (0.3,1,0.3,23) ]

fig = plt.figure()
ax = fig.add_subplot(111)

#for index, height, width, type in zip(indices, heights, widths, types):
#    if type == 'spam':
#        ax.bar(index, height, width, color='#263F6A')
#    elif type == 'rabbit':
#        ax.bar(index, height, width, color='#3F9AC9')
#    elif type == 'grail':
#        ax.bar(index, height, width, color='#76787a')

index = 0
for color in colors:
    ax.bar(index, color[3], width=1, color=(color[0],color[1],color[2]))
    index += 1


# turn off tick marks
ax.set_xticks([])
# turn off x axis labels
plt.setp(ax.get_xaxis().get_label().set_visible(False))

root = Tk.Tk()
root.wm_title("Embedding in TK")

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


Tk.mainloop()

#plt.show()
