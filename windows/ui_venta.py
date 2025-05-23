# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventamuimxN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import db
import ui_ventasError
import ui_ventasBuscar
from datetime import date

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, id):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 718)
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(420, 650, 181, 51))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.clicked.connect(self.search)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 650, 391, 50))
        font1 = QFont()
        font1.setPointSize(20)
        self.lineEdit_2.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(620, 570, 431, 61))
        font2 = QFont()
        font2.setPointSize(22)
        self.label_5.setFont(font2)
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_5.setLineWidth(1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 20, 581, 561))
        font3 = QFont()
        font3.setPointSize(14)
        self.tableWidget.setFont(font3)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(115)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 600, 201, 31))
        self.radioButton.setFont(font3)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(340, 600, 251, 31))
        self.radioButton_2.setFont(font3)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(620, 20, 431, 51))
        self.label_6.setFont(font2)
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setFrameShadow(QFrame.Sunken)
        self.label_6.setLineWidth(1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(620, 80, 141, 51))
        self.label_7.setFont(font2)
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setFrameShadow(QFrame.Sunken)
        self.label_7.setLineWidth(1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(620, 140, 431, 51))
        self.label_8.setFont(font2)
        self.label_8.setFrameShape(QFrame.Box)
        self.label_8.setFrameShadow(QFrame.Sunken)
        self.label_8.setLineWidth(1)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(770, 80, 281, 51))
        font4 = QFont()
        font4.setPointSize(18)
        self.comboBox.setFont(font4)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(620, 200, 431, 351))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.radioButton_3 = QRadioButton(self.frame)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(60, 30, 101, 41))
        self.radioButton_3.setFont(font3)
        self.radioButton_3.toggled.connect(self.card)
        self.radioButton_4 = QRadioButton(self.frame)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(260, 30, 111, 41))
        self.radioButton_4.setFont(font3)
        self.radioButton_4.toggled.connect(self.cash)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(190, 120, 221, 50))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(190, 200, 221, 50))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(190, 280, 221, 50))
        self.lineEdit_5.setFont(font1)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 120, 161, 51))
        self.label_9.setFont(font2)
        self.label_9.setFrameShape(QFrame.Box)
        self.label_9.setFrameShadow(QFrame.Sunken)
        self.label_9.setLineWidth(1)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 200, 161, 51))
        self.label_10.setFont(font2)
        self.label_10.setFrameShape(QFrame.Box)
        self.label_10.setFrameShadow(QFrame.Sunken)
        self.label_10.setLineWidth(1)
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 280, 161, 51))
        self.label_11.setFont(font2)
        self.label_11.setFrameShape(QFrame.Box)
        self.label_11.setFrameShadow(QFrame.Sunken)
        self.label_11.setLineWidth(1)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(620, 650, 431, 51))
        self.pushButton_6.setFont(font)
        self.pushButton_6.clicked.connect(self.makeSale)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget.setColumnWidth(0,50)

        self.id = id
        self.saleMade = False
        self.connection = db.connect()
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM empleado WHERE id_empleado = {self.id};")
        empleado = self.cursor.fetchone() 
        self.label_6.setText(f"Empleado: {empleado[1]}")
        self.cursor.execute(f"SELECT * FROM cliente;")
        client = self.cursor.fetchall()
        if len(client) > 0:
            for i in range(len(client)):
                self.comboBox.addItem(client[i][2])
        self.radioButton_4.setChecked(True)
        self.cash()
        self.radioButton_2.setChecked(True)
        self.cursor.execute(f"SELECT * FROM cliente WHERE nombre = \'{self.comboBox.currentText()}\'")
        client_id = self.cursor.fetchone()[0]
        self.cursor.execute(f"INSERT INTO venta (fecha_venta,total,metodo_de_pago,id_cliente,id_empleado) VALUES (\'{date.today()}\',NULL,NULL,{client_id},{self.id})")
        self.comboBox.currentTextChanged.connect(self.updateClient)

        self.setItems()

        self.tableWidget.cellClicked.connect(self.handleCell)

    # setupUi
        
    def handleCell(self,row,column):
        if column < 1:
            self.cursor.execute("SELECT max(id_venta) FROM venta;")
            sale_id = self.cursor.fetchone()[0]
            self.cursor.execute(f"SELECT * FROM detalle_articulo WHERE id_venta = {sale_id};")
            detailedProducts = self.cursor.fetchall()
            if column == 0:
                self.cursor.execute(f"DELETE FROM detalle_articulo WHERE id_detalle = {detailedProducts[row][0]}")
        
    def updateClient(self):
        self.cursor.execute("SELECT max(id_venta) FROM venta;")
        sale_id = self.cursor.fetchone()[0]
        self.cursor.execute(f"SELECT * FROM cliente WHERE nombre = \'{self.comboBox.currentText()}\'")
        client_id = self.cursor.fetchone()[0]
        self.cursor.execute(f"UPDATE venta SET fecha_venta = \'{date.today()}\',total = NULL,metodo_de_pago = NULL,id_cliente = {client_id},id_empleado = {self.id} WHERE id_venta = {sale_id}")

    def setItems(self):
        self.cursor.execute("SELECT max(id_venta) FROM venta;")
        sale_id = self.cursor.fetchone()[0]
        self.cursor.execute(f"SELECT * FROM detalle_articulo WHERE id_venta = {sale_id};")
        detailedProducts = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(detailedProducts))
        if len(detailedProducts) > 0:
            self.tableWidget.setColumnCount(5)
            for i in range(len(detailedProducts)):

                self.tableWidget.setItem(i,0,QTableWidgetItem("🗑️"))
                self.tableWidget.setItem(i,1,QTableWidgetItem(str(detailedProducts[i][5])))#idVariacion
                self.tableWidget.setItem(i,2,QTableWidgetItem(str(detailedProducts[i][1])))#cantidad
                self.tableWidget.setItem(i,3,QTableWidgetItem(str(detailedProducts[i][2])))#P/U
                self.tableWidget.setItem(i,4,QTableWidgetItem(str(detailedProducts[i][2] * detailedProducts[i][1])))#P/C

        total = 0
        for i in range(self.tableWidget.rowCount()):
            total += float(self.tableWidget.item(i,4).text())
        self.label_5.setText(f"TOTAL: {total}")

        QTimer.singleShot(3000, self.setItems)

    def card(self):
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)

    def cash(self):
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)

    def makeSale(self):
        self.cursor.execute("SELECT max(id_venta) FROM venta;")
        sale_id = self.cursor.fetchone()[0]
        total = 0
        for i in range(self.tableWidget.rowCount()):
            total += float(self.tableWidget.item(i,4).text())
        if self.radioButton_3.isChecked():
            self.cursor.execute(f"UPDATE venta SET total = {total}, metodo_de_pago = \'Tarjeta\' WHERE id_venta = {sale_id};")
        else:
            self.cursor.execute(f"UPDATE venta SET total = {total}, metodo_de_pago = \'Efectivo\' WHERE id_venta = {sale_id};")

        self.cursor.execute("SELECT max(id_venta) FROM venta;")
        latestSale = self.cursor.fetchone()[0]
        self.cursor.execute(f"SELECT * FROM venta WHERE id_venta = {latestSale};")
        sale = self.cursor.fetchone()
        self.cursor.execute(f"SELECT * FROM detalle_articulo WHERE id_venta = {latestSale};")
        detailedProducts = self.cursor.fetchall()
        with open("Reporte\\Ventas.txt", "a") as f:
            f.write(f"\n\nFecha: {date.today()}")
            f.write(f"\nVenta:")
            f.write(f"\nid_venta, fecha_venta, total, metodo_de_pago, id_cliente, id_empleado")
            f.write(f"\n{sale}")
            f.write(f"\nArticulos en detalle: ")
            f.write(f"\nid_detalle, cantidad, precio_unitario, descuento_aplicado, id_venta, id_variacion")
            for i in range(len(detailedProducts)):
                f.write(f"\n{detailedProducts[i]}")

        self.mainWindow.close()

    def closeEvent(self,event):      
        self.connection.close()
        self.cursor.close()
        event.accept()

    def search(self):
        if self.lineEdit_2.text() == "":
            pass
        else:
            if self.radioButton.isChecked():
                self.cursor.execute(f"SELECT * FROM producto WHERE id_producto = {self.lineEdit_2.text()} ")
            else:
                self.cursor.execute(f"SELECT * FROM producto WHERE nombre LIKE \'%{self.lineEdit_2.text()}%\' ")
            result = self.cursor.fetchall()
            if len(result) > 0:
                self.ventanaBuscar = ui_ventasBuscar.ventasBuscar(result)
                self.ventanaBuscar.show()
            else:
                self.ventasError = ui_ventasError.ventasError()
                self.ventasError.show()        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TOTAL:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Borrar", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"P/U", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"P/C", None));
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Busqueda por ID", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Busqueda por nombre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Empleado:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Metodo de pago:", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Tarjeta", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Efectivo", None))
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tarjeta", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CVV", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Registrar venta", None))
    # retranslateUi



class venta(QMainWindow):
    def __init__(self, id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, id)