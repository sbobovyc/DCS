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

import Tkinter
import ImageTk
from utils import Utils

class GUI_thumbnail(Tkinter.Canvas):
    
    def __init__(self, parent, controller):
        self.name = "thumbnail"
        self.image = None
        self.controller = controller
        self.controller.register(self, self.name)        
        self.width = 128
        self.height = 128
        Tkinter.Canvas.__init__(self, parent, width=self.width, height=self.height, background="grey", bd=0)                            
        self.pack()
        
    
    def display_thumbnail(self, image_path):
        PIL_image = Utils.source_image_thumbnail(image_path, (self.width, self.height))        
        imagetk = ImageTk.PhotoImage(PIL_image)
        self.image = imagetk
        self.create_image(64,64,image=self.image)
