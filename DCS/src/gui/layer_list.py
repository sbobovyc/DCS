"""
Created on June 28, 2011

@author: sbobovyc
"""
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
    

class GUI_layer_list(tk.Frame):
    
    def __init__(self, parent, controller):
        # register with controller
        self.controller = controller
        self.controller.register(self, "layer_list")
                
        self.text = "Layer:"
        self.width = 4
        self.height = 5
        self.layer_list = []
        self.currently_selected_layer = None         
        
        # initialize the frame
        tk.Frame.__init__(self, parent, width=20, background="gray")
        self.pack(fill=tk.X)
        
        # label
        self.label = tk.Label(self, text=self.text, bg="grey", relief="sunken")
        self.label.pack(anchor=tk.NW, side=tk.LEFT, expand=tk.TRUE, fill=tk.X)                
        
        self.current_color = tk.Canvas(self, width=50, height=50)
        self.current_color.pack(anchor=tk.N, side=tk.LEFT, expand=tk.TRUE, fill=tk.Y)
        
        self.layers = tk.Listbox(self, width=self.width, height=self.height)
        self.layers.bind("<Double-Button-1>", self.edit)
        self.layers.pack(side=tk.LEFT)        
          
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        
        # attach listbox to scrollbar
        self.layers.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.layers.yview)
        
        # start polling the list
        self.poll() 
        
        
    def insert_layer(self, layer):        
        self.layers.insert(tk.END, layer.id)
        
    def remove_all_layers(self):
        self.layers.delete(0, tk.END)
        
    def edit(self, event):
        layer_id = self.get_currently_selected_layer()
        self.controller.set_layer_color(layer_id)
        
    def poll(self):        
        selected_layer = self.layers.curselection()
        if selected_layer != self.currently_selected_layer:
            self.list_has_changed(selected_layer)
            self.currently_selected_layer = selected_layer   
            
        self.after(250, self.poll)

    def get_currently_selected_layer(self):
        try:
            return self.currently_selected_layer[0]
        except:
            return 0
    
    def list_has_changed(self, selection):
        # a layer was selected, so signal the controller
        # check if an actual layer was selected
    
        if len(selection) != 1:
            pass
        else: 
            self.currently_selected_layer = selection[0]
            self.controller.select_layer(self.currently_selected_layer)   

 
    
    