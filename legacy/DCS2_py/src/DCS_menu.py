from Tkinter import *

class DCS_menu(Menu):
    
    def __init__(self, parent, event_handler):
        # create a menu
        Menu.__init__(self, parent)
        
        
        filemenu = Menu(self)
        self.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open...", command=event_handler.file_open)
        filemenu.add_command(label="Save as", command=event_handler.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.callback)
        
        helpmenu = Menu(self)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.callback)
        
    def callback(self):
        print "called the callback!"
        

        