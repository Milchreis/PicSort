# -*- coding: utf-8 -*-

'''
@author: nick
'''

import wx
import core.tools

class InitWindow(wx.Frame):

    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        self.model = None
        
        self.SetTitle('PicSort')
        self.SetSize((305, 250))
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        
        img = wx.Image(core.tools.getResource("res/logo.png"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.img = wx.StaticBitmap(self, -1, img, (10, 5), (img.GetWidth(), img.GetHeight()))
        
        self.source = wx.Button(self, -1, "(1) Choose source directory")
        self.source.Bind(wx.EVT_BUTTON, self.chooseSourceDirectory)

        self.target = wx.Button(self, -1, "(2) Choose target directory")
        self.target.Bind(wx.EVT_BUTTON, self.chooseTargetDirectory)

        vbox = wx.BoxSizer(wx.VERTICAL)
        
        vbox.Add(self.img, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.source, 0, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.target, 0, wx.EXPAND | wx.ALL, 10)
        
        self.SetSizer(vbox)

    def chooseSourceDirectory(self, e):
        self.model.sourceDir = self.getDirectory()

    def chooseTargetDirectory(self, e):
        self.model.targetDir = self.getDirectory()
        self.model.startRender()
        
    def getDirectory(self):
        dlg = wx.DirDialog(self, message="Choose a directory",  defaultPath='')

        if dlg.ShowModal() == wx.ID_OK:
            return dlg.GetPath()