import wx


class MainFrame(wx.Frame):
    """ Just a frame with a DrawPane """

    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(DrawPane(self), 1, wx.EXPAND)
        self.SetSizer(s)

########################################################################
class DrawPane(wx.PyScrolledWindow):
    """ A PyScrolledWindow with a 1000x1000 drawable area """

    VSIZE = (1000, 1000)

    def __init__(self, *args, **kw):
        wx.PyScrolledWindow.__init__(self, *args, **kw)
        self.SetScrollbars(10, 10, 100, 100)
        self.prepare_buffer()
        cdc = wx.ClientDC(self)
        self.PrepareDC(cdc)
        dc = wx.BufferedDC(cdc, self.buffer)

        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_MOTION, self.on_motion)

    def prepare_buffer(self):
        self.buffer = wx.EmptyBitmap(*DrawPane.VSIZE)
        cdc = wx.ClientDC(self)
        self.PrepareDC(cdc)
        dc = wx.BufferedDC(cdc, self.buffer)
        dc.Clear()
        bmp = wx.Bitmap("t62.jpg")
        dc.DrawBitmap(bmp, 0, 0)  
        #dc.DrawLine(0, 0, 999, 999) # Draw something to better show the flicker problem


    def on_paint(self, evt):
        dc = wx.BufferedPaintDC(self, self.buffer, wx.BUFFER_VIRTUAL_AREA)

    def on_mouse_down(self, evt):
        self.mouse_pos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()

    def on_motion(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            newpos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
            coords = self.mouse_pos + newpos
            cdc = wx.ClientDC(self)
            self.PrepareDC(cdc)
            dc = wx.BufferedDC(cdc, self.buffer)
            dc.DrawLine(*coords)
            self.mouse_pos = newpos

if __name__ == "__main__":
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    MainFrame(None).Show()
    app.MainLoop()
