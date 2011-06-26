import PIL
import DCS_utils

class Layer:
    def __init__(self, _width, _height, _octave_count, _frequency, _persistence, _seed, _threshold, _z):
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
        
         
if __name__ == '__main__':
    layer = Layer(800,800, 2, 0.2, 0.2, 200, 0.1, 2.0)       
    layer.generate_layer_mask()  
    