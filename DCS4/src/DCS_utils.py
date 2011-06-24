import ctypes
from PIL import Image


def combine_layers(image_list):
    return Image.merge("RGBA", image_list)
##
# @param ptr: ctypes int* array
# @param image: PIL image object 
# @param color: RGB color triple
def draw_pixels(ptr, image, color):
    width = image.size[0]
    height = image.size[1]
    
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
    #TODO test if this works with even numbers
    bin_list = []
    if (len(histogram)  % numcolors) == 0:
        for i in range( (0, numcolors) ):
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
        color_list.append( ((tmp_red/tmp_weight, tmp_green/tmp_weight, tmp_blue/tmp_weight), tmp_weight) )
    # end 3
        
    return color_list

def calculate_base_color(colors):
    """ Weighted average of supplied colors """
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

    return [red, green, blue]

def draw_blobs(width, height, octave_count, frequency, persistence, seed, threshold, z):
    canvas_width = ctypes.c_int(800) 
    canvas_height = ctypes.c_int(800) 
    octave_count = ctypes.c_int(2)  
    frequency = ctypes.c_double(0.04)
    persistence = ctypes.c_double(0.02) 
    seed = ctypes.c_int(22) 
    threshold = ctypes.c_double(0.2) 
    z = ctypes.c_double(1.0) 
    
    
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
    
def main():
    utils = ctypes.CDLL('/home/sbobovyc/workspace/DCS4/src/utils.so')
    image = "/home/sbobovyc/workspace/DCS4/image.jpeg"
    numcolors = 3
    hist = histogram_colors(get_image_pixels(image))
    colors = calc_colors(hist, numcolors)
    print colors 
    print calculate_base_color(colors)
    canvas_width = ctypes.c_int(800) 
    canvas_height = ctypes.c_int(800) 
    octave_count = ctypes.c_int(2)  
    frequency = ctypes.c_double(0.04)
    persistence = ctypes.c_double(0.02) 
    seed = ctypes.c_int(22) 
    threshold = ctypes.c_double(0.2) 
    z = ctypes.c_double(1.0) 
    
    
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
    
    out_image = Image.new("RGBA", (canvas_width.value, canvas_height.value), (0,0,0,0)) #completely transparent image
    draw_pixels(ptr, out_image, colors[0][0])
    
    out_image.save("out.png")

if __name__ == '__main__':
    main()