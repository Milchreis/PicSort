# -*- coding: utf-8 -*-

'''
@author: nick
'''
from core.image import loadImage

AUTHOR = "Nick"
VERSION = 1.0
PLUGIN_NAME = "magnify"
DESCIPTION = """
Shows an area of the picture in the original size. It is useful for check the 
sharpness of an image.

Activate or deactivate with 's' key.
"""

import pygame


properties = {
    'active'    : False,
    'width'     : 300,
    'height'    : 300,
    'x'         : 10,
    'y'         : 10,
    'model'     : None,
    'img'       : None,
}


def init(pluginmodel):
    global properties
    properties['model'] = pluginmodel


def visible(boolean):
    pass


def render():
    global properties
    
    x, y = pygame.mouse.get_pos()
    
    xFac = float(x) / float(properties['model'].windowWidth)
    x = int(properties['img'].get_width() * xFac)

    yFac = float(y) / float(properties['model'].windowHeight)
    y = int(properties['img'].get_height() * yFac)
    
    if properties['active']: 
        cropped = properties['model'].original.subsurface((x, y, properties['width'], properties['height']))
        properties['model'].renderer.screen.blit(cropped, (properties['x'], properties['y']))


def onEvent(event, pluginmodel):
    global properties
    
    if event.type == pygame.KEYUP and event.key == pygame.K_s:
        properties['active'] = not properties['active']
        properties['img'] = loadImage(pluginmodel.images[pluginmodel.counter])
        render()
        
    if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
        properties['img'] = loadImage(pluginmodel.images[pluginmodel.counter])
        
        
        
            
        
