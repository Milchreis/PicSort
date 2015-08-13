# -*- coding: utf-8 -*-

'''
@author: nick
'''

def getResource(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """

    import sys
    import os

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def getHome():
    from os.path import expanduser
    return expanduser("~")