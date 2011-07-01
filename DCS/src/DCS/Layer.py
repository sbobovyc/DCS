"""
Created on June 22, 2011

@author: sbobovyc
"""
import PIL
import Utils

class Layer(object):    
    def __init__(self, _width=0, _height=0, _octave_count=0, _frequency=0, _persistence=0, _seed=0, _threshold=0, _z=0, color = (0,0,0,0)):
        self.width = _width
        self.height = _height
        self.octave_count = _octave_count
        self.frequency = _frequency
        self.persistence = _persistence 
        self.seed = _seed
        self.threshold = _threshold
        self.z = _z
        self.mask = None
        self.color = color
        self.image = None

    def generate_layer_mask(self):        
         self.mask = Utils.draw_blobs(self.width, self.height, self.octave_count, self.frequency, self.persistence, self.seed, self.threshold, self.z)                
    
    def draw_layer(self):
        self.image = PIL.Image.new("RGBA", (self.width, self.height), (0,0,0,0))
        Utils.draw_pixels(self.mask, self.image, self.color)
        
if __name__ == "__main__":
    layer = Layer(800,800,2,0.004,0.04, 0, 0.2, 1.0, (50,50,50))
    layer.generate_layer_mask()
    layer.draw_layer()
    