from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('..')
from db_conectar.Conectordb import Conexion
from css.estilos import Estilos
import pymysql 

class Buscadorxd:
    
    def __init__(self, Buscador):
        Buscador.setObjectName("Buscador")
        Buscador.resize(534, 314)
        Buscador.setMinimumSize(QtCore.QSize(534, 314))
        Buscador.setMaximumSize(QtCore.QSize(534, 314))       
        self.centralwidget = QtWidgets.QWidget(Buscador)
        self.centralwidget.setObjectName("centralwidget")
        #Logo
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))
        Buscador.setWindowIcon(icono) 
        #Estilo
        css = Estilos()
        css.estilo_buscar(Buscador)
        #Tabla que contiene informacion de la base de datos MySQL.
        self.tabla_db = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_db.setGeometry(QtCore.QRect(10, 110, 511, 192))
        self.tabla_db.setObjectName("tabla_db")
        self.tabla_db.setColumnCount(5)
        self.tabla_db.setRowCount(0)
        item1 = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(0, item1)
        item2 = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(1, item2)
        item3 = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(2, item3)
        item4 = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(3, item4)
        item5 = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(4, item5)
        #Conexion a la base de datos con la tabla de pyqt5
        self.buscar()
        conectarx = Conexion()
        conectarx.conectar(self.datos,self.tabla_db)
        #Boton de busqueda
        self.btn_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar.setGeometry(QtCore.QRect(230, 60, 75, 31))
        self.btn_buscar.setObjectName("btn_buscar")
        #Contenedor
        self.contenedor = QtWidgets.QWidget(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(50, 10, 431, 51))
        self.contenedor.setObjectName("contenedor")
        #Lo que esta dentro del contenedor :V
        self.contenedor2 = QtWidgets.QHBoxLayout(self.contenedor)
        self.contenedor2.setContentsMargins(0, 0, 0, 0)
        self.contenedor2.setObjectName("contenedor2")
        #escribir xd
        self.escr_buscar = QtWidgets.QLineEdit(self.contenedor)
        self.escr_buscar.setObjectName("escr_buscar")
        #Caja con nombres para buscar
        self.cbox_buscar_por = QtWidgets.QComboBox(self.contenedor)
        self.cbox_buscar_por.setObjectName("cbox_buscar_por")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        #Lo demas :v
        self.contenedor2.addWidget(self.escr_buscar)
        self.contenedor2.addWidget(self.cbox_buscar_por)
        Buscador.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Buscador)
        self.hentai(Buscador)

    def hentai(self, Buscador):
        nombress = QtCore.QCoreApplication.translate
        Buscador.setWindowTitle(nombress("Buscador", "Buscar musica"))
        item = self.tabla_db.horizontalHeaderItem(0)
        item.setText(nombress("Buscador", "Nombre"))
        item = self.tabla_db.horizontalHeaderItem(1)
        item.setText(nombress("Buscador", "Autor"))
        item = self.tabla_db.horizontalHeaderItem(2)
        item.setText(nombress("Buscador", "Genero"))
        item = self.tabla_db.horizontalHeaderItem(3)
        item.setText(nombress("Buscador", "Año"))
        item = self.tabla_db.horizontalHeaderItem(4)
        item.setText(nombress("Buscador", "Duracion"))
        self.btn_buscar.setText(nombress("Buscador", "Buscar"))
        self.escr_buscar.setPlaceholderText(nombress("Buscador", "Buscar"))
        self.cbox_buscar_por.setItemText(0, nombress("Buscador", "Nombre "))
        self.cbox_buscar_por.setItemText(1, nombress("Buscador", "Autor"))
        self.cbox_buscar_por.setItemText(2, nombress("Buscador", "Genero"))

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
