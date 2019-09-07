import wx


class Display(wx.Frame):

    def __init__(self, *args, **kw):
        super(Display, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        closeButton = wx.Button(pnl, label='Close', pos=(20, 20))
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Centre()

    def OnClose(self, e):
        self.Close(True)


def main():

    app = wx.App()
    ex = Display(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()  