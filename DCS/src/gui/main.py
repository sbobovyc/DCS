#/usr/bin/env python
"""
Created on June 28, 2011

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

import os
import sys
DCS_path = os.path.abspath("..") 
sys.path.append(DCS_path) 
print sys.path

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

from menubar import GUI_menubar
from work_frame import GUI_work_frame
from display_frame import GUI_display_frame
from utils import Utils
import Controller

import ctypes
import win32api
import win32gui
import win32process
import win32con

def windowEnumerationHandler(hwnd, resultList):

    '''Pass to win32gui.EnumWindows() to generate list of window handle, window text tuples.'''

    resultList.append((hwnd, win32gui.GetWindowText(hwnd)))
    
class GUI_main(tk.Tk):
    '''
    classdocs
    '''
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.name = "main"   

        # if on linux, set the icon
        if Utils.isLinux():                
            os.path.join("..", "dcs.xbm")     
            self.iconbitmap('@../dcs.xbm')    
        if Utils.isWindows():
             
            #print ctypes.windll.kernel32.GetCurrentProcessId()
            #topWindows = []
            #win32gui.EnumWindows(windowEnumerationHandler, topWindows)
            #print topWindows
            whndl = self.winfo_id() #inner
            outer = self.wm_frame()

            print whndl            
            print outer
            hinst =  win32api.GetModuleHandle(None)
            print hinst
            pid, ppid = win32process.GetWindowThreadProcessId(hinst)
            print win32gui.GetWindowText(hinst)
            print pid
            print ppid
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            hicon = win32gui.LoadImage(whndl,
                                   "dcs.ico",
                                   win32con.IMAGE_ICON,
                                   0,
                                   0,
                                   icon_flags)
            message = win32gui.NIM_MODIFY
            notify_id = (whndl,
                          0,
                          win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP,
                          win32con.WM_USER+20,
                          hicon,
                          '')
        
            win32gui.Shell_NotifyIcon(message, notify_id)
            #win32gui.PostMessage(hinst, win32con.WM_CLOSE,0,0)
            #self.iconbitmap(default="..\dcs.ico")
        
        # instantiate the controller, register with the controller
        self.controller = Controller.Controller()
        self.controller.register(self, self.name)
        self.initialize()
        
    def initialize(self):
        # make the main window cover the entire screen
        if Utils.isLinux():
            self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
            self.geometry("%dx%d+0+0" % (self.w, self.h))
        if Utils.isWindows():
            self.wm_state('zoomed')    
        #create menu
        self.menu = GUI_menubar(self, self.controller)
        self.config(menu=self.menu)
        
        
        #create frame structure
        self.big_frame = tk.Frame(self, bd=2, relief=tk.FLAT, background="grey")
        self.big_frame.pack(anchor=tk.NW, expand=tk.TRUE, fill=tk.BOTH)
        
        self.work_frame = GUI_work_frame(self.big_frame, self.controller)
        self.work_frame.pack(side=tk.RIGHT, anchor=tk.N)
        
        self.display_frame = GUI_display_frame(self.big_frame, self.controller)
        self.display_frame.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH)
                     
        
if __name__ == "__main__":
    app = GUI_main(None)
    app.title('DCS')    
    app.mainloop()
