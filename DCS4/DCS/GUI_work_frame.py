import Tkinter

from GUI_thumbnail import GUI_thumbnail
from GUI_spin_label import GUI_spin_label

class GUI_work_frame(Tkinter.Frame):
    
    def __init__(self, parent):
        
        #TODO move default initialization to a separate function
        self.width = 800
        self.height = 800
        self.num_colors = 3
        
        # initialize the frame
        Tkinter.Frame.__init__(self, parent, bd=2, relief=Tkinter.FLAT, background="grey")
                        
        # add widgets to frame
        self.thumbnail = GUI_thumbnail(self)
        self.button_generate = Tkinter.Button(self, text="Generate", bd=2, command=None)
        self.button_generate.pack()
        self.width_label = GUI_spin_label(self, text="Width", from_=1, to=1600, default=self.width, command=None)
        self.width_label.pack(anchor=Tkinter.E)                
        self.height_label = GUI_spin_label(self, text="Height", from_=1, to=1600, default=self.height, command=None)
        self.height_label.pack(anchor=Tkinter.E)
        self.num_colors_label = GUI_spin_label(self, text="Number of Colors", from_=1, to=16, default=self.num_colors, command=None)
        self.num_colors_label.pack(anchor=Tkinter.E)

        
