"""
Created on June 28, 2011

@author: sbobovyc
"""
import Tkinter

from GUI_thumbnail import GUI_thumbnail
from GUI_spin_label import GUI_spin_label
from GUI_layer_list import GUI_layer_list
from Layer import Layer

class GUI_work_frame(Tkinter.Frame):
    
    def __init__(self, parent):
        
        #TODO move default initialization to a separate function
        self.width = 800
        self.height = 800
        self.num_colors = 3
        self.selected_layer = Tkinter.ANCHOR
        self.default_octave_count = 3
        self.default_frequency = 0.2
        self.default_persistence = 0.2 
        self.default_seed = 0
        self.default_threshold = 0.2
        self.default_z = 1.0
        
        # initialize the frame
        Tkinter.Frame.__init__(self, parent, bd=2, relief=Tkinter.FLAT, background="grey")
                        
        # add widgets to frame
        self.thumbnail = GUI_thumbnail(self)
        self.button_generate = Tkinter.Button(self, text="Generate", bd=2, command=None)
        self.button_generate.pack()
        self.width_label = GUI_spin_label(self, text="Width:", from_=1, to=1600, default=self.width, command=None)
        self.width_label.pack(anchor=Tkinter.E)                
        self.height_label = GUI_spin_label(self, text="Height:", from_=1, to=1600, default=self.height, command=None)
        self.height_label.pack(anchor=Tkinter.E)
        self.num_colors_label = GUI_spin_label(self, text="Number of Colors", from_=1, to=16, default=self.num_colors, command=None)
        self.num_colors_label.pack(anchor=Tkinter.E)
        self.layer_list = GUI_layer_list(self)
        
        # layer specific
        #TODO Lots of fixes here 
        self.octave_count = GUI_spin_label(self, text="Octaves:", from_=1, to=16, default=self.default_octave_count, command=None)
        self.frequency = GUI_spin_label(self, text="Frequency:", from_=0.0, to=1.0, default=self.default_frequency, command=None)
        self.persistence = GUI_spin_label(self, text="Persistence:", from_=0.0, to=1.0, default=self.default_persistence, command=None)
        self.seed = GUI_spin_label(self, text="Persistence:", from_=0, to=10000, default=self.default_seed, command=None)
        self.threshold = GUI_spin_label(self, text="Threshold:", from_=5.0, to=5.0, default=self.default_threshold, command=None)
        self.z = GUI_spin_label(self, text="Height:", from_=-5.0, to=5.0, default=self.default_z, command=None)        
        self.color = (0,0,0,0)
        
