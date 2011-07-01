#! /bin/env python2.6
'''
Created on Oct 4, 2010

@author: sbobovyc
'''
import Image
import ImageDraw
import matplotlib.pyplot as plt
import pylab

if __name__ == '__main__':
    im = Image.open("image.jpeg")
    print im.format, im.size, im.mode
    hist = im.histogram()
    print len(hist)
    red = hist[0:256]
    green = hist[256:512]
    blue = hist[512:768]
    x_axis = range(0,256)

    plt.plot(x_axis, red, 'r')
    plt.plot(x_axis, green, 'g')
    plt.plot(x_axis, blue, 'b')

    plt.show()
    
    data = im.getdata()
    #for pixel in data:
    #	print pixel
    pylab.hist(data, bins=50, normed=1)
    pylab.show()
    #img = Image.new("RGB", (400,400), color=(255,255,255))
    #draw = ImageDraw.Draw(img)
    #draw.polygon([(60,60), (90,60), (90,90), (60,90)], fill=(shadows_red_max, shadows_green_max, shadows_blue_max))
    #draw.polygon([(90,60), (120,60), (120,90), (90,90)], fill=(midtones_red_max, midtones_green_max, midtones_blue_max))
    #draw.polygon([(120,60), (120,60), (150,90), (120,90)], fill=(highlights_red_max, highlights_green_max, highlights_blue_max))
    #img.show()
    #img.save("out.jpg")
