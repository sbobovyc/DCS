# adopted from http://code.activestate.com/recipes/492230-progress_barpy/
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

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


class ProgressBar(object): 

    # Create Progress Bar
    def __init__(self, width, height):
        self.__root = tk.Toplevel()
        self.__root.resizable(False, False)
        self.__root.title('Progress')
        self.__canvas = tk.Canvas(self.__root, width=width, height=height)
        self.__canvas.grid()
        self.__width = width
        self.__height = height        

    # Open Progress Bar
    def open(self):
        self.__root.deiconify()

    # Close Progress Bar
    def close(self):
        self.__root.withdraw()

    # Center Progress Bar            
    def center(self):
        w = self.__root.winfo_screenwidth()
        h = self.__root.winfo_screenheight()
        rootsize = tuple(int(_) for _ in self.__root.geometry().split('+')[0].split('x'))
        x = w/2 - rootsize[0]/2
        y = h/2 - rootsize[1]/2
        self.__root.geometry("%dx%d+%d+%d" % (rootsize + (x, y)))

    # Update Progress Bar
    def update(self, ratio):
        self.__canvas.delete(tk.ALL)
        self.__canvas.create_rectangle(0, 0, self.__width * ratio, \
                                       self.__height, fill='blue')
        self.__root.update()