import pyGui
import wx

def main():

    app = wx.App()
    ex = pyGui.Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()