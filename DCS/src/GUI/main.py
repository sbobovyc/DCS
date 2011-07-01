#/usr/bin/env python
"""
Created on June 28, 2011

@author: sbobovyc
"""
import os
import sys
DCS_path = os.path.abspath("..") 
sys.path.append(DCS_path) 
print sys.path

import Tkinter

from menubar import GUI_menubar
from work_frame import GUI_work_frame
from display_frame import GUI_display_frame
import Controller

class GUI_main(Tkinter.Tk):
    '''
    classdocs
    '''
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.name = "main"        
        
        # instantiate the controller, register with the controller
        self.controller = Controller.Controller()
        self.controller.register(self, self.name)
        self.initialize()
        
    def initialize(self):
        # make the main window cover the entire screen
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (self.w, self.h))
                
        #create menu
        self.menu = GUI_menubar(self, self.controller)
        self.config(menu=self.menu)
        
        
        #create frame structure
        self.big_frame = Tkinter.Frame(self, bd=2, relief=Tkinter.FLAT, background="grey")
        self.big_frame.pack(anchor=Tkinter.NW, expand=Tkinter.TRUE, fill=Tkinter.BOTH)
        
        self.work_frame = GUI_work_frame(self.big_frame, self.controller)
        self.work_frame.pack(side=Tkinter.RIGHT, anchor=Tkinter.N)
        
        self.display_frame = GUI_display_frame(self.big_frame, self.controller)
        self.display_frame.pack(side=Tkinter.LEFT, expand=Tkinter.TRUE, fill=Tkinter.BOTH)
                     
        
if __name__ == "__main__":
    app = GUI_main(None)
    app.title('DCS')
    app.mainloop()
