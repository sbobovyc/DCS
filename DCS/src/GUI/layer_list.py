"""
Created on June 28, 2011

@author: sbobovyc
"""
import Tkinter

class GUI_layer_list(Tkinter.Frame):
    
    def __init__(self, parent, controller):
        # register with controller
        self.controller = controller
        self.controller.register(self, "layer_list")
                
        self.text = "Layer:"
        self.width = 3
        self.height = 5
        self.layer_list = []
        self.currently_selected_layer = None 
        
        # initialize the frame
        Tkinter.Frame.__init__(self, parent, width=20, background="gray")
        self.pack(fill=Tkinter.X)
        
        # label
        self.label = Tkinter.Label(self, text=self.text, bg="grey", relief="sunken")
        self.label.pack(anchor=Tkinter.NW, side=Tkinter.LEFT, expand=Tkinter.TRUE, fill=Tkinter.X)                
        
        self.current_color = Tkinter.Canvas(self, width=50, height=50)
        self.current_color.pack(anchor=Tkinter.N, side=Tkinter.LEFT, expand=Tkinter.TRUE, fill=Tkinter.Y)
        
        self.layers = Tkinter.Listbox(self, width=self.width, height=self.height)
        self.layers.bind("<Double-Button-1>", self.call_back)
        self.layers.pack(side=Tkinter.LEFT)
          
        self.scrollbar = Tkinter.Scrollbar(self)
        self.scrollbar.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
        
        # attach listbox to scrollbar
        self.layers.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.layers.yview)
        
        # start polling the list
        self.poll() 
        
        
    def insert_layer(self, layer):        
        self.layers.insert(Tkinter.END, layer.id)
        
    def call_back(self, event):
        print "list"
        
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
            print "selection is", selection
 
    
    