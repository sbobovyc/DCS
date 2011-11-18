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

import ctypes
import os
import random
from PIL import Image

class ColorFilter(object):
    def __init__(self, id, color1, color2):
        self.id = id
        self.color_range = color1, color2   # pair of colors which are lists like [r,g,b]
    
    def get_color1(self):
        return self.color_range[0]
    
    def get_color2(self):
        return self.color_range[1]
    
    def getR1(self):
        return self.color_range[0][0]
    
    def getR2(self):
        return self.color_range[1][0]
    
    def getG1(self):
        return self.color_range[0][1]
    
    def getG2(self):
        return self.color_range[1][1]
    
    def getB1(self):
        return self.color_range[0][2]
    
    def getB2(self):
        return self.color_range[1][2]
    
    def in_range(self, color):
        if color[0] >= self.getR1() and color[0] <= self.getR2() and \
            color[1] >= self.getG1() and color[1] <= self.getG2() and \
            color[2] >= self.getB1() and color[2] <= self.getB2():
            return True
        else:
            return False
    
def isLinux():
    if os.sys.platform == "linux2":
        return True
    else:
        return False
def isWindows():
	if os.sys.platform == "win32":
		return True
	else:
		return False

def filter_pixel(color, color_filter_list):
    for color_range in color_filter_list:
        if color_range.in_range(color):
            return True
        else:
            return False
##
# @param image_list: list of PIL images
# @param width: width of output image, an integer
# @param height: height of output image, an integer
def combine_layers(image_list, width, height):
    final_image = Image.new("RGBA", (width, height), (0,0,0,0))
    
    for image in image_list:
        final_image.paste(image, None, image)
    return final_image

##
# @param ptr: ctypes int* array
# @param image: PIL image object 
# @param color: RGB color triple
def draw_pixels(ptr, image, color):
    width, height = image.size    
    
    pix = image.load()    
    for i in range(height):
        for j in range(width):
            if ptr[i][j] == 1:                
                pix[j, i] = color   # j,i instead of i,j since pixel object is indexed by x,y not row,column
    
##
# @param image_path: full path to the image 
# @return: list of image pixels
def get_image_pixels(image_path):
    #read image_path
    src_image = Image.open(image_path)    
    
    #put image_path pixels in a list
    pixel_list = list(src_image.getdata())
    return pixel_list
##
# @param image_path: full path to the image 
# @return: string describing the image format and dimensions
def get_image_info(image_path):
    #read image_path
    src_image = Image.open(image_path)        
    return "%s %s %s" % (src_image.format, src_image.size, src_image.mode)

##
# @param pixel_list: list of image pixels 
# @param filter_list: list of color_filter objects which define color ranges to be excluded from histogram
# @return: a sorted histogram of colors in the image and number of filtered pixels
def histogram_colors(pixel_list, color_filter_list=None):
    filtered_pixels = 0
    #histogram the pixels
    if color_filter_list == None or len(color_filter_list) == 0:
        histogram = {}
        for x in pixel_list:
            if x in histogram:
                histogram[x] += 1
            else:
                histogram[x] = 1
    else:
        print "Filtering"
        histogram = {}
        for x in pixel_list:
            if not filter_pixel(x, color_filter_list):
                if x in histogram:
                    histogram[x] += 1
                else:
                    histogram[x] = 1
            else:
                filtered_pixels += 1
    #sort the histogram
    keys = histogram.keys()
    keys.sort()
    sorted_histogram = []
    for x in keys:
        sorted_histogram.append((x, histogram.get(x)))
            
    return sorted_histogram, filtered_pixels

##
# @param histogram: a sorted histogram of colors in an image
# @param numcolors: the number of output colors desired
# @return: a list of colors and their weights
def calc_colors(histogram, numcolors):    
    # 1. Figure out bin sizes
    # 2. Partition histogram according to those bin sizes
    # 3. Do a weighted average on each bin
    
    # start 1
    bin_size = len(histogram) / numcolors
    # end 1
    
    # start 2
    #divide the histogram into almost equal bins    
    bin_list = []
    if (len(histogram)  % numcolors) == 0:
        for i in range(0, numcolors):
            bin_list.append( (i*bin_size, i*bin_size+bin_size-1) )
    else:
        bin_list.append( (0,bin_size) )
        for i in range(1, numcolors):
            bin_list.append( (i*bin_size+1, i*bin_size+bin_size) )    
    # end 2
    
    # start 3
    color_list = []
    
    for bin in bin_list:
        tmp_red = 0
        tmp_green = 0
        tmp_blue = 0
        tmp_weight = 0
        
        for i in range(bin[0], bin[1]):            
            weight = histogram[i][1]
            
            tmp_red += histogram[i][0][0] * weight
            tmp_green += histogram[i][0][1] * weight
            tmp_blue += histogram[i][0][2] * weight
            tmp_weight += histogram[i][1]            
        # @todo: Division by zero is possible. Need to fix this in the future.
        color_list.append( ((tmp_red/tmp_weight, tmp_green/tmp_weight, tmp_blue/tmp_weight), tmp_weight) )
    # end 3
        
    return color_list

