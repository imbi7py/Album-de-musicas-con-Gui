from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.insert(0, '../conectordb')
sys.path.insert(0, '../css')
from Conectordb import Conexion
from estilos import Estilos
import pymysql 

class Buscadorxd:
    def __init__(self, Buscador):
        Buscador.setObjectName("Buscador")
        Buscador.resize(534, 314)
        Buscador.setMinimumSize(QtCore.QSize(534, 314))
        Buscador.setMaximumSize(QtCore.QSize(534, 314))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))#, QtGui.QIcon.Normal, QtGui.QIcon.Offb
        Buscador.setWindowIcon(icon)        
        #Esto va en otro archivo
        css = Estilos()
        css.estilo_buscar(Buscador)
        #Esto va en otro archivo
        self.centralwidget = QtWidgets.QWidget(Buscador)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla_db = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_db.setGeometry(QtCore.QRect(10, 110, 511, 192))
        self.tabla_db.setObjectName("tabla_db")
        self.tabla_db.setColumnCount(5)
        self.tabla_db.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(4, item)
        #
        self.buscar()
        conectarx = Conexion()
        conectarx.conectar(self.datos,self.tabla_db)
        #
        self.btn_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar.setGeometry(QtCore.QRect(230, 60, 75, 31))
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 10, 431, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.escr_buscar = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.escr_buscar.setObjectName("escr_buscar")
        self.horizontalLayout_2.addWidget(self.escr_buscar)
        self.cbox_buscar_por = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cbox_buscar_por.setObjectName("cbox_buscar_por")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.horizontalLayout_2.addWidget(self.cbox_buscar_por)
        Buscador.setCentralWidget(self.centralwidget)
        self.texto_transparente(Buscador)
        QtCore.QMetaObject.connectSlotsByName(Buscador)

    def texto_transparente(self, Buscador):
        _translate = QtCore.QCoreApplication.translate
        Buscador.setWindowTitle(_translate("Buscador", "Buscar musica"))
        item = self.tabla_db.horizontalHeaderItem(0)
        item.setText(_translate("Buscador", "Nombre"))
        item = self.tabla_db.horizontalHeaderItem(1)
        item.setText(_translate("Buscador", "Autor"))
        item = self.tabla_db.horizontalHeaderItem(2)
        item.setText(_translate("Buscador", "Genero"))
        item = self.tabla_db.horizontalHeaderItem(3)
        item.setText(_translate("Buscador", "Año"))
        item = self.tabla_db.horizontalHeaderItem(4)
        item.setText(_translate("Buscador", "Duracion"))
        self.btn_buscar.setText(_translate("Buscador", "Buscar"))
        self.escr_buscar.setPlaceholderText(_translate("Buscador", "Buscar"))
        self.cbox_buscar_por.setItemText(0, _translate("Buscador", "Nombre "))
        self.cbox_buscar_por.setItemText(1, _translate("Buscador", "Autor"))
        self.cbox_buscar_por.setItemText(2, _translate("Buscador", "Genero"))

    def buscar(self):
        buscar = Conexion()
        self.datos = []
        buscar.buscar_datos(self.datos)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Buscador = QtWidgets.QMainWindow()
    ventana = Buscadorxd(Buscador)
    Buscador.show()
    sys.exit(app.exec_())
