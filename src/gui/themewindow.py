# -*- coding: utf-8 -*-

'''
@author: nick
'''

import wx

class ThemeDialog(wx.Dialog):
    
    def __init__(self, *args, **kw):
        super(ThemeDialog, self).__init__(*args, **kw) 
            
        self.SetSize((350, 100))
        self.SetTitle("Change the theme")
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        
        self.model = None
        
        self.label = wx.StaticText(self, -1, "New theme")
        self.themeInput = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.themeInput.Bind(wx.EVT_TEXT_ENTER, self.onConfirm)

        inBox = wx.BoxSizer(wx.HORIZONTAL)
        inBox.Add(self.label, 0, wx.EXPAND | wx.ALL, 5)
        inBox.Add(self.themeInput, 1, wx.EXPAND | wx.ALL, 0)
       
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        mbox = wx.BoxSizer(wx.VERTICAL)
        mbox.Add(inBox, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
        mbox.Add(hbox2, 0, wx.ALIGN_RIGHT | wx.ALL, 10)

        self.SetSizer(mbox)
        
        okButton.Bind(wx.EVT_BUTTON, self.onConfirm)
        closeButton.Bind(wx.EVT_BUTTON, self.onClose)
        self.themeInput.SetFocus()
        
        
    def onConfirm(self, e):
        wx.CallAfter(self.__confirm)

    def __confirm(self):
        self.model.theme = self.themeInput.GetValue()
        self.onClose(None)
#         self.model.renderer.setFullscreen(True)

    def cancel(self, e):
        self.onClose(None)
#         self.model.renderer.setFullscreen(True)

    def onClose(self, e):
        self.Destroy()

