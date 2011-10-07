import Tkinter
import random
import tkColorChooser

def cmd(event):
    color1 = tkColorChooser.askcolor(title="Choose first color")[0] 
    
if __name__ == '__main__':
    root = Tkinter.Tk()
    root.title('Color Filters')
    root.resizable(0,0)

    ## Grid sizing behavior in window
    root.grid_rowconfigure(3, pad=0, weight=0)
#    root.grid_columnconfigure(0, pad=0, weight=0)
    cnv = Tkinter.Canvas(root, width=200)
    cnv.grid(row=0, column=0, sticky='nswe')
    ## Scrollbars for canvas 
    vScroll = Tkinter.Scrollbar(root, orient=Tkinter.VERTICAL, command=cnv.yview)
    vScroll.grid(row=0, column=4, sticky='ns')
    cnv.configure(yscrollcommand=vScroll.set)
    ## Frame in canvas
    frame = Tkinter.Frame(cnv)
    ## This puts the frame in the canvas's scrollable zone
    cnv.create_window(0, 0, window=frame, anchor='nw')
    ## Frame contents
    Tkinter.Button(frame, text="Add filter").grid(row=0, column=0)
    color1 = Tkinter.Label(frame, text="Color1")
    color1.grid(row=1, column=0)
    color2 = Tkinter.Label(frame, text="Color2")
    color2.grid(row=1, column=1)
    enabled = Tkinter.Label(frame, text="Enabled")
    enabled.grid(row=1, column=2)

 
    for i in range(2,102):
        label1 = Tkinter.Label(frame, width=3, bg="#%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        label1.grid(row=i,column=0)
        label2 = Tkinter.Label(frame, width=3, bg="#%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        label2.grid(row=i,column=1)
        label1.bind("<Button-1>", cmd)
        Tkinter.Checkbutton(frame).grid(row=i, column=2)
        Tkinter.Button(frame, text="Delete").grid(row=i, pady=5, column=3)
    ## Update display to get correct dimensions
    frame.update_idletasks()
    ## Configure size of canvas's scrollable zone
    cnv.configure(scrollregion=(0, 0, frame.winfo_width(), frame.winfo_height()))
    
    
    
    root.mainloop() 





