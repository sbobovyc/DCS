'''
Created on Dec 24, 2010

@author: sbobovyc
'''
import Tkinter
import tkMessageBox
from functools import partial

from tkFileDialog import askopenfilename, asksaveasfile, asksaveasfilename
from PIL import Image, ImageTk, ImageDraw

import DCS_utils


class DCS_gui_events(object):
    '''
    classdocs
    '''
    parent_gui = None
    source_image_path = ""
    output_image_path = ""
    imagetk = None
    thumb = None
    num_colors = None
    current_image = None
    output_image_height = None
    output_image_width = None
    base_color = None
    colors = None
    file_types = [('all files', '.*'), ('', '.pgm'), ('', '.jpeg'), ('', '.bmp')]

    
    def __init__(self, parent):
        '''
        Constructor
        '''
        self.parent_gui = parent
        
    def file_open(self):
        self.source_image_path = askopenfilename() 
        print self.source_image_path          
        self.analyze_image()
        self.thumb = DCS_utils.source_image_thumbnail(self.source_image_path)
        self.parent_gui.canvas2.create_image(64,64,image=self.thumb)
        

    def file_save(self):
        self.output_image_path = asksaveasfilename(filetypes=self.file_types) 
        print self.output_image_path
        self.current_image.save (self.output_image_path)

    def analyze_image(self):
        hist, err = DCS_utils.histogram_image(self.source_image_path)
        #error check
        if err != 0:
            return
            
        self.colors = DCS_utils.calc_colors(hist,self.parent_gui.number_of_colors)
        print self.colors
        
        self.base_color = (0,0,0) 
        
        for each in self.colors[0:len(self.colors)-1]:
            self.base_color = (self.base_color[0] + each[0], self.base_color[1] + each[1], self.base_color[2] + each[2])
             
        self.base_color = (self.base_color[0] / len(self.colors)-1, self.base_color[1] / len(self.colors)-1, self.base_color[2] / len(self.colors)-1)
        
        print "base color", self.base_color
        
    def update_num_colors(self):
        self.num_colors = self.num_colors
        print self.num_colors 
        
    def generate(self):
                
        width = self.parent_gui.width
        height = self.parent_gui.height
    
        self.current_image = Image.new ( "RGB", (width,height), self.base_color )
        draw = ImageDraw.Draw ( self.current_image )
        
        try:
            for x in range(0, 500):
                blob = DCS_utils.Cammo_blob(self.colors[0], 0, draw, width, height, max_level=2)
                blob = DCS_utils.Cammo_blob(self.colors[1], 0, draw, width, height, max_level=2)
                blob = DCS_utils.Cammo_blob(self.colors[2], 0, draw, width, height, max_level=2)
        except:
            tkMessageBox.showerror(message="Input image file not specified")
            return

        self.imagetk = ImageTk.PhotoImage(self.current_image)
        self.parent_gui.canvas.create_image(0,0,image=self.imagetk)
        self.parent_gui.canvas.config(scrollregion=self.parent_gui.canvas.bbox(Tkinter.ALL))
