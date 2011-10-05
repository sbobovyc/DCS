'''
Created on Oct 4, 2011

@author: sbobovyc
'''
"""   
    Copyright (C) 2011 Stanislav Bobovych

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

import tkColorChooser

class GUI_Color_Filter_Checkbox(tk.Checkbutton):
    '''
    classdocs
    '''

    def __init__(self, parent, controller):
        # register with controller
        self.name = "filter"
        self.controller = controller
        self.controller.register(self, self.name)
        
        self.text = "Filter"
        self.variable = tk.IntVar()
        tk.Checkbutton.__init__(self, master=parent, text=self.text, bg="grey", activebackground="grey", variable=self.variable, command=self.toggle) 
        self.pack()
        self.deselect()
        
    def toggle(self):
        if self.variable.get() == 1:
            color1 = tkColorChooser.askcolor(title="Choose first color")[0] 
            if color1 != None:
                color2 = tkColorChooser.askcolor(title="Choose second color")[0]
            else:
                self.deselect()
                return
            
            if color2 != None:
                self.controller.set_filter(color1, color2)
            else:
                self.deselect()
        else:
            print "Toggle"
            self.controller.unset_filter()

            
    def isFilter(self):
        if self.variable.get() == 1:
            return True
        else:
            return False