"""
Created on June 28, 2011

@author: sbobovyc
"""
import Tkinter

from thumbnail import GUI_thumbnail
from spin_label import GUI_spin_label
from layer_list import GUI_layer_list
from DCS import Layer

class GUI_work_frame(Tkinter.Frame):
    
    def __init__(self, parent, controller):
        self.name = "work_frame"
        self.controller = controller
        self.controller.register(self, "work_frame")
        
        #TODO move default initialization to a separate function
        self.width = 400
        self.height = 400
        self.num_colors = 3
        self.selected_layer = Tkinter.ANCHOR
        self.default_octave_count = 2
        self.default_frequency = 0.04
        self.default_persistence = 0.02 
        self.default_seed = "rand"
        self.default_threshold = 0.2
        self.default_z = 1.0
        
        # initialize the frame
        Tkinter.Frame.__init__(self, parent, bd=2, relief=Tkinter.FLAT, background="grey")
                        
        # add widgets to frame
        
        #top of frame, mostly static
        self.thumbnail = GUI_thumbnail(self, self.controller)
        self.button_generate = Tkinter.Button(self, text="Generate", bd=2, command=self.controller.generate_layers)
        self.button_generate.pack()
        self.width_label = GUI_spin_label(self, text="Width:", from_=1, to=1600, increment=1.0, default=self.width, command=None)
        self.width_label.pack(anchor=Tkinter.E)                
        self.height_label = GUI_spin_label(self, text="Height:", from_=1, to=1600, increment=1.0, default=self.height, command=None)
        self.height_label.pack(anchor=Tkinter.E)
        self.num_colors_label = GUI_spin_label(self, text="Number of Colors", from_=1, to=16, increment=1.0, default=self.num_colors, command=None)
        self.num_colors_label.pack(anchor=Tkinter.E)
        
        #middle of frame
        self.layer_list = GUI_layer_list(self, self.controller)
        
        #bottom of rame, layer specific
        #TODO Lots of fixes here 
        self.octave_count = GUI_spin_label(self, text="Octaves:", from_=1, to=16, increment=1.0, default=self.default_octave_count, command=self.update_current_layer)
        self.frequency = GUI_spin_label(self, text="Frequency:", from_=0.0, to=1.0, increment=0.01, default=self.default_frequency, command=self.update_current_layer)
        self.persistence = GUI_spin_label(self, text="Persistence:", from_=0.0, to=1.0, increment=0.01, default=self.default_persistence, command=self.update_current_layer)
        self.seed = GUI_spin_label(self, text="Seed:", from_=0, to=10000, increment=1.0, default=self.default_seed, command=self.update_current_layer)
        self.threshold = GUI_spin_label(self, text="Threshold:", from_=-5.0, to=5.0, increment=0.01, default=self.default_threshold, command=self.update_current_layer)
        self.z = GUI_spin_label(self, text="Height:", from_=-5.0, to=5.0, increment=0.01, default=self.default_z, command=self.update_current_layer)        
        
    def get(self):
        return {"width":self.width_label.get(), "height":self.height_label.get(), 
                "num_colors":self.num_colors_label.get(), "octave_count":self.octave_count.get(),
                "frequency":self.frequency.get(), "persistence":self.persistence.get(),
                "seed":self.seed.get(), "threshold":self.threshold.get(), "z":self.z.get()}
        
    def clear_fields(self):
        self.octave_count.clear()
        self.frequency.clear()
        self.persistence.clear()
        self.seed.clear()
        self.threshold.clear()
        self.z.clear()
        
    def set_fields(self, layer):
        self.octave_count.set(layer.octave_count)
        self.frequency.set(layer.frequency)
        self.persistence.set(layer.persistence)
        self.seed.set(layer.seed)
        self.threshold.set(layer.threshold)
        self.z.set(layer.z)
        
    def update_current_layer(self):
        self.controller.update_layer(self.layer_list.get_currently_selected_layer())