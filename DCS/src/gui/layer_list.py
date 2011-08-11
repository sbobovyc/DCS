"""
Created on June 28, 2011

@author: sbobovyc
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
        # make sure only one element is selected
        selected_layer = self.layers.curselection()
        if selected_layer != self.currently_selected_layer:
            self.list_has_changed(selected_layer)
            self.currently_selected_layer = selected_layer          
        self.after(250, self.poll)

    def get_currently_selected_layer(self):
        return self.currently_selected_layer[0]
    
    def list_has_changed(self, selection):
        # a layer was selected, so signal the controller
        # check if an actual layer was selected
    
        if len(selection) != 1:
            pass
        else: 
            self.currently_selected_layer = selection[0]
            self.controller.select_layer(self.currently_selected_layer)            
 
    
    