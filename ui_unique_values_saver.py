# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_unique_values_saver.ui'
#
# Created: Thu Mar 20 04:11:08 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Unique_values_saver(object):
    def setupUi(self, Unique_values_saver):
        Unique_values_saver.setObjectName(_fromUtf8("Unique_values_saver"))
        Unique_values_saver.resize(436, 418)
        Unique_values_saver.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label = QtGui.QLabel(Unique_values_saver)
        self.label.setGeometry(QtCore.QRect(20, 90, 311, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Unique_values_saver)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 311, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Layer = QtGui.QComboBox(Unique_values_saver)
        self.Layer.setGeometry(QtCore.QRect(20, 120, 391, 27))
        self.Layer.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Layer.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Layer.setAcceptDrops(False)
        self.Layer.setAutoFillBackground(False)
        self.Layer.setModelColumn(0)
        self.Layer.setObjectName(_fromUtf8("Layer"))
        self.Field = QtGui.QComboBox(Unique_values_saver)
        self.Field.setGeometry(QtCore.QRect(20, 180, 391, 27))
        self.Field.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Field.setAcceptDrops(False)
        self.Field.setMinimumContentsLength(0)
        self.Field.setObjectName(_fromUtf8("Field"))
        self.Save = QtGui.QPushButton(Unique_values_saver)
        self.Save.setGeometry(QtCore.QRect(20, 220, 144, 44))
        self.Save.setObjectName(_fromUtf8("Save"))
        self.EXIT = QtGui.QPushButton(Unique_values_saver)
        self.EXIT.setGeometry(QtCore.QRect(310, 230, 85, 27))
        self.EXIT.setObjectName(_fromUtf8("EXIT"))
        self.progressbar = QtGui.QProgressBar(Unique_values_saver)
        self.progressbar.setGeometry(QtCore.QRect(20, 270, 381, 25))
        self.progressbar.setProperty("value", 0)
        self.progressbar.setObjectName(_fromUtf8("progressbar"))
        self.txt = QtGui.QTextBrowser(Unique_values_saver)
        self.txt.setGeometry(QtCore.QRect(20, 310, 391, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.txt.setFont(font)
        self.txt.setObjectName(_fromUtf8("txt"))
        self.label_5 = QtGui.QLabel(Unique_values_saver)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 411, 71))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.frame = QtGui.QFrame(Unique_values_saver)
        self.frame.setGeometry(QtCore.QRect(10, 10, 411, 81))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(30, 10, 51, 51))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MultiEdit/pienocampo.png")))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.retranslateUi(Unique_values_saver)
        QtCore.QMetaObject.connectSlotsByName(Unique_values_saver)

    def retranslateUi(self, Unique_values_saver):
        Unique_values_saver.setWindowTitle(_translate("Unique_values_saver", "Unique_values_saver", None))
        self.label.setText(_translate("Unique_values_saver", "LAYER", None))
        self.label_2.setText(_translate("Unique_values_saver", "FIELD", None))
        self.Save.setText(_translate("Unique_values_saver", "Save unique values \n"
" as shapefile", None))
        self.EXIT.setText(_translate("Unique_values_saver", "EXIT", None))
        self.label_5.setText(_translate("Unique_values_saver", "UNIQUE_VALUES_SAVER 0.1  \n"
"(C) 2014 by Giuseppe De Marco\n"
" www.pienocampo.it", None))

import resources_rc
