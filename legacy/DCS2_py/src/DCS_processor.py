import DCS_utils

def analyze_source_image(source_image_path, num_colors):
        hist, err = DCS_utils.histogram_image(source_image_path)
        #error check
        if err != 0:
            return
            
        colors = DCS_utils.calc_colors(hist,num_colors)
        print colors
        
        base_color = (0,0,0) 
        
        for each in colors[0:len(colors)-1]:
            base_color = (base_color[0] + each[0], base_color[1] + each[1], base_color[2] + each[2])
             
        base_color = (base_color[0] / len(colors)-1, base_color[1] / len(colors)-1, base_color[2] / len(colors)-1)
        
        print "base color", base_color
        
def DCS_processor(source_image_path, num_colors, output_width, output_height):

    
    print source_image_path          
    self.analyze_image()
    self.thumb = DCS_utils.source_image_thumbnail(self.source_image_path)
    self.parent_gui.canvas2.create_image(64,64,image=self.thumb)
	output_width = 600
	output_height = 600
	
	self.current_image = Image.new ( "RGB", (output_width,output_height), self.base_color )
	draw = ImageDraw.Draw ( self.current_image )
	
	
	for x in range(0, 500):
	    blob = DCS_utils.Cammo_blob(self.colors[0],0,draw,width,height, max_level=2)
	    blob = DCS_utils.Cammo_blob(self.colors[1],0,draw,width,height, max_level=2)
	    blob = DCS_utils.Cammo_blob(self.colors[2],0,draw,width,height, max_level=2)
	self.imagetk = ImageTk.PhotoImage(self.current_image)
	self.parent_gui.canvas.create_image(0,0,image=self.imagetk)
	self.parent_gui.canvas.config(scrollregion=self.parent_gui.canvas.bbox(Tkinter.ALL))

if __name__ == "__main__":
