'''
@author: nick
'''

import pygame

def loadImage(path):
    return pygame.image.load(path)

def getResizedDimension(surface, screendimension):
    
    if surface.get_width() > screendimension[0]:
        
        factor = screendimension[0] / float(surface.get_width())
        height = int(surface.get_height() * factor)
        return (screendimension[0], height)
    
    elif surface.get_height() > screendimension[1]:
    
        factor = screendimension[1] / float(surface.get_height())
        width = int(surface.get_width() * factor)
        return (width, screendimension[1])

    return(surface.get_width(), surface.get_height())

def resizeImage(surface, dimension):
    dim = getResizedDimension(surface, dimension)                
    img = pygame.transform.scale(surface, dim) 
    return img