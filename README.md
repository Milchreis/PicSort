![alt text](https://31.media.tumblr.com/bb9e67b5816527cfbb1c13df221fd0c5/tumblr_inline_n2y0y7iVgi1r10owe.png "Logo")

PicSort is a simple program to view images in a diashow-like fullscreen. Moreover is provides functions for organize the images while the first look. The main goal of this tool is to get your best images from your camera to your harddrive in an easy way. The tool organize the images in different categories (named 'themes'). Set up a theme and choose the images best images for the copy process.

Before you could see your images you have to set up the source and the destination directory. Further you just navigate thru your image pool or you define a theme. Until now, the theme is active. With `spacebar` you copy the picture into the destination directory with a subdirectory of your theme. In that way, you are able to look for your new pictures, f.e. on you camera or smartphone and sort them in the same time. Fast, clean and easy.

This project is in development.

Additional the program includes a lot of functions which are defines as plugins. You can program your own plugins for this tool without knowing the main core code. For more informations look [here](https://github.com/MilchReis/PicSort#plugins "plugin-section").


![alt text](http://abload.de/img/screen16srx.png "Sceenshot")

## Shortcuts ##

Press the F1 key in fullscreen to show the full shortcut information's. The following list shows the basic keys.

 - `Left` and `Right` to show the previous or next picture
 - `CTRL` to open up the dialog to input the theme
 - `Spacebar` to copy the current picture to destination (like "destination/theme/img.jpg")

## Download / Build ##

The simplest way to run picsort is to download the build for your platform. The latetest builds of the project is hosted on github. Feel free to [download](https://github.com/MilchReis/PicSort/tree/master/bin "download-address") it. Until now windows and linux are supported.

If you want to see or manipulate the code you can fork or download it. To run the code you have to install the following packages:

 - python (2.7)
 - wxpython
 - pygame
 - exifread

With the command `python picsort/src/main.py` you start the program. To build your own binary (standalone file) you can download the pyinstaller and put it into the build-directory.
After that run the build-<...>.sh file.

## Plugins

PicSort includes a simple plugin-system to load individual plugins to extend the functionality. A lot of functions are also written as build-in plugins. This plugins are placed in the plugins-package. Look at these files to see how a plugin is structured. For programm your own plugin take the dummyplugin-file. 

If you want to program a plugin you don't need the source code. Place your plugin file in this directory `/home/<yourname>/.picsortPlugins`. 

## Commandline Interface

Often the tool is used with the same source and destination directory. Therefore picsort provides a commandline interface. On start you are able to put this informations in commandline and the first little window will not shown. In that way you can write a script to start the program directly with your image base.

usage: PicSprt /path/to/source /path/to/target

## Future builds ##
The following list includes the changes in the current code base to the lastest version. The next build-release will contains the following changes.

 - automatic language detection and changing by os defaults.

## Changelog ##

#### Version 0.1 ####

 - view images in fullscreen
 - navigate thru the image pool
 - set up themes and copy images
 - build-in plugins
 	 - auto rotating pictures by exif information
 	 - minimap (shows the previous and next images)
 	 - delete image (provides the deletion of the source file)
 	 - image numbers (shows the current number of the image and the maximum)
 	 - magnify (show a subarea of the image in the original size)

