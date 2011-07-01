"""
Created on Dec 24, 2010

@author: sbobovyc
"""
import Tkinter
from Tix import Tk
from Tkconstants import ANCHOR

import DCS_utils
from DCS_menu import DCS_menu
from DCS_gui_events import DCS_gui_events
from DCS_spin_label import DCS_spin_label
from DCS_color_list import DCS_color_list

class DCS_gui(Tkinter.Tk):
    '''
    classdocs
    '''
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent        
        self.width = 800;
        self.height = 600;
        self.number_of_colors = 4;
        self.max_level = 3;
        self.initialize()
        
    def initialize(self):
        # make it cover the entire screen
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        
        #attach event handler
        self.event_handler = DCS_gui_events(self)

        #building gui components
        #create menu
        self.menu = DCS_menu(self, self.event_handler)
        self.config(menu=self.menu)
        
        self.frame1 = Tkinter.Frame(self, bd=2, relief=Tkinter.FLAT, background="red")        
        self.frame1.grid_rowconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(0, weight=1)
        
        self.xscrollbar = Tkinter.Scrollbar(self.frame1, orient=Tkinter.HORIZONTAL)
        self.xscrollbar.grid(row=1, column=0, sticky=Tkinter.E+Tkinter.W)
        
        self.yscrollbar = Tkinter.Scrollbar(self.frame1)
        self.yscrollbar.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S, rowspan=1)
        
        self.canvas = Tkinter.Canvas(self.frame1, background="grey", bd=0, height=0, width=0,
                        xscrollcommand=self.xscrollbar.set,
                        yscrollcommand=self.yscrollbar.set)
        
        """
        self.canvas = Tkinter.Canvas(self.frame1, bd=0, scrollregion=(0, 0, 1000, 1000),
                xscrollcommand=self.xscrollbar.set,
                yscrollcommand=self.yscrollbar.set)
        """
        self.canvas.grid(row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        
        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)
        #self.xscrollbar.set(1.0,0.0)
        #self.yscrollbar.set(1.0,1.0)
        
        self.frame2 = Tkinter.Frame(self.frame1, bd=2, relief=Tkinter.FLAT, background="blue")
        self.frame2.grid_rowconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(1, weight=1)
        self.frame2.grid(row=0, column=2, sticky=Tkinter.N)
        
        
        self.canvas2 = Tkinter.Canvas(self.frame2, width=128, height=128, background="grey", bd=0)
        self.canvas2.grid_columnconfigure(0, weight=1)
        self.canvas2.grid_rowconfigure(0, weight=1)
        self.canvas2.grid(row=0,column=0)
        
        
        self.button_generate = Tkinter.Button(self.frame2, text="Generate", bd=3, command=self.event_handler.generate)
        self.button_generate.grid_columnconfigure(1, weight=1)
        self.button_generate.grid_rowconfigure(0, weight=1)
        self.button_generate.grid(row=1,column=0)
        
        self.num_colors = DCS_spin_label(self.frame2, text="Number of colors", from_=1, to=99, command=self.event_handler.num_colors, default=self.number_of_colors)
        self.num_colors.grid(row=2, column=0)
        
        self.levels = DCS_spin_label(self.frame2, text="Max level", from_=1, to=5, default=self.max_level, command=None)
        self.levels.grid(row=3, column=0)
        
        self.color_list = DCS_color_list(self.frame2)
        self.color_list.grid(row=4, column=0)
        
        self.width_label = DCS_spin_label(self.frame2, text="Width", from_=1, to=1600, default=self.width, command=None)
        self.width_label.grid(row=5, column=0)
        
        self.height_label = DCS_spin_label(self.frame2, text="Height", from_=1, to=1600, default=self.height, command=None)
        self.height_label.grid(row=6, column=0)
        
        self.frame1.pack(anchor=Tkinter.NW, expand=Tkinter.TRUE, fill=Tkinter.BOTH)
        #self.frame1.pack()
        
        
if __name__ == "__main__":
    app = DCS_gui(None)
    app.title('DCS')
    app.mainloop()
        
