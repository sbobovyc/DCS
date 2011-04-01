#!/usr/bin/env python

from PIL import Image
from optparse import OptionParser
import sys, gtk, pygtk, time

def Pixbuf2Image(pb, opt):
    '''convert gtk Pixbuf to PIL Image'''
    width, height = pb.get_width(), pb.get_height()
    return Image.fromstring(opt,(width,height),pb.get_pixels())

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-m","--mode",dest="Pal",type="str",default="RGB",metavar="MODE",help = 'Palette')
    parser.add_option("-l","--min" ,dest="Min",type="int",default= 1, metavar="MIN", help = 'Threshold')
    clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
    (options, args) = parser.parse_args()

# monitor clipboard and wait for an image

    while True:
        data = clipboard.wait_for_image()
        time.sleep(500 / 1000.0)
        if data: break
    try:
        Pass = True; Ltot = []
        Lpix = list(Pixbuf2Image(data, options.Pal).getdata())

# iterate through pixels, loading them into a list and calculating totals

        for INX, x in enumerate(Lpix):
            for INC, y in enumerate(Ltot):
                if x == y[0]:
                    Pass = False
                    Ltot[INC][1] += 1
                    break
                else:
                    Pass = True
                    continue
            if Pass:
                Pass = False
                Ltot.append([x,1])

# print the results

        for z in Ltot:
            if z[1] > options.Min:
                print z[0],"\t\t",z[1]
    except Exception, error:
        print "\Failed:\n%s\n" % error