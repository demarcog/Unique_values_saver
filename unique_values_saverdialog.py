# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Unique_values_saverDialog
                                 A QGIS plugin
 it grabs unique values froma a vector layer and 
#saves all the features corresponding to each unique value as a new shapefile
#with geomentry type and attributes coming from source vector file.
                             -------------------
        begin                : 2014-03-16
        copyright            : (C) 2014 by Giuseppe De Marco
        email                : info@pienocampo.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_unique_values_saver import Ui_Unique_values_saver
# create the dialog for zoom to point


class Unique_values_saverDialog(QtGui.QDialog, Ui_Unique_values_saver):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
	self.ui = Ui_Unique_values_saver()
        self.ui.setupUi(self)
