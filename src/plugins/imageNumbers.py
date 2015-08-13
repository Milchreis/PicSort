# -*- coding: utf-8 -*-

'''
@author: nick
'''

AUTHOR = "Nick"
VERSION = 1.0
PLUGIN_NAME = "imageNumbers"
DESCIPTION = """
Shows the number of the current image and the number of all images of the current directory

Activate or deactivate with 'n'
"""

import pygame
from gui.components import InfoField

class ImageNumbers():
    
    def __init__(self):
        self.active = True
        self.model = None
        self.numberInfo = InfoField()

    def onEvent(self, event):
        if event.type == pygame.KEYUP and event.key == pygame.K_n:
            self.active = not self.active

        self.render()

    def render(self):
        if self.active:
            self.numberInfo.text = "{}/{}".format(self.model.counter+1, len(self.model.images))
            self.numberInfo.position = (self.model.windowWidth - 100, 10)
            self.numberInfo.render(self.model.renderer.screen)
            
            
    def setModel(self, model):
        self.model = model


__numbers = None

def init(pluginmodel):
    global __numbers
    __numbers = ImageNumbers()
    __numbers.setModel(pluginmodel)

def visible(boolean):
    global __numbers
    __numbers.active = boolean

def render():
    global __numbers
    __numbers.render()

def onEvent(event, pluginmodel):
    global __numbers
    __numbers.onEvent(event)
