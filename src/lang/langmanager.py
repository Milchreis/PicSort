# -*- coding: utf-8 -*-

'''
@author: nick
'''

from core.pluginmanager import PluginManager

ENGLISH = "en"
GERMAN = "de"

class LanguageManager():

    def __init__(self):
        
        self.pm = PluginManager('lang')
        self.pm.loadPlugins()
        
        self.language = self.pm.getPlugin("en")

    def setLanguage(self, languagekey):
        self.language = self.pm.getPlugin(languagekey)

    def get(self, key):
        if self.language.map[key] == None:
            return key
        else:
            return self.language.map[key]


__langmanager = LanguageManager()

def setLanguage(languagekey):
    global __langmanager
    return __langmanager.set(languagekey)


def get(key):
    global __langmanager
    return __langmanager.get(key)
