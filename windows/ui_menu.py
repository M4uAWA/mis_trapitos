# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menunBxDwP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import ui_clientes
import ui_productos
import ui_proveedores
import ui_venta
import db

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,id):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        self.id = id
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 401, 31))
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        font1 = QFont()
        font1.setPointSize(16)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(860, 20, 201, 121))
        self.label_3.setFont(font)
        self.label_3.setPixmap(QPixmap(u"img\\s.png"))
        self.label_3.setScaledContents(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(700, 160, 291, 251))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.clicked.connect(self.goToVenta)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(400, 160, 291, 251))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.clicked.connect(self.goToClientes)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(100, 430, 291, 251))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.clicked.connect(self.goToProveedores)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(100, 160, 291, 251))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.clicked.connect(self.goToProductos)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(400, 430, 591, 251))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.clicked.connect(self.exitMenu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM empleado WHERE id_empleado = {id};")
        accountName = cursor.fetchall()[0][1]
        self.label.setText(f"Bienvenid@: {accountName}")
        cursor.execute(f"SELECT * FROM administrador WHERE id_empleado = {id};")
        account = cursor.fetchall()
        if len(account) == 0:
            self.pushButton_3.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
        cursor.close()
        connection.close()

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    
    def goToClientes(self):
        self.clientes = ui_clientes.clientes()
        self.clientes.show()
    def goToVenta(self):
        self.venta = ui_venta.venta(self.id)
        self.venta.show()
    def goToProveedores(self):
        self.proveedores = ui_proveedores.proveedores()
        self.proveedores.show()
    def goToProductos(self):
        self.productos = ui_productos.productos()
        self.productos.show()
    def exitMenu(self):
        self.mainWindow.close()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bienvenid@: ", None))
        self.label_3.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Gestionar\n"
"clientes", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Gestionar\n"
"proveedores", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Gestionar\n"
"productos", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Salir de\n"
"la aplicaci\u00f3n", None))
    # retranslateUi   
    
class menu(QMainWindow):
    def __init__(self,id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,id)