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
    offsetX = 0                                     #offset en X
    offsetY = 5                                     #Offset entre titulo y oración
    offsetYT = 10                                   #Offset entre titulos

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

        """Titulo"""
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label='Clasificación de Nueces', pos=(25, 15), size=(200, -1))
        heading.SetFont(font)

        wx.StaticLine(self, pos=(25, 35), size=(190, 1))

        wx.StaticLine(self, pos=(20 + self.offsetX, 38 + self.offsetY), size=(400, 2))
        wx.StaticText(self, label='Diámetro umbral de la nuez', pos=(25 + self.offsetX, 40 + self.offsetY))
        wx.StaticText(self, label=self.Umbral, pos=(350 + self.offsetX, 40 + self.offsetY))
        wx.StaticLine(self, pos=(20 + self.offsetX, 56 + self.offsetY), size=(400, 2))

        wx.StaticLine(self, pos=(420 + self.offsetX, 38 + self.offsetY), size=(2, 20))
        wx.StaticLine(self, pos=(20 + self.offsetX, 38 + self.offsetY), size=(2, 20))

        """Subtitulo Nueces en Buen estado"""
        font2 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        subheading1 = wx.StaticText(self, label='Nueces en Buen estado', pos=(25 + self.offsetX, 60 + self.offsetYT), size=(200, -1))
        subheading1.SetFont(font2)

        wx.StaticLine(self, pos=(20 + self.offsetX, 77 + self.offsetY + self.offsetYT), size=(400, 2))
        wx.StaticText(self, label='Cantidad total de nueces en buen estado', pos=(25 + self.offsetX, 80+ self.offsetY + self.offsetYT))
        wx.StaticText(self, label=self.Buenas, pos=(350 + self.offsetX, 80 + self.offsetY + self.offsetYT))

        wx.StaticLine(self, pos=(20 + self.offsetX, 97 + self.offsetY + self.offsetYT), size=(400, 2))
        wx.StaticText(self, label='Cantidad de nueces de diámetro mayor al umbral', pos=(25 + self.offsetX, 100 + self.offsetY + self.offsetYT))
        wx.StaticText(self, label=self.Buenas_grandes, pos=(350 + self.offsetX, 100 + self.offsetY + self.offsetYT))

        wx.StaticLine(self, pos=(20 + self.offsetX, 117 + self.offsetY + self.offsetYT), size=(400, 2))
        wx.StaticText(self, label='Cantidad de nueces de diámetro menor al umbral', pos=(25 + self.offsetX, 120 + self.offsetY + self.offsetYT))
        wx.StaticText(self, label=self.Buenas_chicas, pos=(350 + self.offsetX, 120 + self.offsetY + self.offsetYT))
        wx.StaticLine(self, pos=(20 + self.offsetX, 137 + self.offsetY + self.offsetYT), size=(400, 2))

        wx.StaticLine(self, pos=(420 + self.offsetX, 77 + self.offsetY + self.offsetYT), size=(2, 62))
        wx.StaticLine(self, pos=(20 + self.offsetX, 77 + self.offsetY + self.offsetYT), size=(2, 62))

        """Subtitulo Nueces en mal estado"""
        subheading2 = wx.StaticText(self, label='Nueces en mal estado', pos=(25 + self.offsetX, 150 + self.offsetY + self.offsetYT))
        subheading2.SetFont(font2)

        wx.StaticLine(self, pos=(20 + self.offsetX, 172 + self.offsetY + self.offsetYT), size=(400, 2))
        wx.StaticText(self, label='Cantidad de nueces en mal estado', pos=(25 + self.offsetX, 175 + self.offsetY + self.offsetYT))
        wx.StaticText(self, label=self.Malas, pos=(350 + self.offsetX, 175 + self.offsetY + self.offsetYT))
        wx.StaticLine(self, pos=(20 + self.offsetX, 190 + self.offsetY + self.offsetYT), size=(400, 2))

        wx.StaticLine(self, pos=(420 + self.offsetX, 172 + self.offsetY + self.offsetYT), size=(2, 20))
        wx.StaticLine(self, pos=(20 + self.offsetX, 172 + self.offsetY + self.offsetYT), size=(2, 20))


        #tsum = wx.StaticText(self, label='164 336 000', pos=(240, 280))
        #sum_font = tsum.GetFont()
        #sum_font.SetWeight(wx.BOLD)
        #tsum.SetFont(sum_font)


        btn = wx.Button(self, label='Close', pos=(140, 220))

        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetBackgroundColour('#3f5049')
        #self.SetBackgroundStyle()
        self.SetSize((450, 300))
        self.SetTitle('UI')
        self.Centre()

        #self.Data.set_config_value( self.Data.get_config_value() + "1")

    def OnClose(self, e):
        self.Close(True)

    def updateInfo(self, event):
        #self.Data.set_config_value( self.Data.get_config_value() + "1")
        self.Data.read_values()
        #self.clean_values()
        if self.Data.get_config_value() != self.Umbral:
            self.Umbral = self.Data.get_config_value()
            wx.StaticText(self, label="                ", pos=(350 + self.offsetX, 40 + self.offsetY))
            wx.StaticText(self, label=self.Data.get_config_value(), pos=(350 + self.offsetX, 40 + self.offsetY))
        if self.Data.get_clasif_buenas_value() != self.Buenas:
            self.Buenas = self.Data.get_clasif_buenas_value()
            wx.StaticText(self, label="                ", pos=(350 + self.offsetX, 80 + self.offsetY + self.offsetYT))
            wx.StaticText(self, label=self.Data.get_clasif_buenas_value(), pos=(350 + self.offsetX, 80 + self.offsetY + self.offsetYT))
        if self.Data.get_subclasif_buenas_grandes_value() != self.Buenas_grandes:
            self.Buenas_grandes = self.Data.get_subclasif_buenas_grandes_value()
            wx.StaticText(self, label="                ", pos=(350 + self.offsetX, 100 + self.offsetY + self.offsetYT))
            wx.StaticText(self, label=self.Data.get_subclasif_buenas_grandes_value(), pos=(350 + self.offsetX, 100 + self.offsetY + self.offsetYT))
        if self.Data.get_subclasif_buenas_chicas_value() != self.Buenas_chicas:
            self.Buenas_chicas = self.Data.get_subclasif_buenas_chicas_value()
            wx.StaticText(self, label="                ", pos=(350 + self.offsetX, 120 + self.offsetY + self.offsetYT))
            wx.StaticText(self, label=self.Data.get_subclasif_buenas_chicas_value(), pos=(350 + self.offsetX, 120 + self.offsetY + self.offsetYT))
        if self.Data.get_clasif_malas_value() != self.Malas:
            self.Malas = self.Data.get_clasif_malas_value()
            wx.StaticText(self, label="                ", pos=(350 + self.offsetX, 175 + self.offsetY + self.offsetYT))
            wx.StaticText(self, label=self.Data.get_clasif_malas_value(), pos=(350 + self.offsetX, 175 + self.offsetY + self.offsetYT))
        else:
            print("No changes")

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