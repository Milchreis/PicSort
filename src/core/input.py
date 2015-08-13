# -*- coding: utf-8 -*-

'''
@author: nick
'''

import pygame

class InputProcessor():

    def __init__(self, appModel):
        self.model = appModel

    
    def process(self, event):
        if event.type == pygame.QUIT:
            self.model.closeWindow()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.model.closeWindow()
            
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            self.model.getNextImage()
        
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            self.model.getPreviousImage()

        if event.type == pygame.KEYUP and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
            self.model.renderer.setFullscreen(False)
            self.model.changeTheme()

        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.model.copyImage()
            self.model.getNextImage()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if self.model.renderer.isFullscreen:
                self.model.renderer.setFullscreen(False)
            else:
                self.model.renderer.setFullscreen(True)
            
        for plugin in self.model.pluginmanager.plugins:
            try:
                self.model.pluginmanager.plugins[plugin].onEvent(event, self.model)
            except Exception, e:
                self.model.logger.warn("Error while input for: " + plugin)
                self.model.logger.warn(plugin + " -> " + str(e))