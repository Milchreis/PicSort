# -*- coding: utf-8 -*-

'''
@author: nick
'''

import logging
import optparse
import os
import exifread
from core.model import AppModel
from core import tools

if __name__ == '__main__':

    # Set up the logger
    # ============================================================
    logger = logging.getLogger('picsort')
    logger.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(ch)
    
    fh = logging.FileHandler(tools.getResource('../logging.log'))
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(fh)
    
    appModel = AppModel()
    
    # Set up the OptionParser
    # ============================================================
    parser = optparse.OptionParser('usage: PicSort [<sourceDirectory> [<targetDirectory>]]')
    (options, args) = parser.parse_args()
    
    if len(args) > 0:
        if len(args) >= 1 and os.path.exists(args[0]):
            appModel.sourceDir = args[0]
    
        if len(args) >= 2 and os.path.exists(args[1]):
            appModel.targetDir = args[1]

        appModel.windowapp.mainWindow.Hide()
        appModel.startRender()
   

    