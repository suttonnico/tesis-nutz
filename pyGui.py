#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
+++++UI++++++

In this code example, we create a static line.

author: Edu
last modified: Septiembre 2019
"""


import wx
import fileLibrary

class Example(wx.Frame):
    Data = fileLibrary.nueces_data()
    winsize = 0
    xsize = 100
    ysize = 0
    center = [0, 0]
    offsetX = 80                                   #offset en X
    offsetY = 50                                     #Offset entre titulo y oración
    offsetYT = 10                                   #Offset entre titulos
    offsetTitleY = 50
    offsetValue = 600

    Buenas = 0
    Malas = 0
    Buenas_chicas = 0
    Buenas_grandes = 0
    Umbral = None

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.Buenas = self.Data.get_clasif_buenas_value()
        self.Malas = self.Data.get_clasif_malas_value()
        self.Buenas_chicas = self.Data.get_subclasif_buenas_chicas_value()
        self.Buenas_grandes = self.Data.get_subclasif_buenas_grandes_value()
        self.Umbral = self.Data.get_config_value()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateInfo, self.timer)
        self.timer.Start(500)
        self.InitUI()

    def InitUI(self):

        """Set windows sizes"""
        self.Maximize()
        self.SetBackgroundColour('#CCFFFF')
        self.winsize = self.GetSize()
        self.xsize = self.winsize[0]
        self.ysize = self.winsize[1]
        self.center[0] = self.winsize[0]/2
        self.center[1] = self.winsize[1]/2

        """Titulo"""
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label='Clasificación de Nueces', pos=(self.center[0] - self.offsetX + 100, self.center[1] - self.offsetY - self.offsetTitleY), size=(200, -1))
        heading.SetFont(font)

        font2 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        wx.StaticLine(self, pos=(self.center[0] - self.offsetX + 100, self.center[1] - self.offsetY - self.offsetTitleY + 40), size=(heading.GetSize()[0], 1))

        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 17), size=(650, 2))
        text1 = wx.StaticText(self, label='Diámetro umbral de la nuez', pos=(self.center[0] - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 20))
        text2 = wx.StaticText(self, label=self.Umbral, pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 20))
        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 45), size=(650, 2))

        text1.SetFont(font2)
        text2.SetFont(font2)

        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX + 646, self.center[1] - self.offsetY + self.offsetYT + 17), size=(3, 28))
        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 18), size=(3, 28))

        """Subtitulo Nueces en Buen estado"""
        font3 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        subheading1 = wx.StaticText(self, label='Nueces en Buen estado', pos=(self.center[0] - self.offsetX, self.center[1] - self.offsetY  + self.offsetYT + 55), size=(200, -1))
        subheading1.SetFont(font3)

        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 87), size=(650, 2))
        text3 = wx.StaticText(self, label='Cantidad total de nueces en buen estado', pos=(self.center[0] - self.offsetX, self.center[1] - self.offsetY  + self.offsetYT + 90))
        text4 = wx.StaticText(self, label=self.Buenas, pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY  + self.offsetYT + 90))

        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 116), size=(650, 2))
        text5 = wx.StaticText(self, label='Cantidad de nueces de diámetro mayor al umbral', pos=(self.center[0] - self.offsetX, self.center[1] - self.offsetY  + self.offsetYT + 120))
        text6 = wx.StaticText(self, label=self.Buenas_grandes, pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 120))

        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 148), size=(650, 2))
        text7 = wx.StaticText(self, label='Cantidad de nueces de diámetro menor al umbral', pos=(self.center[0] - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 150))
        text8 = wx.StaticText(self, label=self.Buenas_chicas, pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 150))
        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 177), size=(651, 2))

        text3.SetFont(font2)
        text4.SetFont(font2)
        text5.SetFont(font2)
        text6.SetFont(font2)
        text7.SetFont(font2)
        text8.SetFont(font2)

        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX + 600, self.center[1] - self.offsetY + self.offsetYT + 87), size=(2, 90))
        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 87), size=(2, 90))

        """Subtitulo Nueces en mal estado"""
        subheading2 = wx.StaticText(self, label='Nueces en mal estado', pos=(self.center[0] - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 190))
        subheading2.SetFont(font3)

        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 223), size=(650, 2))
        text9 = wx.StaticText(self, label='Cantidad de nueces en mal estado', pos=(self.center[0] - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 225))
        text10 = wx.StaticText(self, label=self.Malas, pos=(self.center[0] - self.offsetX + self.offsetValue,self.center[1] - self.offsetY + self.offsetYT + 225))
        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 253), size=(650, 2))

        text9.SetFont(font2)
        text10.SetFont(font2)

        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX + 600, self.center[1] - self.offsetY + self.offsetYT + 223), size=(2, 32))
        wx.StaticLine(self, pos=(self.center[0] - 5 - self.offsetX, self.center[1] - self.offsetY + self.offsetYT + 223), size=(2, 32))


        #tsum = wx.StaticText(self, label='164 336 000', pos=(240, 280))
        #sum_font = tsum.GetFont()
        #sum_font.SetWeight(wx.BOLD)
        #tsum.SetFont(sum_font)


        btn = wx.Button(self, label='Close', pos=(self.center[0], self.center[1] - self.offsetY  + self.offsetYT  + 300))

        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        #self.SetBackgroundColour('#3f5049')
        #self.SetBackgroundStyle()
        #self.SetSize((450, 300))
        #self.Maximize()
        self.SetTitle('UI')
        self.Centre()

        #self.Data.set_config_value( self.Data.get_config_value() + "1")

    def OnClose(self, e):
        self.Close(True)

    def updateInfo(self, event):
        #self.Data.set_config_value( self.Data.get_config_value() + "1")
        self.Data.read_values()
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        #self.clean_values()
        if self.Data.get_config_value() != self.Umbral:
            self.Umbral = self.Data.get_config_value()
            text1 = wx.StaticText(self, label="             ", pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 20))
            text2 = wx.StaticText(self, label=self.Data.get_config_value(), pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 20))
            text1.SetFont(font)
            text2.SetFont(font)
        if self.Data.get_clasif_buenas_value() != self.Buenas:
            self.Buenas = self.Data.get_clasif_buenas_value()
            text1 = wx.StaticText(self, label="             ", pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY  + self.offsetYT + 90))
            text2 = wx.StaticText(self, label=self.Data.get_clasif_buenas_value(), pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY  + self.offsetYT + 90))
            text1.SetFont(font)
            text2.SetFont(font)
        if self.Data.get_subclasif_buenas_grandes_value() != self.Buenas_grandes:
            self.Buenas_grandes = self.Data.get_subclasif_buenas_grandes_value()
            text1 = wx.StaticText(self, label="             ", pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 120))
            text2 = wx.StaticText(self, label=self.Data.get_subclasif_buenas_grandes_value(), pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 120))
            text1.SetFont(font)
            text2.SetFont(font)
        if self.Data.get_subclasif_buenas_chicas_value() != self.Buenas_chicas:
            self.Buenas_chicas = self.Data.get_subclasif_buenas_chicas_value()
            text1 = wx.StaticText(self, label="             ", pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 150))
            text2 = wx.StaticText(self, label=self.Data.get_subclasif_buenas_chicas_value(), pos=(self.center[0] - self.offsetX + self.offsetValue, self.center[1] - self.offsetY + self.offsetYT + 150))
            text1.SetFont(font)
            text2.SetFont(font)
        if self.Data.get_clasif_malas_value() != self.Malas:
            self.Malas = self.Data.get_clasif_malas_value()
            text1 = wx.StaticText(self, label="             ", pos=(self.center[0] - self.offsetX + self.offsetValue,self.center[1] - self.offsetY + self.offsetYT + 225))
            text2 = wx.StaticText(self, label=self.Data.get_clasif_malas_value(), pos=(self.center[0] - self.offsetX + self.offsetValue,self.center[1] - self.offsetY + self.offsetYT + 225))
            text1.SetFont(font)
            text2.SetFont(font)

        #else:
            #print("No changes")

    def clean_values(self):
       #wx.CLEAR()
       wx.StaticText(self, label="                ", pos=(350 + self.offsetX, 40 + self.offsetY))


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
