# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventasBuscarECpRuB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import db
import ui_ventasBuscarVariacion

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, result):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(511, 194)
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 100, 221, 70))
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.select)
        font1 = QFont()
        font1.setPointSize(18)
        font2 = QFont()
        font2.setPointSize(22)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 20, 451, 51))
        self.comboBox_2.setFont(font1)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 100, 221, 70))
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.cancel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()
        for i in range(len(result)):
            self.comboBox_2.addItem(result[i][1])

    def select(self):
        self.cursor.execute(f"SELECT * FROM producto WHERE nombre = \'{self.comboBox_2.currentText()}\';")
        self.cursor.execute(f"SELECT * FROM variacion_producto WHERE id_producto = {self.cursor.fetchone()[0]};")
        self.ventasBuscarVariacion = ui_ventasBuscarVariacion.ventasBuscarVariacion(self.cursor.fetchall())
        self.ventasBuscarVariacion.show()
        self.mainWindow.close()
    
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

    def cancel(self):
        self.mainWindow.close()

class ventasBuscar(QMainWindow):
    def __init__(self, result):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, result)