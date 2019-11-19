# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        '''self.lineas = QtGui.QPlainTextEdit(self.centralwidget)
        self.lineas.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineas.setReadOnly(True)
        self.lineas.setObjectName("lineas")
        self.gridLayout.addWidget(self.lineas, 0, 0, 1, 1)'''
        self.entrada = QtGui.QPlainTextEdit(self.centralwidget)
        self.entrada.setObjectName("entrada")
        self.gridLayout.addWidget(self.entrada, 0, 1, 1, 1)
        self.salida = QtGui.QPlainTextEdit(self.centralwidget)
        self.salida.setMaximumSize(QtCore.QSize(16777215, 80))
        self.salida.setReadOnly(True)
        self.salida.setObjectName("salida")

        self.gridLayout.addWidget(self.salida, 1, 0, 1, 2)
        self.validar = QtGui.QPushButton(self.centralwidget)
        self.validar.setObjectName("validar")
        self.gridLayout.addWidget(self.validar, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.validar.setText(_translate("MainWindow", "Validar"))