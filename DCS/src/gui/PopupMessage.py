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

import tkSimpleDialog
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


class PopupMessage(tk.Message):    
        
    def __init__(self, parent, delay=2000, **options):
        self.parent = parent
        self.delay = delay
        tk.Message.__init__(self, parent, options)
        self.after(self.delay, self.poll)
        
    def poll(self):
        self.parent.focus_set()
        self.destroy()