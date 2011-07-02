"""
Created on June 22, 2011

@author: sbobovyc
"""
import PIL

class Base_Layer(object):    
    def __init__(self, _width=0, _height=0, color = (0,0,0,0)):
        self.id = "base"
        self.width = _width
        self.height = _height
        self.octave_count = "N/A"
        self.frequency = "N/A"
        self.persistence = "N/A" 
        self.seed = "N/A"
        self.threshold = "N/A"
        self.z = "N/A"
        self.mask = None
        self.color = color
        self.color_weight = "N/A"
        self.image = None

    def generate_layer_mask(self):    
        pass                
    
    def draw_layer(self):
        self.image = PIL.Image.new("RGBA", (self.width, self.height), self.color)        
        
    