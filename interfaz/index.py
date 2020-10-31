from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.insert(0, '../css')
from estilos import Estilos
from inter_buscar import *
from inter_editar import *
from inter_eliminar import *
from inter_registrar import *

class Albun_musicaxd:#(object)
    
    def __init__(self, Albun_musica):

        Albun_musica.setObjectName("Albun_musica")
        Albun_musica.resize(343, 326)
        Albun_musica.setMinimumSize(QtCore.QSize(343, 326))
        Albun_musica.setMaximumSize(QtCore.QSize(343, 326))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))#, QtGui.QIcon.Normal, QtGui.QIcon.On
        Albun_musica.setWindowIcon(icon)
        #Esto va en otro archiv/
        css = Estilos()
        css.estilo_index(Albun_musica)
        #Esto va en otro archivo
        self.centralwidget = QtWidgets.QWidget(Albun_musica)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_registrar_musica = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registrar_musica.setGeometry(QtCore.QRect(50, 50, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_registrar_musica.setFont(font)
        self.btn_registrar_musica.setStyleSheet("")
        self.btn_registrar_musica.setObjectName("btn_registrar_musica")
        self.btn_registrar_musica.clicked.connect(self.abrir_registro)
        self.btn_ver_album = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ver_album.setGeometry(QtCore.QRect(190, 50, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_ver_album.setFont(font)
        self.btn_ver_album.setStyleSheet("")
        self.btn_ver_album.setObjectName("btn_ver_album")
        self.btn_ver_album.clicked.connect(self.abrir_buscador)
        self.btn_editar_cancion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editar_cancion.setGeometry(QtCore.QRect(50, 180, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_editar_cancion.setFont(font)
        self.btn_editar_cancion.setStyleSheet("")
        self.btn_editar_cancion.setObjectName("btn_editar_cancion")
        self.btn_editar_cancion.clicked.connect(self.abrir_editor)
        self.btn_eliminar_musica = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eliminar_musica.setGeometry(QtCore.QRect(190, 180, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_eliminar_musica.setFont(font)
        self.btn_eliminar_musica.setStyleSheet("")
        self.btn_eliminar_musica.setObjectName("btn_eliminar_musica")
        self.btn_eliminar_musica.clicked.connect(self.abrir_eliminador)
        Albun_musica.setCentralWidget(self.centralwidget)

        self.texto_transparente(Albun_musica)
        QtCore.QMetaObject.connectSlotsByName(Albun_musica)
        Albun_musica.setTabOrder(self.btn_registrar_musica, self.btn_ver_album)
        Albun_musica.setTabOrder(self.btn_ver_album, self.btn_editar_cancion)
        Albun_musica.setTabOrder(self.btn_editar_cancion, self.btn_eliminar_musica)

    def texto_transparente(self, Albun_musica):
        _translate = QtCore.QCoreApplication.translate
        Albun_musica.setWindowTitle(_translate("Albun_musica", "Album de Canciones"))
        self.btn_registrar_musica.setText(_translate("Albun_musica", "REGISTRAR"))
        self.btn_ver_album.setText(_translate("Albun_musica", "CONSULTAR"))
        self.btn_editar_cancion.setText(_translate("Albun_musica", "EDITAR"))
        self.btn_eliminar_musica.setText(_translate("Albun_musica", "ELIMINAR"))

    def abrir_registro(self):
        self.ventana = QtWidgets.QMainWindow()
        self.xd = Pantalla_registroxd(self.ventana)
        self.ventana.show()

    def abrir_buscador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.xd = Buscadorxd(self.ventana)
        self.ventana.show()        

    def abrir_editor(self):
        self.ventana = QtWidgets.QMainWindow()
        self.xd = Editorxd(self.ventana)
        self.ventana.show()

    def abrir_eliminador(self):
        self.ventana = QtWidgets.QMainWindow()
        self.xd = Eliminadorxd(self.ventana)
        self.ventana.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Albun_musica = QtWidgets.QMainWindow()
    ventana = Albun_musicaxd(Albun_musica)
    Albun_musica.show()
    sys.exit(app.exec_())
