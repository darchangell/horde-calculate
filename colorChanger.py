# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color-change.ui'
#
# Created: Sat Dec  7 22:19:08 2013
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(335, 326)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #setup the palette to give a grey background.
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)

        self.color_1 = QtWidgets.QPushButton(self.centralwidget)
        self.color_1.setGeometry(QtCore.QRect(20, 60, 50, 50))
        self.color_1.setPalette(palette)
        self.color_1.setAutoFillBackground(True)
        self.color_1.setFlat(False)
        self.color_1.setObjectName("color_1")
        
        self.color_2 = QtWidgets.QPushButton(self.centralwidget)
        self.color_2.setGeometry(QtCore.QRect(80, 60, 50, 50))
        self.color_2.setPalette(palette)
        self.color_2.setAutoFillBackground(True)
        self.color_2.setFlat(False)
        self.color_2.setObjectName("color_2")

        self.color_3 = QtWidgets.QPushButton(self.centralwidget)
        self.color_3.setGeometry(QtCore.QRect(140, 60, 50, 50))
        self.color_3.setPalette(palette)
        self.color_3.setAutoFillBackground(True)
        self.color_3.setFlat(False)
        self.color_3.setObjectName("color_3")

        self.color_4 = QtWidgets.QPushButton(self.centralwidget)
        self.color_4.setGeometry(QtCore.QRect(200, 60, 50, 50))
        self.color_4.setPalette(palette)
        self.color_4.setAutoFillBackground(True)
        self.color_4.setFlat(False)
        self.color_4.setObjectName("color_4")

        self.color_5 = QtWidgets.QPushButton(self.centralwidget)
        self.color_5.setGeometry(QtCore.QRect(260, 60, 50, 50))
        self.color_5.setPalette(palette)
        self.color_5.setAutoFillBackground(True)
        self.color_5.setFlat(False)
        self.color_5.setObjectName("color_5")

        self.color_6 = QtWidgets.QPushButton(self.centralwidget)
        self.color_6.setGeometry(QtCore.QRect(260, 120, 50, 50))
        self.color_6.setPalette(palette)
        self.color_6.setAutoFillBackground(True)
        self.color_6.setFlat(False)
        self.color_6.setObjectName("color_6")

        self.color_7 = QtWidgets.QPushButton(self.centralwidget)
        self.color_7.setGeometry(QtCore.QRect(20, 120, 50, 50))
        self.color_7.setPalette(palette)
        self.color_7.setAutoFillBackground(True)
        self.color_7.setFlat(False)
        self.color_7.setObjectName("color_7")

        self.color_8 = QtWidgets.QPushButton(self.centralwidget)
        self.color_8.setGeometry(QtCore.QRect(140, 120, 50, 50))
        self.color_8.setPalette(palette)
        self.color_8.setAutoFillBackground(True)
        self.color_8.setFlat(False)
        self.color_8.setObjectName("color_8")

        self.color_9 = QtWidgets.QPushButton(self.centralwidget)
        self.color_9.setGeometry(QtCore.QRect(200, 120, 50, 50))
        self.color_9.setPalette(palette)
        self.color_9.setAutoFillBackground(True)
        self.color_9.setFlat(False)
        self.color_9.setObjectName("color_9")

        self.color_10 = QtWidgets.QPushButton(self.centralwidget)
        self.color_10.setGeometry(QtCore.QRect(80, 120, 50, 50))
        self.color_10.setPalette(palette)
        self.color_10.setAutoFillBackground(True)
        self.color_10.setFlat(False)
        self.color_10.setObjectName("color_10")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.connectButtonsToColor()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def connectButtonsToColor(self):
        for child in self.centralwidget.findChildren(QtWidgets.QPushButton):
            #print(child.objectName())
            child.clicked.connect(self.getColorDialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.color_1.setText(_translate("MainWindow", "Color1"))
        self.color_2.setText(_translate("MainWindow", "Color2"))
        self.color_3.setText(_translate("MainWindow", "Color3"))
        self.color_4.setText(_translate("MainWindow", "Color4"))
        self.color_5.setText(_translate("MainWindow", "Color5"))
        self.color_6.setText(_translate("MainWindow", "Color10"))
        self.color_7.setText(_translate("MainWindow", "Color6"))
        self.color_8.setText(_translate("MainWindow", "Color8"))
        self.color_9.setText(_translate("MainWindow", "Color9"))
        self.color_10.setText(_translate("MainWindow", "Color7"))
        
    def getColorDialog(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid(): #"Color" in self.centralwidget.sender().objectName():
            clicked = self.centralwidget.sender()
            clicked.setStyleSheet("background-color:%s" % (str(color.name())))

#             palette = QtGui.QPalette(clicked.palette())
#             brush = QtGui.QBrush(color)
#             brush.setStyle(QtCore.Qt.SolidPattern)
#             palette.setColor(QtGui.QPalette.Button,color)
#             palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
#             palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
#             palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
#             clicked.setPalette(palette)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    mainWindow = Ui_MainWindow()
    mainWindow.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
