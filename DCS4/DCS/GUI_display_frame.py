"""
Created on June 28, 2011

@author: sbobovyc
"""
import Tkinter

class GUI_display_frame(Tkinter.Frame):
    
    def __init__(self, parent, controller):
        # register with controller
        self.name = "display_frame"
        self.controller = controller
        self.controller.register(self, self.name)
        
        # create a scrollable canvas
        Tkinter.Frame.__init__(self, parent, bd=2, relief=Tkinter.FLAT, background="grey")
                 
        self.xscrollbar = Tkinter.Scrollbar(self, orient=Tkinter.HORIZONTAL)      
        self.xscrollbar.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)  
        
        self.yscrollbar = Tkinter.Scrollbar(self)
        self.yscrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        
        self.canvas = Tkinter.Canvas(self, background="grey", bd=0, height=0, width=0,
                        xscrollcommand=self.xscrollbar.set,
                        yscrollcommand=self.yscrollbar.set)
        self.canvas.pack(side=Tkinter.LEFT, expand=Tkinter.TRUE, fill=Tkinter.BOTH)
        
        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)      
        


        
