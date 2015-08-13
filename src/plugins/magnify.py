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
    
    if properties['active']: 
        # border
        s = pygame.Surface((properties['width'], properties['height']))
        s.fill((0,0,0))
        properties['model'].renderer.screen.blit(s, (properties['x'], properties['y']))
        
        cropped = properties['img'].subsurface((x, y, properties['width'], properties['height']))
        properties['model'].renderer.screen.blit(cropped, (properties['x'], properties['y']))


def onEvent(event, pluginmodel):
    global properties
    
    if event.type == pygame.KEYUP and event.key == pygame.K_s:
        properties['active'] = not properties['active']
        
    if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
        properties['img'] = loadImage(pluginmodel.images[pluginmodel.counter])
        
        
        
            
        
