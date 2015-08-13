# -*- coding: utf-8 -*-

'''
@author: nick
'''

import logging
import shutil
import os
from core.image import loadImage, resizeImage
from core.input import InputProcessor
from gui.window import WindowApp
from core.render import ScreenRenderer
from core.pluginmanager import PluginManager
from core import tools

class AppModel():

    def __init__(self):
        self.logger = logging.getLogger('picsort')
        
        self.sourceDir = None
        self.targetDir = None
        
        self.theme = None
        
        self.images = []
        self.counter = 0
        
        self.windowWidth = None
        self.windowHeight = None
        
        self.isrunning = True
        
        self.img = None
        
        self.windowapp = WindowApp(self)
        self.windowapp.start()
       
        self.inputprocessor = InputProcessor(self)
        self.renderer = ScreenRenderer(self)
        
        self.pluginmanager = PluginManager(tools.getResource("plugins"))
        self.pluginmanager.addDirectory(os.path.join(tools.getHome(), ".picsortPlugins"))
        self.pluginmanager.loadPlugins()
        
        self.showHelp = True
        self.showNumbers = True
       
        for plugin in self.pluginmanager.plugins:
            try:
                self.pluginmanager.plugins[plugin].init(self)
            except Exception, e:
                self.logger.warn("Error while init for: " + plugin)
                self.logger.warn(plugin + " -> " + str(e))
        
    
    def startRender(self):
        self.updateImageList()
        self.loadAndScaleImage(self.images[self.counter])
        self.windowapp.mainWindow.Hide()
        self.renderer.start()
        

    def changeTheme(self):
        self.windowapp.openThemeWindow()

        
    def closeWindow(self):
        self.isrunning = False
        self.windowapp.close();

        
    def updateImageList(self):    
        if self.sourceDir == None:
            raise ValueError("source directory is none")
    
        self.images = []
    
        for f in os.listdir(self.sourceDir):
            if f.lower().endswith(".jpg"):
                self.images.append(os.path.join(self.sourceDir, f.rstrip()))


    def loadAndScaleImage(self, imgPath):
        self.img = loadImage(imgPath)
        self.img = resizeImage(self.img, (self.windowWidth, self.windowHeight))


    def getNextImage(self):
        self.counter += 1
        
        if self.counter >= len(self.images):
            self.counter = 0
        
        self.loadAndScaleImage(self.images[self.counter])
    
    
    def copyImage(self):
        
        curImage = self.images[self.counter]
        target = os.path.join(self.targetDir, self.theme)

        filename =  os.path.basename(curImage)

        if not os.path.exists(target):
            os.makedirs(target)

        target = os.path.join(target, filename)
        
        shutil.copy2(curImage, target)
    
    def getPreviousImage(self):
        self.counter -= 1

        if self.counter < 0:
            self.counter = len(self.images)-1
            
        self.loadAndScaleImage(self.images[self.counter])
    
        
        