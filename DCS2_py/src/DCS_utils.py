'''
Created on Dec 24, 2010

@author: sbobovyc
'''

from PIL import Image, ImageTk

import tkMessageBox
import random

class Cammo_blob():        
    def __init__(self, color, level, image, canvas_width, canvas_height, x_coord=0, y_coord=0, width = 5, height=5, max_level=4):
        
        self.width = width
        self.height = height
        self.distribution = [0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9]
        self.regression = [1.0/max_level, 1.0/max_level, 1.0/max_level, 1.0/max_level, 1.0/max_level, 1.0/max_level, 1.0/max_level, 1.0/max_level]
        self.max_level = max_level

        #print "max level ", max_level
        self.level = level
        self.draw_image = image
        self.color = color
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.x_coord = x_coord
        self.y_coord = y_coord
        
        self.draw(self.canvas_width, self.canvas_height, self.x_coord, self.y_coord)
        
    def draw(self, canvas_width, canvas_height, x_coord=0, y_coord=0):
    
        if(self.level == 0):
            self.x_coord = random.randrange(0, canvas_width)
            self.y_coord = random.randrange(0, canvas_height)
            #self.draw_image.rectangle(((self.x_coord, self.y_coord),(self.x_coord+self.width, self.y_coord+self.height)), fill=self.color)
            self.draw_image.rectangle(((self.x_coord, self.y_coord),(self.x_coord+self.width, self.y_coord+self.height)), fill=self.color)
            if random.random() < self.distribution[0]:
                upper_left_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord-self.width, self.y_coord-self.height, max_level=self.max_level)
            if random.random() < self.distribution[1]:
                upper_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord, self.y_coord-self.height, max_level=self.max_level)
            if random.random() < self.distribution[2]:
                upper_right_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord+self.width, self.y_coord-self.height, max_level=self.max_level)
            if random.random() < self.distribution[3]:
                left_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord-self.width, self.y_coord, max_level=self.max_level)
            if random.random() < self.distribution[4]:
                right_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord+self.width, self.y_coord, max_level=self.max_level)
            if random.random() < self.distribution[5]:
                bottom_left_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord-self.width, self.y_coord+self.height, max_level=self.max_level)
            if random.random() < self.distribution[6]:
                bottom_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord, self.y_coord+self.height, max_level=self.max_level)
            if random.random() < self.distribution[7]:
                bottom_right_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord+self.width, self.y_coord+self.height, max_level=self.max_level)
            
            
        elif(self.level < self.max_level):
            for x in range(0, len(self.distribution)):
                self.distribution[x] = self.distribution[x] - self.regression[x]*self.level
            self.x_coord = x_coord
            self.y_coord = y_coord
            
            self.draw_image.rectangle(((self.x_coord, self.y_coord),(self.x_coord+self.width, self.y_coord+self.height)), fill=self.color)
            #print self.distribution[0]
            if random.random() < self.distribution[0]:
                upper_left_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord-self.width, self.y_coord-self.height, max_level=self.max_level)
                #print "upper_left ",self.level
            if random.random() < self.distribution[1]:
                upper_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord, self.y_coord-self.height, max_level=self.max_level)
                #print "upper ",self.level
            if random.random() < self.distribution[2]:
                upper_right_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord+self.width, self.y_coord-self.height, max_level=self.max_level)
                #print "upper_right ",self.level
            if random.random() < self.distribution[3]:
                left_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord-self.width, self.y_coord, max_level=self.max_level)
                #print "left ",self.level
            if random.random() < self.distribution[4]:
                right_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord+self.width, self.y_coord, max_level=self.max_level)
                #print "right ",self.level
            if random.random() < self.distribution[5]:
                bottom_left_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord-self.width, self.y_coord+self.height, max_level=self.max_level)
                #print "bottom_left ",self.level
            if random.random() < self.distribution[6]:
                bottom_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord, self.y_coord+self.height, max_level=self.max_level)
                #print "bottom ",self.level
            if random.random() < self.distribution[7]:
                bottom_right_cammo = Cammo_blob(self.color,self.level+1, self.draw_image, self.canvas_height, self.canvas_width, self.x_coord+self.width, self.y_coord+self.height, max_level=self.max_level)
                #print "bottom_right ",self.level
        else:
            pass
        
    def set_distribution_regression(self, distribution, regression):
        self.distribution = distribution
        self.regression = regression
        self.draw_image
        self.draw(self.canvas_width, self.canvas_height, self.x_coord, self.y_coord)
        
def histogram_image(image):
    #read image
    try:
        src_image = Image.open(image)
    except:
        tkMessageBox.showerror(
                                 "Open file",
                                 "Cannot open this file\n(%s)" % image
                                 )
        return None, -1
    
    print src_image.format, src_image.size, src_image.mode
    #put image pixels in a list
    pixel_list = list(src_image.getdata())
    
    #histogram the pixels
    histogram = {}
    for x in pixel_list:
        if x in histogram:
            histogram[x] += 1
        else:
            histogram[x] = 1
    
    #sort the histogram
    keys = histogram.keys()
    keys.sort()
    sorted_histogram = []
    for x in keys:
        sorted_histogram.append((x, histogram.get(x)))
        
    return sorted_histogram, 0

def calc_colors(histogram, numcolors):
    bin_size = len(histogram) / numcolors
    
    colors = []
    temp = (0,0,0)
    counter = 0
    
    
    # 1. Figure out bin sizes
    # 2. Partition histogram according to those bin sizes
    # 3. Do a weighted average on each bin
    
    #divide the histogram into almost equal bins
    bin_list = []
    for x in range(0, numcolors):
        if x != numcolors-1:
            bin_list.append(bin_size)
        else:
            bin_list.append(len(histogram) - bin_size*x)
    # if bin sizes are not equal, the first bin will be the largest bin 
    bin_list.reverse()    
    
    
    partitioned_histogram = []
    
    # partition histogram according to bin sizes
    counter2 = 0
    for each in bin_list:
        partitioned_histogram.append(histogram[counter2:counter2+each])
        counter2 = counter2 + each
    
    # weighted average on each bin
    for each in partitioned_histogram:
        for x in range(0, len(each)+1):
            if x % len(each) == 0 and x != 0:
                # take a weighted average
                temp = (temp[0] / counter, temp[1] / counter, temp[2] / counter)
                colors.append(temp)
                temp = (0,0,0)
                counter = 0                
            else:
                temp = (temp[0] + each[x][0][0] * each[x][1], temp[1] + each[x][0][1] * each[x][1], temp[2] + each[x][0][2] * each[x][1]) 
                counter = counter + each[x][1]
        
    return colors

def source_image_thumbnail(src_image_path):
    #create thumbnail using PIL
    size = 128, 128
    im = Image.open(src_image_path)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save("thumbnail", "JPEG")

    imagetk = ImageTk.PhotoImage(im)
    return imagetk
    
