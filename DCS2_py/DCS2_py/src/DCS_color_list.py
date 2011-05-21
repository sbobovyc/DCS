'''
Created on Jan 12, 2011

@author: sbobovyc
'''

'''
Created on Jan 12, 2011

@author: sbobovyc
'''
import Tkinter

class DCS_color_list(Tkinter.Frame):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent, background="green", bd=2, height=5) 
        self.parent = parent
        
        self.initialize()
        
    def initialize(self):        
        self.yscrollbar = Tkinter.Scrollbar(self)
        self.yscrollbar.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S, rowspan=1)
        
        self.canvas = Tkinter.Canvas(self, bd=0, width=20, height=50, yscrollcommand=self.yscrollbar.set)

        self.canvas.grid(row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.yscrollbar.config(command=self.canvas.yview)
        
    def create_color_list(self):
        self.canvas.delete(Tkinter.ALL)
        