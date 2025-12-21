# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-Copyright-Text: 2020 Daniel Wood
# SPDX-FileNotice: Part of the Feeds & Speeds addon.


import FreeCADGui
from PySide import QtGui
import CAMFeedsAndSpeedsGui
import os

__dir__ = os.path.dirname(__file__)
iconPath = os.path.join( __dir__, 'Icons' )

def getIcon(iconName):
     return os.path.join( iconPath , iconName)

def updateMenu(workbench):

    if workbench == 'CAMWorkbench':
    
        print('Feeds and Speeds Addon loaded:', workbench)

        mw = FreeCADGui.getMainWindow()
        addonMenu = None

        # Find the main path menu
        pathMenu = mw.findChild(QtGui.QMenu, "&CAM")

        for menu in pathMenu.actions():
            if menu.text() == "CAM Addons":
                # create a new addon menu
                addonMenu = menu.menu()
                break

        if addonMenu is None:
            addonMenu = QtGui.QMenu("CAM Addons")
            addonMenu.setObjectName("CAM_Addons")

            # Find the dressup menu entry
            dressupMenu = mw.findChild(QtGui.QMenu, "Path Dressup")

            #addonMenu.setTitle("CAM Addons")
            pathMenu.insertMenu(dressupMenu.menuAction(), addonMenu)

        # create an action for this addon
        action = QtGui.QAction(addonMenu)
        action.setText("Feeds and Speeds")
        action.setIcon(QtGui.QPixmap(getIcon('CAM_FeedsAndSpeeds.svg')))
        action.setStatusTip("Check Feeds and Speeds")
        action.triggered.connect(CAMFeedsAndSpeedsGui.Show)

        # append this addon to addon menu
        addonMenu.addAction(action)

FreeCADGui.getMainWindow().workbenchActivated.connect(updateMenu)
