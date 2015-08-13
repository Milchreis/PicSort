# -*- coding: utf-8 -*-

'''
@author: nick
'''

import wx
import threading
import initwindow
import themewindow

class WindowApp(threading.Thread):
 
    def __init__(self, appModel):
        threading.Thread.__init__(self)
        
        self.model = appModel
        
        self.app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        
        self.mainWindow = initwindow.InitWindow(None, 1, style=wx.CAPTION)
        self.mainWindow.model = self.model
        self.mainWindow.Center()
        
        self.mainWindow.Show()

      
    def openThemeWindow(self):
        wx.CallAfter(self.__createThemeWindow)

    
    def __createThemeWindow(self):
#         self.themeWindow = themewindow.ThemeWindow(None, 2, style=wx.CAPTION)
#         self.themeWindow.model = self.model
#         self.themeWindow.SetPosition((self.model.windowWidth/2-(self.themeWindow.GetSize()[0]/2), 50))
#         self.themeWindow.Show()
        
        chgdep = themewindow.ThemeDialog(None)
        chgdep.model = self.model
        chgdep.ShowModal()
        chgdep.Destroy()
        
        
    def run(self):
        self.app.MainLoop()
        
        
    def close(self):
        self.app.ExitMainLoop()


