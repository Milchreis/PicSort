# -*- coding: utf-8 -*-

'''
@author: nick
'''

AUTHOR = "Nick"
VERSION = 1.0
PLUGIN_NAME = "delete image"
DESCIPTION = """
Deletes an image from the source directory

Use with 'DEL' key
"""

import wx
import pygame
import os

model = None

def showDialog():
    global model
    
    dlg = wx.MessageDialog(None, "Are you sure to delete this image from source directory?", "Delete?", wx.YES_NO | wx.ICON_QUESTION)
    result = dlg.ShowModal() == wx.ID_YES
    dlg.Destroy
    
    if result:
        path = model.images[model.counter]
        delete(path)
    
def delete(filepath):
    os.remove(filepath)
    print "delete: " + filepath
    
def init(pluginmodel):
    global model
    model = pluginmodel

def visible(boolean):
    pass

def render():
    pass

def onEvent(event, pluginmodel):
    if event.type == pygame.KEYUP and event.key == pygame.K_DELETE:
        wx.CallAfter(showDialog)
