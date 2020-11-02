from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('..')
sys.path.append('..')
from db_conectar.Conectordb import Conexion
from css.estilos import Estilos
import pymysql


class Eliminadorxd:

    def mensaje(self,titulo,mensaje):
        mensj = QtWidgets.QMessageBox()
        mensj.setWindowTitle(titulo)
        mensj.setText(mensaje)
        mensj.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mensj.exec_()

    def __init__(self, Eliminador):
        Eliminador.setObjectName("Eliminador")
        Eliminador.resize(534, 314)
        Eliminador.setMinimumSize(QtCore.QSize(534, 314))
        Eliminador.setMaximumSize(QtCore.QSize(534, 314))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))#, QtGui.QIcon.Normal, QtGui.QIcon.Offb
        Eliminador.setWindowIcon(icon)
        #Esto va en otro archivo
        css = Estilos()
        css.estilo_eliminar(Eliminador)
        #Esto va en otro archivo
        self.centralwidget = QtWidgets.QWidget(Eliminador)
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
        #
        self.buscar()
        conectarx = Conexion()
        conectarx.conectar(self.datos,self.tabla_db)
        #
        self.tabla_db.setHorizontalHeaderItem(4, item)
        self.btn_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar.setGeometry(QtCore.QRect(170, 60, 75, 31))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 60, 81, 31))
        self.pushButton.setObjectName("pushButton")
        Eliminador.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.eliminar)

        self.texto_transparente(Eliminador)
        QtCore.QMetaObject.connectSlotsByName(Eliminador)
            
    def texto_transparente(self, Eliminador):
        _translate = QtCore.QCoreApplication.translate
        Eliminador.setWindowTitle(_translate("Eliminador", "Eliminar musica"))
        item = self.tabla_db.horizontalHeaderItem(0)
        item.setText(_translate("Eliminador", "Nombre"))
        item = self.tabla_db.horizontalHeaderItem(1)
        item.setText(_translate("Eliminador", "Autor"))
        item = self.tabla_db.horizontalHeaderItem(2)
        item.setText(_translate("Eliminador", "Genero"))
        item = self.tabla_db.horizontalHeaderItem(3)
        item.setText(_translate("Eliminador", "Año"))
        item = self.tabla_db.horizontalHeaderItem(4)
        item.setText(_translate("Eliminador", "Duracion"))
        self.btn_buscar.setText(_translate("Eliminador", "Buscar"))
        self.escr_buscar.setPlaceholderText(_translate("Eliminador", "Buscar"))
        self.cbox_buscar_por.setItemText(0, _translate("Eliminador", "Nombre "))
        self.cbox_buscar_por.setItemText(1, _translate("Eliminador", "Autor"))
        self.cbox_buscar_por.setItemText(2, _translate("Eliminador", "Genero"))
        self.pushButton.setText(_translate("Eliminador", "Eliminar"))

    def buscar(self):
    	buscar = Conexion()
    	self.datos = []
    	buscar.buscar_datos(self.datos)

    def eliminar(self):
    	eliminar = Conexion()
    	nombre_musica = self.escr_buscar.text()
    	msg = self.mensaje("Alerta","Se ha eliminado una musica por su nombre")
    	eliminar.eliminar_musica(nombre_musica,msg)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Eliminador = QtWidgets.QMainWindow()
    ventana = Eliminadorxd(Eliminador)
    Eliminador.show()
    sys.exit(app.exec_())

