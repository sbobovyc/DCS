"""
Created on June 22, 2011

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

import PIL
import Utils

class Layer(object):    
    def __init__(self, id, _width=0, _height=0, _octave_count=0, _frequency=0, _persistence=0, _seed=0, _threshold=0, _z=0, color = (0,0,0,0), color_weight = 1):
        self.id = id
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
        self.color_weight = color_weight
        self.image = None

    def generate_layer_mask(self):    
        self.mask = None    
        self.mask = Utils.draw_blobs(self.width, self.height, self.octave_count, self.frequency, self.persistence, self.seed, self.threshold, self.z)                
    
    def draw_layer(self):
        self.image = PIL.Image.new("RGBA", (self.width, self.height), (0,0,0,0))
        Utils.draw_pixels(self.mask, self.image, self.color)
        
    