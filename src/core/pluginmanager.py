# -*- coding: utf-8 -*-

'''
@author: nick
'''

import imp
import os
import logging

class PluginManager():

    def __init__(self, directory):
        self.pluginDirs = [directory]
        self.plugins = {}
        self.logger = logging.getLogger('picsort')

    def addDirectory(self, directory):
        self.pluginDirs.append(directory)
    
    
    def getPlugin(self, name):
        return self.plugins[name]
    
    
    def listPlugins(self):
        plugins = []
        
        for directory in self.pluginDirs:
            if os.path.exists(directory):
                for f in os.listdir(directory):
                    if f.endswith(".py") and not f == "__init__.py":
                        plugins.append(os.path.join(directory, f))
            else:
                self.logger.warn("directory not exists: {}".format(directory))
            
        return plugins


    def loadPlugins(self):
    
        for plugin in self.listPlugins():
            try:
                name, _ = os.path.splitext(os.path.split(plugin)[1])
            
                submodule = imp.load_source(name, plugin)
                self.plugins[name] = submodule
            except Exception, e:
                self.logger.error(e)
