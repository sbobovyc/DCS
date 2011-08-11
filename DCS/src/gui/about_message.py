import tkSimpleDialog
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


class About(tkSimpleDialog.Dialog):    
        
    def body(self, parent):        
        tk.Label(parent, text="Value").pack()
        self.e = tk.Entry(parent)
        self.e.pack(padx=5)
        return self.e
    