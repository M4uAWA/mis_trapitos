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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, result):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(511, 274)
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 180, 221, 70))
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.select)
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(260, 100, 221, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.spinBox_2.setFont(font1)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setMinimum(1)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 100, 221, 51))
        font2 = QFont()
        font2.setPointSize(22)
        self.label_12.setFont(font2)
        self.label_12.setFrameShape(QFrame.Box)
        self.label_12.setFrameShadow(QFrame.Sunken)
        self.label_12.setLineWidth(1)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 20, 451, 51))
        self.comboBox_2.setFont(font1)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 180, 221, 70))
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.cancel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()
        self.result = result
        for i in range(len(result)):
            self.comboBox_2.addItem(str(result[i]))
        self.updateButton()
        self.comboBox_2.currentTextChanged.connect(self.updateButton)

    def updateButton(self):
        if tuple(self.comboBox_2.currentText())[3] == 0:
            self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(True)

    def select(self):
        self.cursor.execute(f"SELECT * FROM producto WHERE id_producto = {eval(self.comboBox_2.currentText())[4]}")
        producto = self.cursor.fetchone()
        self.cursor.execute("SELECT max(id_venta) FROM venta;")
        sale_id = self.cursor.fetchone()[0]
        self.cursor.execute(f"INSERT INTO detalle_articulo(cantidad,precio_unitario,descuento_aplicado,id_venta,id_variacion) VALUES ({self.spinBox_2.value()},{float(producto[3]) - (float(producto[3]) * (producto[5]/100))},{producto[5]},{sale_id},{eval(self.comboBox_2.currentText())[0]})")
        self.mainWindow.close()
    
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

    def cancel(self):
        self.mainWindow.close()

class ventasBuscarVariacion(QMainWindow):
    def __init__(self, result):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, result)