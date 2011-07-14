"""
Created on June 28, 2011

@author: sbobovyc
"""
import Tkinter
import tkFileDialog
import os

class GUI_menubar(Tkinter.Menu):
    
    def __init__(self, parent, controller):
        self.parent = parent
        self.name = "menubar"
        self.controller = controller
        self.controller.register(self, self.name)
        # file types
        self.file_types = [('all files', '.*'), ('', '.png'), ('', '.pgm'), ('', '.jpeg'), ('', '.bmp')]
        
        # create a menu
        Tkinter.Menu.__init__(self, parent)
                
        filemenu = Tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=filemenu)
#        filemenu.add_command(label="New Project", command=self.callback())
#        filemenu.add_command(label="Open Project", command=self.callback())
        filemenu.add_command(label="Open ...", command=self.file_open)
#        filemenu.add_command(label="Save", command=self.callback())
        filemenu.add_command(label="Save as", command=self.file_save)
        filemenu.add_command(label="Save Layers", command=self.file_save_layer)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_callback)
        
        helpmenu = Tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.callback)
        
    def callback(self):
        print "called the callback!"
    
    def file_open(self):                
        source_image_path = tkFileDialog.askopenfilename()
        self.controller.open_image(source_image_path) 
    
    def file_save(self):
        output_image_path = tkFileDialog.asksaveasfilename(filetypes=self.file_types)
        self.controller.save_image(output_image_path)
        
    def file_save_layer(self):
        output_path = tkFileDialog.asksaveasfilename(filetypes=self.file_types)
        basename, extension = os.path.splitext(output_path)
        self.controller.save_layers(basename, extension)
         
    def exit_callback(self):
        self.parent.quit()
        