import random
from PIL import Image,ImageTk
from DCS import Utils
from DCS import Layer
from DCS import Base_Layer
from progressbar import ProgressBar

import Tkinter

class Controller(object):
    
    def __init__(self):
        self.image_path = None  #current image_path
        self.object_map = {}    #map of gui objects (name to object)
        self.histogram = []     #color histogram         
        self.layer_list = []    #list of layers
        self.imagePIL = None    #generated image, in PIL format
        self.imagetk = None     #generated image, in Tkinter format
    
    ##
    # @param object: a tkinter gui object
    # @param name: a string that represent the name of the object
    def register(self, object, name):        
        self.object_map[name] = object
    
    def open_image(self, image_path):
        self.image_path = image_path
        self.set_thumbnail(image_path)
        self.generate_layers_init()
    
    def save_image(self, image_path):                
        self.imagePIL.save(image_path)
    
    ##
    # This function generates the initial layers. Parameters are taken from the gui, except the seed.
    def generate_layers_init(self):
        #clear out data        
        del self.layer_list[:]
        del self.histogram[:]
        
        #grab params from gui    
        params = self.object_map["work_frame"].get()
         
        #generate histogram
        pixels = Utils.get_image_pixels(self.image_path)
        self.histogram = Utils.histogram_colors(pixels)
        color_list = Utils.calc_colors(self.histogram, int(params["num_colors"]))        
        base_color = Utils.calculate_base_color(color_list)
        print color_list
        print base_color       
        
        #create base layer
        base_layer = Base_Layer.Base_Layer(int(params["width"]), int(params["height"]), base_color)
        self.layer_list.append(base_layer)
        self.object_map["layer_list"].insert_layer(base_layer)
        
        #create layers 
        i = 1
        for color in color_list:
            if params["seed"] == "rand":
                seed = random.randint(0, 1000)
            else:
                seed = int(params["seed"])
            layer = Layer.Layer(i, int(params["width"]), int(params["height"]), int(params["octave_count"]),
                                               float(params["frequency"]), float(params["persistence"]), seed, 
                                               float(params["threshold"]), float(params["z"]), color[0], color[1])            
            self.layer_list.append(layer)
            self.object_map["layer_list"].insert_layer(layer)
            i += 1
            
        # select the first layer in the list
        # not used, since the user may be confused as to why they have to click again on 
        # a highlighted value
#        self.object_map["layer_list"].layers.selection_set(first=0) 
#        self.object_map["layer_list"].layers.activate(0)

        # clear fields in work frame
        self.object_map["work_frame"].clear_fields()
    
    ##
    # @param layer_id: ID of the selected layer. This may be a string, so it needs
    # to be converted to an int. 
    def select_layer(self, layer_id):
        # clear fields in work frame
        self.object_map["work_frame"].clear_fields()
        # get the layer from layer_list by id
        layer = self.layer_list[int(layer_id)]
        # fill the gui with parameters of a particular layer
        self.object_map["work_frame"].set_fields(layer)
        # set color of layer canvas
        self.object_map["layer_list"].current_color.config(bg = ("#%02x%02x%02x" % layer.color))
                    
    def update_layer(self, layer_id):
        # get the layer from layer_list by id
        layer = self.layer_list[int(layer_id)]
            
        # check if the base layer was selected
        if layer.id == "base":
            pass
        else:
            
            #grab params from gui    
            params = self.object_map["work_frame"].get()
            # update layer fields
            layer.width = int(params["width"])
            layer.height = int(params["height"])
            layer.octave_count = int(params["octave_count"])
            layer.frequency = float(params["frequency"])
            layer.persistence = float(params["persistence"])
            if params["seed"] == "rand":
                    layer.seed = random.randint(0, 1000)
            else:
                    layer.seed = int(params["seed"])
            
            layer.threshold = float(params["threshold"])
            layer.z =  float(params["z"])
#                layer.color =  color[0]    
    
    def generate_layers(self):        
        #grab params from gui    
        params = self.object_map["work_frame"].get()
        
        # background color is expected to be at the front of the lists
        base_color = self.layer_list[0].color
        
        # create temporary image list        
        image_list = []
        image_list.append(Image.new("RGBA", (int(params["width"]), int(params["height"])), base_color))
        
        #open the progressbar
        pb = ProgressBar(200,50)
        pb.open()
        pb.update(0.0)   
        pb.center()
        #each layer generates mask and draw image_path 
        total = len(self.layer_list)      
        i = 0.0
        for layer in self.layer_list:
            layer.width = int(params["width"])
            layer.height = int(params["height"])
            layer.generate_layer_mask()
            layer.draw_layer()
            image_list.append(layer.image)
            i += 1.0
            pb.update(i/total)            
        pb.close()
        #combine layers                
        self.imagePIL = Utils.combine_layers(image_list, int(params["width"]), int(params["height"]))
        self.imagetk=ImageTk.PhotoImage(self.imagePIL)                       
        self.object_map["display_frame"].canvas.create_image(0,0,image=self.imagetk)
        #scroll the canvas        
        self.object_map["display_frame"].canvas.config(scrollregion=self.object_map["display_frame"].canvas.bbox(Tkinter.ALL))
        
    def generate_layers2(self):
        #clear out data        
        del self.layer_list[:]
        del self.histogram[:]
        
        
        #grab params from gui    
        params = self.object_map["work_frame"].get()
         
        #generate histogram
        pixels = Utils.get_image_pixels(self.image_path)
        self.histogram = Utils.histogram_colors(pixels)
        color_list = Utils.calc_colors(self.histogram, int(params["num_colors"]))        
        base_color = Utils.calculate_base_color(color_list)
        # calculate background color, each color has a weight of 1, the effect is that 
        # the colors are averaged
        color_list = []
        for layer in self.layer_list:
            color_list.append((layer.color, layer.color_weight))      
        base_color = Utils.calculate_base_color(color_list)
        print color_list
        print base_color
        image_list = []
        image_list.append(Image.new("RGBA", (int(params["width"]), int(params["height"])), base_color))
        for color in color_list:
            layer = Layer.Layer(int(params["width"]), int(params["height"]), int(params["octave_count"]),
                                               float(params["frequency"]), float(params["persistence"]), int(params["seed"]), 
                                               float(params["threshold"]), float(params["z"]), color[0])            
            self.layer_list.append(layer)
            self.object_map["layer_list"].insert_layer(layer)
        #each layer generates mask and draw image_path        
        for layer in self.layer_list:
            layer.generate_layer_mask()
            layer.draw_layer()
            image_list.append(layer.image)            
            
        #combine layers        
        #compose an image from the background color and layers
        image = Utils.combine_layers(image_list, int(params["width"]), int(params["height"]))
        self.imagetk=ImageTk.PhotoImage(image)                       
        self.object_map["display_frame"].canvas.create_image(0,0,image=self.imagetk)
        
#        config(scrollregion=self.parent_gui.canvas.bbox(Tkinter.ALL))
        #send layer info to gui
        
        
    def set_thumbnail(self, image_path):
        self.object_map["thumbnail"].display_thumbnail(image_path)        