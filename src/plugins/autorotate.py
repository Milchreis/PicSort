# -*- coding: utf-8 -*-

'''
@author: nick
'''
from core.image import resizeImage

AUTHOR = "Nick"
VERSION = 1.0
PLUGIN_NAME = "auto rotate"
DESCIPTION = """
Reads the exif data an tries to rotate the image
"""

import pygame
import exifread

def init(pluginmodel):
    pass

def visible(boolean):
    pass

def render():
    pass

def onEvent(event, pluginmodel):
    
    rotationTAG = 'Image Orientation'
    
    if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
        
        img = pluginmodel.images[pluginmodel.counter]
        f = open(img, 'rb')
        tags = exifread.process_file(f, details=False, stop_tag=rotationTAG)
        
        value = tags[rotationTAG]
        print value
        
        if not value == None and value.printable.startswith("Rotated "):
            
            angle = value.printable.split(" ")[1]
            
            if not value.printable.endswith("CW"):
                angle = "-"+angle
                
            img = pygame.transform.rotate(pluginmodel.img, int(angle))
            pluginmodel.img = resizeImage(img, (pluginmodel.windowWidth, pluginmodel.windowHeight)) 
            
        