##
# @param colors: list of colors
# @return base_color: a triplet, representing a weighted average of the input colors 
def calculate_base_color(colors):    
    red = 0
    blue = 0
    green = 0
    total_weight = 0
     
    for color in colors:    
        weight = color[1]
        red += color[0][0] * weight
        green += color[0][1] * weight
        blue += color[0][2] * weight
        total_weight += weight
    
    red /= total_weight;
    green /= total_weight;
    blue /= total_weight;

    return (red, green, blue)

##
# @param canvas_width: integer
# @param canvas_height: integer
# @param octave_count: integer
# @param frequency: double
# @param persistence: double
# @param seed: int  
# @param threshold: double
# @param z: double
def draw_blobs(canvas_width, canvas_height, octave_count, frequency, persistence, seed, threshold, z):

    path = os.path.dirname(os.path.realpath(__file__))    
    lib = None
    lib_path = None
    if isLinux():
        lib = "libutils.so"
        lib_path = os.path.join(path, "build", lib)
    if isWindows():        
        lib_path = "libutils.dll"
        if os.path.isfile(lib_path):
            pass
        else:
            lib = "libutils.dll"
            lib_path = os.path.join(path, "build", lib)                
        
    utils = ctypes.CDLL(lib_path)    
    
    canvas_width = ctypes.c_int(canvas_width) 
    canvas_height = ctypes.c_int(canvas_height) 
    octave_count = ctypes.c_int(octave_count)  
    frequency = ctypes.c_double(frequency)
    persistence = ctypes.c_double(persistence) 
    seed = ctypes.c_int(seed) 
    threshold = ctypes.c_double(threshold) 
    z = ctypes.c_double(z) 
        
    # create a multidimensional int array
    INT = ctypes.c_int
    PINT = ctypes.POINTER(INT)
    PPINT = ctypes.POINTER(PINT)
    
    # An array of ints can be passed to a function that takes int*.
    INTARR = INT * canvas_width.value
    # An array of int* can be passed to your function as int**.
    PINTARR = PINT * canvas_height.value
    
    # Declare int* array.
    ptr = PINTARR()
    for i in range(0, canvas_height.value):
        # fill out each pointer with an array of ints.
        ptr[i] = INTARR()
        for j in range(0, canvas_width.value):
            ptr[i][j] = 0
    
    utils.draw_blobs(canvas_width, canvas_height, octave_count, frequency, persistence, seed, threshold, z, ptr)
    return ptr

##
# @param image_path: full path to the image
# @param geometry: tuple that represents the geometry of the generated thumbnail  
# @return: thumbnail of the image as PIL image
def source_image_thumbnail(image_path, geometry):
    #create thumbnail using PIL    
    image = Image.open(image_path)
    image.thumbnail(geometry, Image.ANTIALIAS)    
    
    return image
    
if __name__ == '__main__':
#    image = os.path.join(os.getcwd(), "image.jpeg")
#    image = "/home/sbobovyc/DCS_github/DCS/DCS/images/image.jpeg"
    image = "C:\Users\sbobovyc\workspace\DCS\DCS\images\image.jpeg"
    numcolors = 3
    color_filter = ColorFilter(0, [100,0,0], [50,50,50])
    #hist, filtered_pixels = histogram_colors(get_image_pixels(image), None)
    hist, filtered_pixels = histogram_colors(get_image_pixels(image), [color_filter])
    colors = calc_colors(hist, numcolors)
    print colors 
    base_color = calculate_base_color(colors) 
    print base_color
    
    canvas_width = 800
    canvas_height = 800 
    octave_count = 2  
    frequency = 0.04
    persistence = 0.02     
    threshold = 0.2 
    z = 1.0
    
    mask_list = []
    image_list = []
    image_list.append(Image.new("RGBA", (canvas_width, canvas_height), base_color))
#    image_list[0].save("layer0.png")
    i = 1
    for each in colors:
        random.seed()
        seed = random.randrange(0,10000)
        mask = draw_blobs(canvas_width, canvas_height, octave_count, frequency, persistence, seed, threshold, z)
        mask_list.append(mask)
        out_image = Image.new("RGBA", (canvas_width, canvas_height), (0,0,0,0))  #completely transparent image        
        draw_pixels(mask, out_image, each[0])
        image_list.append(out_image)
#        out_image.save("layer%i.png" % i)
        i += 1
    
    final_image = combine_layers(image_list, canvas_width, canvas_height)    
    final_image.save("out.png")
