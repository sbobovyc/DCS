'''
Created on Dec 24, 2010

@author: sbobovyc
'''

from Tkinter import *
from tkMessageBox import *
from tkColorChooser import askcolor              
from tkFileDialog   import askopenfilename      

class DCS_file_chooser(object):
    def callback(self):
        askopenfilename() 
    
    def __init__(self):    
        errmsg = 'Error!'
        Button(text='Quit', command=self.callback).pack(fill=X)
        Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
        mainloop()

if __name__ == '__main__':
    DCS_file_chooser()

        