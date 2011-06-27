'''
Created on Jan 12, 2011

@author: sbobovyc
'''
import Tkinter
from Tix import Tk

class GUI_spin_label(Tkinter.Frame):
    '''
    classdocs
    '''

    def __init__(self, parent, text, from_, to, command, state=Tkinter.NORMAL, default=0):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent, width=20) 
        self.parent = parent
        self.text = text
        self.from_ = from_
        self.to = to
        self.default = default
        self.state = state
        self.command = command
        self.pack(expand=Tkinter.TRUE, fill=Tkinter.X)
        self.initialize()
        
        
    def initialize(self):
        self.label = Tkinter.Label(self, text=self.text, bg="grey", relief="sunken")
        self.label.pack(side=Tkinter.LEFT, expand=Tkinter.TRUE, fill=Tkinter.X)
        self.spinbox = Tkinter.Spinbox(self, from_=self.from_, to=self.to, state=self.state, width=3, command=self.command)
        self.spinbox.delete(0,"end")
        self.spinbox.insert(0,self.default)
        self.spinbox.pack(side=Tkinter.RIGHT)
#        self.spinbox.grid_columnconfigure(0, weight=1)
#        self.spinbox.grid_rowconfigure(0, weight=1)
#        self.spinbox.grid(row=0,column=1)
        
    def get(self):
        return self.spinbox.get()
        
    
        
        
        