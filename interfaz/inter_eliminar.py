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
        self.centralwidget = QtWidgets.QWidget(Eliminador)
        self.centralwidget.setObjectName("centralwidget")      
        #Logo
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))#, QtGui.QIcon.Normal, QtGui.QIcon.Offb
        Eliminador.setWindowIcon(icono)
        #Estilo de la ventana
        css = Estilos()
        css.estilo_eliminar(Eliminador)
        #Tabla que se conecta de manera directa con mysql
        self.tabla_db = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_db.setGeometry(QtCore.QRect(10, 110, 511, 192))
        self.tabla_db.setObjectName("tabla_db")
        self.tabla_db.setColumnCount(5)
        self.tabla_db.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(0, item)
        self.tabla_db.setHorizontalHeaderItem(1, item)
        self.tabla_db.setHorizontalHeaderItem(2, item)
        self.tabla_db.setHorizontalHeaderItem(3, item)
        self.tabla_db.setHorizontalHeaderItem(4, item)
        #conexion con mysql y la tabla de pyqt5
        self.buscar()
        conectarx = Conexion()
        conectarx.conectar(self.datos,self.tabla_db)
        #Boton de busqueda
        self.btn_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar.setGeometry(QtCore.QRect(170, 60, 75, 31))
        self.btn_buscar.setObjectName("btn_buscar")
        #contenedor
        self.contenedor = QtWidgets.QWidget(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(50, 10, 431, 51))
        self.contenedor.setObjectName("contenedor")
        self.contenedor2 = QtWidgets.QHBoxLayout(self.contenedor)
        self.contenedor2.setContentsMargins(0, 0, 0, 0)
        self.contenedor2.setObjectName("contenedor2")
        #Linea para escribir xd
        self.escr_buscar = QtWidgets.QLineEdit(self.contenedor)
        self.escr_buscar.setObjectName("escr_buscar")
        self.contenedor2.addWidget(self.escr_buscar)
        #Caja para buscar por: 
        self.cbox_buscar_por = QtWidgets.QComboBox(self.contenedor)
        self.cbox_buscar_por.setObjectName("cbox_buscar_por")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.contenedor2.addWidget(self.cbox_buscar_por)
        #boton de eliminar
        self.elimina = QtWidgets.QPushButton(self.centralwidget)
        self.elimina.setGeometry(QtCore.QRect(280, 60, 81, 31))
        self.elimina.setObjectName("elimina")
        Eliminador.setCentralWidget(self.centralwidget)
        self.elimina.clicked.connect(self.eliminar)

        self.texto_transparente(Eliminador)
        QtCore.QMetaObject.connectSlotsByName(Eliminador)
            
    def texto_transparente(self, Eliminador):
        nombresss = QtCore.QCoreApplication.translate
        Eliminador.setWindowTitle(nombresss("Eliminador", "Eliminar musica"))
        item = self.tabla_db.horizontalHeaderItem(0)
        item.setText(nombresss("Eliminador", "Nombre"))
        item = self.tabla_db.horizontalHeaderItem(1)
        item.setText(nombresss("Eliminador", "Autor"))
        item = self.tabla_db.horizontalHeaderItem(2)
        item.setText(nombresss("Eliminador", "Genero"))
        item = self.tabla_db.horizontalHeaderItem(3)
        item.setText(nombresss("Eliminador", "Año"))
        item = self.tabla_db.horizontalHeaderItem(4)
        item.setText(nombresss("Eliminador", "Duracion"))
        #Texto remplazo ?
        self.btn_buscar.setText(nombresss("Eliminador", "Buscar"))
        self.escr_buscar.setPlaceholderText(nombresss("Eliminador", "Buscar"))
        self.cbox_buscar_por.setItemText(0, nombresss("Eliminador", "Nombre "))
        self.cbox_buscar_por.setItemText(1, nombresss("Eliminador", "Autor"))
        self.cbox_buscar_por.setItemText(2, nombresss("Eliminador", "Genero"))
        self.elimina.setText(nombresss("Eliminador", "Eliminar"))

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

