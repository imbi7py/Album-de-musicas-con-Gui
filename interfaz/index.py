from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('..')
from css.estilos import Estilos
from inter_buscar import *
from inter_editar import *
from inter_eliminar import *
from inter_registrar import *

class Albun_musicaxd:
    
    def __init__(self, Albun_musica):
        Albun_musica.setObjectName("Albun_musica")
        Albun_musica.resize(343, 326)
        Albun_musica.setMinimumSize(QtCore.QSize(343, 326))
        Albun_musica.setMaximumSize(QtCore.QSize(343, 326))
        self.centralwidget = QtWidgets.QWidget(Albun_musica)
        Albun_musica.setCentralWidget(self.centralwidget)
        # logo
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))
        Albun_musica.setWindowIcon(icono)
        #Estilos
        css = Estilos()
        css.estilo_index(Albun_musica)
        #abrir ventana de registro    
        self.btn_registrar_musica = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registrar_musica.setGeometry(QtCore.QRect(50, 50, 101, 91))
        self.btn_registrar_musica.clicked.connect(self.abrir_registro)
        #abrir ventana de busqueda
        self.btn_ver_album = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ver_album.setGeometry(QtCore.QRect(190, 50, 101, 91))
        self.btn_ver_album.clicked.connect(self.abrir_buscador)
        #abrir ventana de edicion
        self.btn_editar_cancion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editar_cancion.setGeometry(QtCore.QRect(50, 180, 101, 91))
        self.btn_editar_cancion.clicked.connect(self.abrir_editor)
        #abrir ventana para eliminar
        self.btn_eliminar_musica = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eliminar_musica.setGeometry(QtCore.QRect(190, 180, 101, 91))
        self.btn_eliminar_musica.clicked.connect(self.abrir_eliminador)
        # tamaño de letra
        letra = QtGui.QFont()
        letra.setPointSize(8)
        #texto de los botones
        self.texto(Albun_musica)

    def texto(self, Albun_musica):
        transparencia = QtCore.QCoreApplication.translate
        Albun_musica.setWindowTitle(transparencia("Albun_musica", "Album de Canciones"))
        self.btn_registrar_musica.setText(transparencia("Albun_musica", "REGISTRAR"))
        self.btn_ver_album.setText(transparencia("Albun_musica", "CONSULTAR"))
        self.btn_editar_cancion.setText(transparencia("Albun_musica", "EDITAR"))
        self.btn_eliminar_musica.setText(transparencia("Albun_musica", "ELIMINAR"))

    def abrir_registro(self):
        self.ventana = QtWidgets.QMainWindow()
        self.abrir = Pantalla_registroxd(self.ventana)
        self.ventana.show()

    def abrir_buscador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.abrir = Buscadorxd(self.ventana)
        self.ventana.show()        

    def abrir_editor(self):
        self.ventana = QtWidgets.QMainWindow()
        self.abrir = Editorxd(self.ventana)
        self.ventana.show()

    def abrir_eliminador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.abrir = Eliminadorxd(self.ventana)
        self.ventana.show()

if __name__ == "__main__":
    aplicacion = QtWidgets.QApplication(sys.argv)
    Albun_musica = QtWidgets.QMainWindow()
    ventana = Albun_musicaxd(Albun_musica)
    Albun_musica.show()
    sys.exit(aplicacion.exec_())
