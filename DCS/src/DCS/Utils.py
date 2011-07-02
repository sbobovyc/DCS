"""
Created on June 22, 2011

@author: sbobovyc
"""
import ctypes
import os
import random
from PIL import Image

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
                pix[i, j] = color 
    
##
# @param image_path: full path to the image 
# @return: list of image pixels
def get_image_pixels(image_path):
    #read image_path
    src_image = Image.open(image_path)    
    print src_image.format, src_image.size, src_image.mode    
    #put image_path pixels in a list
    pixel_list = list(src_image.getdata())
    return pixel_list

##
# @param pixel_list: list of image pixels 
# @return: a sorted histogram of colors in the image
def histogram_colors(pixel_list):
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
            
    return sorted_histogram

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
        color_list.append( ((tmp_red/tmp_weight, tmp_green/tmp_weight, tmp_blue/tmp_weight, 255), tmp_weight) )
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
    utils = ctypes.CDLL(os.path.join(path, "utils.so"))
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
    for i in range(canvas_height.value):
        # fill out each pointer with an array of ints.
        ptr[i] = INTARR()
        for j in range(canvas_width.value):
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
    image = os.path.join(os.getcwd(), "image.jpeg")
    numcolors = 3
    hist = histogram_colors(get_image_pixels(image))
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
    image_list[0].save("layer0.png")
    i = 1
    for each in colors:
        random.seed()
        seed = random.randrange(0,10000)
        mask = draw_blobs(canvas_width, canvas_height, octave_count, frequency, persistence, seed, threshold, z)
        mask_list.append(mask)
        out_image = Image.new("RGBA", (canvas_width, canvas_height), (0,0,0,0))  #completely transparent image        
        draw_pixels(mask, out_image, each[0])
        image_list.append(out_image)
        out_image.save("layer%i.png" % i)
        i += 1
    
    final_image = combine_layers(image_list, canvas_width, canvas_height)    
    final_image.save("out.png")
