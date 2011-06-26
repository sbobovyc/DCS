from Tkinter import *

class GUI_menubar(Menu):
    
    def __init__(self, parent):
        # create a menu
        Menu.__init__(self, parent)
        
        
        filemenu = Menu(self)
        self.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=self.callback())
        filemenu.add_command(label="Open Project", command=self.callback())
        filemenu.add_command(label="Open ...", command=self.callback())
        filemenu.add_command(label="Save", command=self.callback())
        filemenu.add_command(label="Save as", command=self.callback())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.callback)
        
        helpmenu = Menu(self)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.callback)
        
    def callback(self):
        print "called the callback!"
        