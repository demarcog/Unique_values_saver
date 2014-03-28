# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Unique_values_saver
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os.path
import os
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from unique_values_saverdialog import Unique_values_saverDialog
import pdb


class Unique_values_saver:
    
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'unique_values_saver_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = Unique_values_saverDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/unique_values_saver/icon.png"),
            u"Unique_values_saver", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Unique_values_saver", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Unique_values_saver", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        #---------custom functions begin
    
     #checks if layer are vector type
    def checkvector(self):
        count = 0
        for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if layer.type() == QgsMapLayer.VectorLayer:
                count += 1
        return count
    
    #gets output path os independently
    def get_dir(self):
        if os.path.exists(os.getenv("HOME")+'/workpath'):
            fpath = open(os.getenv("HOME")+'/workpath', 'r')
            read_path = fpath.read()
            fpath.close
        else:
            read_path ="."
            dirname = QFileDialog.getExistingDirectory(self.dlg, "Select the Directory for your Plugin", ".")
            if len(dirname)==0:
                QMessageBox.warning(None, "Warning","No folder selected, please select one!")
                dirname=None
                return dirname
            else:
                return dirname
        return dirname

    def get_layer(self):
        self.dlg.ui.Layer.clear()
        self.dlg.ui.txt.clear()
        self.dlg.ui.progressbar.setValue(0)
        for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if layer.type() == QgsMapLayer.VectorLayer:
                self.dlg.ui.Layer.addItem(layer.name())
                #update other comboboxes
                self.get_field()
        return
    
    def get_field(self):
        #clear comboboxes and linedits
        self.dlg.ui.Field.clear()
        self.dlg.ui.txt.clear()
        if self.dlg.ui.Layer.currentText() != "":
            layername = self.dlg.ui.Layer.currentText()
            for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
                if selectlayer.name() == layername:
                    #removed for API 2 compatibility removing counter and iteritems()
                    #for index, field in selectlayer.dataProvider().fields().iteritems():
                    for field in selectlayer.dataProvider().fields():
                        self.dlg.ui.Field.addItem(field.name())
        return
                        
                                
    def choose_field(self):
        fieldname = self.dlg.ui.Field.currentText()
        if fieldname != "":
            return fieldname
        else:
            QMessageBox.warning(None, "Warning","No field selected, please select one!")
            return
        
    def choose_layer(self):
        layername = self.dlg.ui.Layer.currentText()
        if layername != "":
            return layername
        else:
            QMessageBox.warning(None, "Warning","No layer selected, please select one!")
            return
        return
    
    def uniquevalues (self):
        self.dlg.ui.txt.clear()
        lay = self.choose_layer()
        fie = self.choose_field()
        uniquevalues = []
        progress = self.dlg.ui.progressbar
        progress.setValue(0)
        if ((lay != "") and (fie != "")):
            for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
                if layer.name() == lay:
                    uniqueprovider = layer.dataProvider()
                    fields = uniqueprovider.fields()
                    dir = self.get_dir()
                    if dir==None:
                        QMessageBox.information(None, "Shapesaver","No output directory given: aborting...")
                        return
                    else:
                        QMessageBox.information(None, "Shapesaver","output dir : "+str(dir))
                        for field in fields:
                            if field.name() == fie:
                                id = fields.indexFromName(fie)
                                uniquevalues=uniqueprovider.uniqueValues(id)
                                progress.setMaximum(len(uniquevalues))
                                if uniquevalues:
                                    for uv in uniquevalues:
                                        progress.setValue(progress.value()+1)
                                        for field in fields:
                                            if field.name() == fie:
                                                selectList =[]
                                                for f in layer.getFeatures():
                                                    attrs = f.attributes()
                                                    double = ""#checks for duplicates in case of null attr value
                                                    for attr in attrs:
                                                        if str(attr) == str(uv):
                                                            if str(f)!= str(double):#checks for duplicates in case of null attr value
                                                                selectList.append(f.id())
                                                                double = f 
                                                # writes matching features in a new shapefile
                                                if selectList:
                                                #selectlayer.setSelectedFeatures(selectList)
                                                    savname = field.name()+str(uv)+".shp"
                                                    savename = os.path.join(dir, savname)
                                                    self.dlg.ui.txt.append("Saving "+str(savename))
                                                    if len(savename) <= 0:
                                                        QMessageBox.information(None, "Shapesaver","No output filename given")
                                                        return
                                                    else:
                                                        outfile = QgsVectorFileWriter(savename, "utf-8", fields, uniqueprovider.geometryType(), uniqueprovider.crs())
                                                        for i in range(len(selectList)):
                                                            for sf in layer.getFeatures():
                                                                if sf.id() == selectList[i]:
                                                                    attributes = sf.attributes()
                                                                    geometry = sf.geometry()
                                                                    feature = QgsFeature()
                                                                    feature.setAttributes(attributes)
                                                                    feature.setGeometry(geometry)
                                                                    outfile.addFeature(feature)
                                                    selectList =[]
        return
    
    def exit(self):
        #after exiting and reloading the plugin
        QObject.disconnect(self.dlg.ui.Layer, SIGNAL("activated(QString)"), self.get_field)
        QObject.disconnect(self.dlg.ui.Layer, SIGNAL("currentIndexChanged(QString)"),self.get_field)
        QObject.disconnect(self.dlg.ui.Field, SIGNAL("currentIndexChanged(QString)"), self.get_field)
        QObject.disconnect(self.dlg.ui.EXIT, SIGNAL("clicked(bool)"), self.exit)
        QMessageBox.information(None, "Exiting ...","Goodbye!")
        self.dlg.close()
        return
    
    
    #---------Custom functions end

    # run method that performs all the real work
    def run(self):
        # Run the dialog event loop
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        if self.checkvector() < 1:
            QMessageBox.critical(None, "Critical","No vector layers \n Please load some, then reload plugin")
            return
        else:
            #self.get_field()
            #pyqtRemoveInputHook()
            #pdb.set_trace()
            #Connect to change in layer combobox and field combobox and execute
            #information retrieving procedures
            self.get_layer()
            self.get_field()
            QObject.connect(self.dlg.ui.Layer, SIGNAL("activated(QString)"), self.get_field)
            QObject.connect(self.dlg.ui.Layer, SIGNAL("currentIndexChanged(QString)"), self.get_field)
            QObject.connect(self.dlg.ui.Save, SIGNAL("clicked(bool)"), self.uniquevalues)
            QObject.connect(self.dlg.ui.EXIT, SIGNAL("clicked(bool)"), self.exit)
            # show the dialog
            self.dlg.show()
            #self.dlg.exec_()
            # See if OK was pressed
            # do something useful (delete the line containing pass and
            # substitute with your code)

