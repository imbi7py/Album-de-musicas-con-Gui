from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('..')
from db_conectar.Conectordb import Conexion
from css.estilos import Estilos
import pymysql

class Pantalla_registroxd:

    def mensaje(self,titulo,mensaje):
        mensj = QtWidgets.QMessageBox()
        mensj.setWindowTitle(titulo)
        mensj.setText(mensaje)
        mensj.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mensj.exec_()

    def __init__(self, Pantalla_registro):
        Pantalla_registro.setObjectName("Pantalla_registro")
        Pantalla_registro.resize(322, 361)
        Pantalla_registro.setMinimumSize(QtCore.QSize(322, 361))
        Pantalla_registro.setMaximumSize(QtCore.QSize(322, 361))
        #logo
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))
        Pantalla_registro.setWindowIcon(icono)
        #Estilo
        css = Estilos()
        css.estilo_registro(Pantalla_registro)
        #Linea para escribir el nombre
        self.pantalla = QtWidgets.QWidget(Pantalla_registro)
        self.pantalla.setObjectName("pantalla")
        self.ing_nombre = QtWidgets.QLineEdit(self.pantalla)
        self.ing_nombre.setGeometry(QtCore.QRect(40, 40, 241, 31))
        self.ing_nombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ing_nombre.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.ing_nombre.setObjectName("ing_nombre")
        #Linea para escribir el autor
        self.ing_autor = QtWidgets.QLineEdit(self.pantalla)
        self.ing_autor.setGeometry(QtCore.QRect(40, 90, 241, 31))
        self.ing_autor.setObjectName("ing_autor")
        #Linea para escribir el año
        self.ing_ano = QtWidgets.QLineEdit(self.pantalla)
        self.ing_ano.setGeometry(QtCore.QRect(40, 190, 241, 31))
        self.ing_ano.setObjectName("ing_ano")
        #Linea para escribir el genero
        self.ing_genero = QtWidgets.QLineEdit(self.pantalla)
        self.ing_genero.setGeometry(QtCore.QRect(40, 140, 241, 31))
        self.ing_genero.setObjectName("ing_genero")
        #Linea para escribir la duracion
        self.ing_duracion = QtWidgets.QLineEdit(self.pantalla)
        self.ing_duracion.setGeometry(QtCore.QRect(40, 240, 241, 31))
        self.ing_duracion.setObjectName("ing_duracion")
        #Boton para registrar los datos ingresados
        self.brn_regitra_datos = QtWidgets.QPushButton(self.pantalla)
        self.brn_regitra_datos.setGeometry(QtCore.QRect(110, 290, 101, 31))
        self.brn_regitra_datos.setObjectName("brn_regitra_datos")
        self.brn_regitra_datos.clicked.connect(self.registrar)
        Pantalla_registro.setCentralWidget(self.pantalla)

        self.texto_transparente(Pantalla_registro)
        QtCore.QMetaObject.connectSlotsByName(Pantalla_registro)
        #Orden por tab
        Pantalla_registro.setTabOrder(self.ing_nombre, self.ing_autor)
        Pantalla_registro.setTabOrder(self.ing_autor, self.ing_genero)
        Pantalla_registro.setTabOrder(self.ing_genero, self.ing_ano)
        Pantalla_registro.setTabOrder(self.ing_ano, self.ing_duracion)
        Pantalla_registro.setTabOrder(self.ing_duracion, self.brn_regitra_datos)

    def registrar(self):
        registro = Conexion()
        nombre_musica = self.ing_nombre.text()
        autor = self.ing_autor.text()
        genero = self.ing_genero.text()
        año = self.ing_ano.text()
        duracion = self.ing_duracion.text()
        alerta = self.mensaje("Alerta!!","Se registro una musica")
        registro.registrar_datos(nombre_musica,autor,genero,año,duracion,alerta)

    def texto_transparente(self, Pantalla_registro):
        nombress = QtCore.QCoreApplication.translate
        Pantalla_registro.setWindowTitle(nombress("Pantalla_registro", "Registrar Musica"))
        self.ing_nombre.setPlaceholderText(nombress("Pantalla_registro", "Nombre de la Musica"))
        self.ing_autor.setPlaceholderText(nombress("Pantalla_registro", "Nombre del autor"))
        self.ing_ano.setPlaceholderText(nombress("Pantalla_registro", "Año de la musica"))
        self.ing_genero.setPlaceholderText(nombress("Pantalla_registro", "Genero musical"))
        self.ing_duracion.setPlaceholderText(nombress("Pantalla_registro", "Duracion en minutos"))
        self.brn_regitra_datos.setText(nombress("Pantalla_registro", "Registrar"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Pantalla_registro = QtWidgets.QMainWindow()
    ventana = Pantalla_registroxd(Pantalla_registro)
    Pantalla_registro.show()
    sys.exit(app.exec_())
