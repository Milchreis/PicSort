# -*- coding: utf-8 -*-

'''
@author: nick
'''

import pygame
import exifread

def autoRotate(imagepath, img):
    
    rotationTAG = 'Image Orientation'
        
    f = open(imagepath, 'rb')
    tags = exifread.process_file(f, details=False, stop_tag=rotationTAG)
    
    value = tags[rotationTAG]
    print value
    
    if not value == None and value.printable.startswith("Rotated "):
        
        angle = value.printable.split(" ")[1]
        
        if not value.printable.endswith("CW"):
            angle = "-"+angle
            
        return pygame.transform.rotate(img, int(angle))
            
        
