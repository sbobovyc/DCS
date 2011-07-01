"""
Created on June 28, 2011

@author: sbobovyc
"""
import Tkinter
import ImageTk
import DCS_utils

class GUI_thumbnail(Tkinter.Canvas):
    
    def __init__(self, parent, controller):
        self.name = "thumbnail"
        self.image = None
        self.controller = controller
        self.controller.register(self, self.name)        
        self.width = 128
        self.height = 128
        Tkinter.Canvas.__init__(self, parent, width=self.width, height=self.height, background="grey", bd=0)                            
        self.pack()
        
    
    def display_thumbnail(self, image_path):
        PIL_image = DCS_utils.source_image_thumbnail(image_path, (self.width, self.height))        
        imagetk = ImageTk.PhotoImage(PIL_image)
        self.image = imagetk
        self.create_image(64,64,image=self.image)