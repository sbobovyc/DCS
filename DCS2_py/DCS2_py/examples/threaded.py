import Tkinter
import threading
class MyTkApp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    def callback(self):
       self.root.quit()
    def run(self):
        self.root=Tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.s = Tkinter.StringVar()
        self.s.set('Foo')
        l = Tkinter.Label(self.root,textvariable=self.s)
        l.pack()
        self.root.mainloop()
app = MyTkApp()
print 'now can continue running code while mainloop runs'
