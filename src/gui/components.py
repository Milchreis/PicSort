# -*- coding: utf-8 -*-

'''
@author: nick
'''

import pygame


def isIn(objPos, objBounds, point):
    if (point[0] > objPos[0] and point[0] < objPos[0] + objBounds[0]) and (point[1] > objPos[1] and point[1] < objPos[1] + objBounds[1]):
        return True
    else:
        return False
        

class Component():
    def __init__(self):
        self.position = (None, None)
        self.bounds = (None, None)
        self.action = None

        self.colorBg = (200, 200, 200)
        self.colorBorder = (10, 10, 10)
        
    def update(self, event):
        pass
    
    def refresh(self):
        pass
    
    def render(self, surface):
        pass
        
        
class InfoField(Component):
    def __init__(self):
        Component.__init__(self)
        self.text = ""
        self.alpha = 128
        self.colorBg = (0, 0, 0)
        self.colorFont = (255, 255, 255)
        self.fontSize = 14

        self.font = pygame.font.SysFont("sans", self.fontSize)
        self.font.set_bold(True)
        self.event = None

    def refresh(self):
        if not self.event == None:
            self.event()

    def update(self, event):
        pass

    def render(self, surface):
        if not(self.text == None) and not(self.text == ""):
            text_width, text_height = self.font.size(self.text)

            s = pygame.Surface((text_width + 20, text_height + 10))
            s.set_alpha(self.alpha)
            s.fill(self.colorBg)
            surface.blit(s, self.position)
            
            txt = self.font.render(self.text, 1, self.colorFont)
            surface.blit(txt, (self.position[0] + 10, self.position[1] + 5))


class InputField(Component):
    
    def __init__(self):
        Component.__init__(self)
        self.cursorTime = 500
        self.cursorHide = False
        self.text = ""
        self.active = False

        
    def update(self, event):
        mouse = pygame.mouse.get_pos()

        if event.type == pygame.KEYUP and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            
            elif event.key == pygame.K_KP_ENTER and not self.action == None:
                self.action()
            
            else:
                if event.key in range(256):
                    self.text += chr(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN and isIn(self.position, self.bounds, mouse):
            self.active = True
        
    
    def render(self, pygamesurface):
        # bg
        pygame.draw.rect(pygamesurface, self.colorBg, (self.position[0], self.position[1], self.bounds[0], self.bounds[1]), 0)
        
        # border
        pygame.draw.rect(pygamesurface, self.colorBorder, (self.position[0], self.position[1], self.bounds[0], self.bounds[1]), 1)

        # text
        if len(self.text) > 0:
            myfont = pygame.font.SysFont("sans", 12 )
            txt = myfont.render( self.text, 1, self.colorBorder)
            pygamesurface.blit( txt, (self.position[0] +10 , self.position[1] + 5) )


class Button(Component):

    def __init__(self):
        Component.__init__(self)
        self.text = None
    
        self.colorBg = (30, 30, 30)
        self.buttonColorHover = (40, 40, 40)
        self.buttonColorText = (255, 255, 255)
        
        self.colorBorder = (10, 10, 10)
    
    def update(self, event):
        mouse = pygame.mouse.get_pos()
        if isIn(self.position, self.bounds, mouse):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not(self.action == None):
                self.action();
        
    def render(self, pygamesurface):
        
        mouse = pygame.mouse.get_pos()
        color = self.colorBg
        
        if isIn(self.position, self.bounds, mouse):
            color = self.buttonColorHover
        
        # bg
        pygame.draw.rect( pygamesurface, color, (self.position[0], self.position[1], self.bounds[0], self.bounds[1]), 0 )
        
        # border
        pygame.draw.rect( pygamesurface, self.colorBorder, (self.position[0], self.position[1], self.bounds[0], self.bounds[1]), 1 )

        # text
        myfont = pygame.font.SysFont("sans", 12 )
        txt = myfont.render( self.text, 1, self.buttonColorText)
        pygamesurface.blit( txt, (self.position[0] +10 , self.position[1] + 5) )
        
