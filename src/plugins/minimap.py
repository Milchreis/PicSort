# -*- coding: utf-8 -*-

'''
@author: nick
'''
from core.image import loadImage, resizeImage

AUTHOR = "Nick"
VERSION = 1.0
PLUGIN_NAME = "minimap"
DESCIPTION = """
Shows a map of the current image stripe.

Activate or deactivate with 'm'
"""

import pygame

class MiniMap():
    
    def __init__(self):
        self.active = False
        self.model = None

        self.thumbW = 100
        self.thumbH = 100
        
        self.thumbPrevious = 3
        self.thumbImgsPrev = []
        self.thumbNext = 3
        self.thumbImgsNext = []

        self.curImg = None

    def reinit(self):
        self.thumbImgsNext = []
        self.thumbImgsPrev = []
        self.curImg = resizeImage(self.model.img, (self.thumbW, self.thumbH))
        
        # Create thumbs for following images
        for i in range(1, self.thumbNext+1):
            if self.model.counter + i < len(self.model.images):
                self.thumbImgsNext.append(resizeImage(loadImage(self.model.images[self.model.counter + i]), (self.thumbW, self.thumbH)))

        # Create thumbs for previous images
        for i in range(1, self.thumbPrevious+1):
            if self.model.counter - i > 0:
                self.thumbImgsPrev.append(resizeImage(loadImage(self.model.images[self.model.counter - i]), (self.thumbW, self.thumbH)))


    def onEvent(self, event):
        if event.type == pygame.KEYUP and event.key == pygame.K_m:
            self.active = not self.active
            
            # Init 
            if self.active:
                self.reinit()

        if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
            
            if self.model.counter == 0:
                self.reinit()
                return
            
            if event.key == pygame.K_RIGHT:
                try:
                    # Neues Bild hinzu (rechts)
                    self.thumbImgsNext.append(resizeImage(loadImage(self.model.images[self.model.counter + self.thumbNext]), (self.thumbW, self.thumbH)))
                except: pass

                try:
                    # erstes Bild weg
                    self.thumbImgsNext.pop(0)
                except: pass
                
                # Links: Current als neues Bild
                self.thumbImgsPrev.insert(0, self.curImg)

                # erstes Bild weg
                if len(self.thumbImgsPrev) > self.thumbPrevious:
                    self.thumbImgsPrev = self.thumbImgsPrev[:-1]
               
            if event.key == pygame.K_LEFT:
                # Neues Bild hinzu (rechts)
                self.thumbImgsNext.insert(0, self.curImg)
                
                # Letztes Bild weg
                if len(self.thumbImgsNext) > self.thumbNext:
                    self.thumbImgsNext = self.thumbImgsNext[:-1]
                
                try:
                    # Links: Current als neues Bild
                    self.thumbImgsPrev.append(resizeImage(loadImage(self.model.images[self.model.counter - self.thumbPrevious]), (self.thumbW, self.thumbH)))
                except: pass
                
                # erstes Bild weg
                self.thumbImgsPrev = self.thumbImgsPrev[1:]

            self.curImg = resizeImage(self.model.img, (self.thumbW, self.thumbH))
            
        self.render()

    def render(self):
        if self.active:
            s = pygame.Surface((self.model.windowWidth, self.thumbH + 6))
            s.set_alpha(128)
            s.fill((0,0,0))
            self.model.renderer.screen.blit(s, (0, self.model.windowHeight-self.thumbH-6))
            
            # draw current
            # border
            s = pygame.Surface((self.thumbW+6, self.thumbH+6))
            s.fill((0,0,0))
            self.model.renderer.screen.blit(s, (self.model.windowWidth/2-self.thumbW/2-3, self.model.windowHeight-self.thumbH-8))
            self.model.renderer.screen.blit(self.curImg, (self.model.windowWidth/2-self.thumbW/2, self.model.windowHeight-self.thumbH-3))
            
            i=1
            for img in self.thumbImgsNext:
                img.set_alpha(200)
                self.model.renderer.screen.blit(img, ((i*self.thumbW) + (i*3) + 12 + self.model.windowWidth/2-self.thumbW/2-3, self.model.windowHeight-self.thumbH-3))
                i += 1

            i=1
            for img in self.thumbImgsPrev:
                img.set_alpha(200)
                self.model.renderer.screen.blit(img, (self.model.windowWidth/2-self.thumbW/2 - 12 - (i*self.thumbW) - (i*3), self.model.windowHeight-self.thumbH-3))
                i += 1
                

    def setModel(self, model):
        self.model = model


__numbers = None

def init(pluginmodel):
    global __numbers
    __numbers = MiniMap()
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
