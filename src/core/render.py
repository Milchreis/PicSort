# -*- coding: utf-8 -*-

'''
@author: nick
'''

import pygame
import threading
from gui.components import InfoField

class ScreenRenderer(threading.Thread):

    def __init__(self, appModel):
        threading.Thread.__init__(self)

        self.model = appModel
        self.uicomponents = []
        
        pygame.init()
        
        screenInfo = pygame.display.Info()
        self.model.windowWidth = screenInfo.current_w
        self.model.windowHeight = screenInfo.current_h
    
        self.screen = None
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("sans", 14 )
        self.font.set_bold(True)
        
        self.themeInfo = InfoField()
        self.themeInfo.position = (self.model.windowWidth/2 - (100/2), 10)
        
        self.themeInfo = InfoField()
        self.themeInfo.position = (self.model.windowWidth/2 - (100/2), 10)
        self.themeInfo.event = self.updateTheme
        self.uicomponents.append(self.themeInfo)
        self.isFullscreen = False
        
    def updateTheme(self):
        self.themeInfo.text = self.model.theme

    def setFullscreen(self, enable):
        if enable:
            pygame.display.set_mode((self.model.windowWidth, self.model.windowHeight), pygame.FULLSCREEN)
            self.isFullscreen = True
        else:
            pygame.display.set_mode((self.model.windowWidth, self.model.windowHeight))
            self.isFullscreen = False
    
    
    def run(self):
        self.screen = pygame.display.set_mode((self.model.windowWidth, self.model.windowHeight))
        
        pygame.mouse.set_visible(1)
        pygame.key.set_repeat( 1, 30 )

        while self.model.isrunning:
            self.clock.tick( 25 )
            
            eventDetected = False
            for event in pygame.event.get():
                self.model.inputprocessor.process(event)
                eventDetected = True
                
            if eventDetected:
                self.screen.fill((0,0,0))
                if not self.model.img == None:
                    x = self.model.windowWidth/2 - self.model.img.get_width()/2
                    y = self.model.windowHeight/2 - self.model.img.get_height()/2
                    self.screen.blit(self.model.img, (x, y))
                
                for ui in self.uicomponents:
                    ui.refresh()
                    ui.render(self.screen)
                
                for plugin in self.model.pluginmanager.plugins:
                    try:
                        self.model.pluginmanager.plugins[plugin].render()
                    except Exception, e:
                        self.model.logger.warn("Error while render for: " + plugin)
                        self.model.logger.warn(plugin + " -> " + str(e))
                
                pygame.display.flip()
                pygame.display.set_caption( "FPS: %.1f" % self.clock.get_fps() )
            
        pygame.quit()
        