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