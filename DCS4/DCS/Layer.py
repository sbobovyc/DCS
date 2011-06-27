"""
Created on June 22, 2011

@author: sbobovyc
"""
import PIL
import DCS_utils

class Layer(object):    
    
    def __init__(self, _width=0, _height=0, _octave_count=0, _frequency=0, _persistence=0, _seed=0, _threshold=0, _z=0):
        self.width = _width
        self.height = _height
        self.octave_count = _octave_count
        self.frequency = _frequency
        self.persistence = _persistence 
        self.seed = _seed
        self.threshold = _threshold
        self.z = _z
        self.mask = None
        self.color = (0,0,0,0)
        self.image = None
    
    def generate_layer_mask(self):        
         mask = DCS_utils.draw_blobs(self.width, self.height, self.octave_count, self.frequency, self.persistence, self.seed, self.threshold, self.z)         
    
    def draw_layer(self):
        self.image = PIL.Image.new(Image.new("RGBA", (self.width, self.height), self.color))
        draw_pixels(self.mask, self.image, color)
        
         
    