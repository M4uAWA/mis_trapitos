# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productosVariacionBSydIs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from datetime import date

import db
import ui_productoVariacionAgregar
import ui_productoVariacionModificar
import ui_productoVariacionBorrar

class Ui_MainWindow(object):

    product_id = None

    def setupUi(self, MainWindow,product_id):

        self.product_id = product_id

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 41, 51))
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(750, 40, 291, 151))
        font = QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setPixmap(QPixmap(u"img\\s.png"))
        self.label_3.setScaledContents(True)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 90, 461, 50))
        font1 = QFont()
        font1.setPointSize(20)
        self.lineEdit_2.setFont(font1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem01 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem01)
        __qtablewidgetitem02 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem02)
        __qtablewidgetitem03 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem03)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 210, 1021, 481))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(16)
        self.tableWidget.setFont(font2)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(169)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        font3 = QFont()
        font3.setPointSize(22)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(550, 90, 181, 51))
        self.pushButton_7.clicked.connect(self.addItemVariation)
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButton_7.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

        self.setItems()

        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,50)
        self.tableWidget.setColumnWidth(3,50)

        self.tableWidget.cellClicked.connect(self.handleCell)
    # setupUi
        
    def handleCell(self,row,column):
        if column < 3:
            if self.lineEdit_2.text() != "":
                self.cursor.execute(f"SELECT * FROM variacion_producto WHERE talla LIKE \'%{self.lineEdit_2.text()}%\' AND id_producto = {self.product_id};")
            else:
                self.cursor.execute(f"SELECT * FROM variacion_producto WHERE id_producto = {self.product_id};")
            variations = self.cursor.fetchall()
            if column == 0:
                self.deleteItemVariation(variations[row][0])
            elif column == 1:
                self.modifyItemVariation(variations[row][0])
            elif column == 2:
                self.itemVariationReport(variations[row][0])

    def deleteItemVariation(self,productVariation_id):
        self.variacionBorrar = ui_productoVariacionBorrar.productoVariacionBorrar(productVariation_id)
        self.variacionBorrar.show()
    
    def modifyItemVariation(self,productVariation_id):
        self.variacionModificar = ui_productoVariacionModificar.productoVariacionModificar(self.product_id,productVariation_id)
        self.variacionModificar.show()

    def itemVariationReport(self,productVariation_id):
        with open("Reporte\\Reporte.txt", "w") as f:
            f.write(f"Fecha: {date.today()}")
            f.write("\nVariacion: ")
            f.write("\nid_variacion, talla, color, stock, id_producto")
            self.cursor.execute(f"SELECT * FROM variacion_producto WHERE id_variacion = {productVariation_id}")
            f.write("\n"+str(self.cursor.fetchone()))
                   
    def addItemVariation(self):
        self.variacionAgregar = ui_productoVariacionAgregar.productoVariacionAgregar(self.product_id)
        self.variacionAgregar.show()
        
    def setItems(self):
        if self.lineEdit_2.text() != "":
            self.cursor.execute(f"SELECT * FROM variacion_producto WHERE talla LIKE \'%{self.lineEdit_2.text()}%\' AND id_producto = {self.product_id};")
        else:
            self.cursor.execute(f"SELECT * FROM variacion_producto WHERE id_producto = {self.product_id};")
        variations = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(variations))
        if len(variations) > 0:
            self.tableWidget.setColumnCount(len(variations[0])+3)
            for i in range(len(variations)):

                self.tableWidget.setItem(i,0,QTableWidgetItem("🗑️"))
                self.tableWidget.setItem(i,1,QTableWidgetItem("✏️"))
                self.tableWidget.setItem(i,2,QTableWidgetItem("📊"))

                for j in range(len(variations[i])):
                    self.tableWidget.setItem(i,j+3,QTableWidgetItem(str(variations[i][j])))
        QTimer.singleShot(3000, self.setItems)

    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.lineEdit_2.setText("")
        ___qtablewidgetitem01 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem01.setText(QCoreApplication.translate("MainWindow", u"Borrar", None));
        ___qtablewidgetitem02 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem02.setText(QCoreApplication.translate("MainWindow", u"Modificar", None));
        ___qtablewidgetitem03 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem03.setText(QCoreApplication.translate("MainWindow", u"Reporte", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Talla", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Color", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"🔍", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Agregar variaci\u00f3n", None))

    # retranslateUi

class productosVariacion(QMainWindow):
    def __init__(self,product_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,product_id)