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
        
    