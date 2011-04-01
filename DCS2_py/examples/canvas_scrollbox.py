from Tkinter import *
root = Tk()
frame = Frame(root, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

canvas = Canvas(frame, bd=0,
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

canvas.grid(row=0, column=0, sticky=N+S+E+W)

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

frame.pack()

mainloop()