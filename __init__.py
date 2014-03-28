# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Unique_values_saver
                                 A QGIS plugin
 It grabs unique values froma a vector layer and saves all the features corresponding to each unique value as a new shapefile with geomentry type and attributes coming from source vector file.
                             -------------------
        begin                : 2014-03-28
        copyright            : (C) 2014 by Giuseppe De Marco Pienocampo
        email                : demarco.giuseppe@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Unique_values_saver class from file Unique_values_saver
    from unique_values_saver import Unique_values_saver
    return Unique_values_saver(iface)
