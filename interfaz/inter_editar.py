from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('..')
from db_conectar.Conectordb import Conexion
from css.estilos import Estilos
import pymysql

class Editorxd:

    def mensaje(self,titulo,mensaje):
        mensj = QtWidgets.QMessageBox()
        mensj.setWindowTitle(titulo)
        mensj.setText(mensaje)
        mensj.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mensj.exec_()

    def __init__(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(752, 314)
        Editor.setMinimumSize(QtCore.QSize(752, 314))
        Editor.setMaximumSize(QtCore.QSize(752, 314))
        self.adaptador = QtWidgets.QWidget(Editor)
        self.adaptador.setObjectName("adaptador")
        #Logo
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))
        Editor.setWindowIcon(icono)
        #Estilos de la ventana
        css = Estilos()
        css.estilo_editar(Editor)
        #Tabla que se conecta de manera directa con mysql
        self.tabla_db = QtWidgets.QTableWidget(self.adaptador)
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
        #conexion con mysql y la tabla de pyqt5
        self.buscar()
        conectarx = Conexion()
        conectarx.conectar(self.datos,self.tabla_db)     
        #boton de busqueda
        self.btn_buscar = QtWidgets.QPushButton(self.adaptador)
        self.btn_buscar.setGeometry(QtCore.QRect(230, 60, 75, 31))
        self.btn_buscar.setObjectName("btn_buscar")
        #Contenedores
        self.contenedor = QtWidgets.QWidget(self.adaptador)
        self.contenedor.setGeometry(QtCore.QRect(50, 10, 431, 51))
        self.contenedor.setObjectName("contenedor")
        self.contenedor2 = QtWidgets.QHBoxLayout(self.contenedor)
        self.contenedor2.setContentsMargins(0, 0, 0, 0)
        self.contenedor2.setObjectName("contenedor2")
        #Linea de busqueda
        self.escr_buscar = QtWidgets.QLineEdit(self.contenedor)
        self.escr_buscar.setObjectName("escr_buscar")
        self.contenedor2.addWidget(self.escr_buscar)
        #Caja de busqueda
        self.cbox_buscar_por = QtWidgets.QComboBox(self.contenedor)
        self.cbox_buscar_por.setObjectName("cbox_buscar_por")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.contenedor2.addWidget(self.cbox_buscar_por)
        #Linea para editar el nombre
        self.edt_nombre = QtWidgets.QLineEdit(self.adaptador)
        self.edt_nombre.setGeometry(QtCore.QRect(540, 20, 201, 31))
        self.edt_nombre.setObjectName("edt_nombre")
        #Linea para editar el autor
        self.edt_autor = QtWidgets.QLineEdit(self.adaptador)
        self.edt_autor.setGeometry(QtCore.QRect(540, 70, 201, 31))
        self.edt_autor.setObjectName("edt_autor")
        #Linea para editar el genero
        self.edt_genero = QtWidgets.QLineEdit(self.adaptador)
        self.edt_genero.setGeometry(QtCore.QRect(540, 120, 201, 31))
        self.edt_genero.setObjectName("edt_genero")
        #Linea para editar el año
        self.edt_ano = QtWidgets.QLineEdit(self.adaptador)
        self.edt_ano.setGeometry(QtCore.QRect(540, 170, 201, 31))
        self.edt_ano.setObjectName("edt_ano")
        #Linea para editar la duracion de la musica
        self.editar_duracion = QtWidgets.QLineEdit(self.adaptador)
        self.editar_duracion.setGeometry(QtCore.QRect(540, 220, 201, 31))
        self.editar_duracion.setObjectName("editar_duracion")
        #Boton para guardar cambios
        self.btn_guardar_editado = QtWidgets.QPushButton(self.adaptador)
        self.btn_guardar_editado.setGeometry(QtCore.QRect(600, 270, 81, 31))
        self.btn_guardar_editado.setObjectName("btn_guardar_editado")
        self.btn_guardar_editado.clicked.connect(self.editar)
        #variado
        Editor.setCentralWidget(self.adaptador)
        self.texto_transparente(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def texto_transparente(self, Editor):
        nombresxd = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(nombresxd("Editor", "Editar musica"))
        item = self.tabla_db.horizontalHeaderItem(0)
        item.setText(nombresxd("Editor", "Nombre"))
        item = self.tabla_db.horizontalHeaderItem(1)
        item.setText(nombresxd("Editor", "Autor"))
        item = self.tabla_db.horizontalHeaderItem(2)
        item.setText(nombresxd("Editor", "Genero"))
        item = self.tabla_db.horizontalHeaderItem(3)
        item.setText(nombresxd("Editor", "Año"))
        item = self.tabla_db.horizontalHeaderItem(4)
        item.setText(nombresxd("Editor", "Duracion"))
        #Aqui estan palabras predefinidas la cual se van a cambiar al momento de escribi dentro de ellas :V
        self.btn_buscar.setText(nombresxd("Editor", "Buscar"))
        self.escr_buscar.setPlaceholderText(nombresxd("Editor", "Buscar"))
        self.cbox_buscar_por.setItemText(0, nombresxd("Editor", "Nombre "))
        self.cbox_buscar_por.setItemText(1, nombresxd("Editor", "Autor"))
        self.cbox_buscar_por.setItemText(2, nombresxd("Editor", "Genero"))
        self.edt_nombre.setPlaceholderText(nombresxd("Editor", "Editar nombre"))
        self.edt_autor.setPlaceholderText(nombresxd("Editor", "Editar autor"))
        self.edt_genero.setPlaceholderText(nombresxd("Editor", "Editar genero"))
        self.edt_ano.setPlaceholderText(nombresxd("Editor", "Editar año"))
        self.editar_duracion.setPlaceholderText(nombresxd("Editor", "Editar duracion"))
        self.btn_guardar_editado.setText(nombresxd("Editor", "Editar"))

    def buscar(self):
        buscar = Conexion()
        self.datos = []
        buscar.buscar_datos(self.datos)

    def editar(self):
        editar = Conexion()
        nombre_buscado = self.escr_buscar.text()
        nombre = self.edt_nombre.text()
        autor = self.edt_autor.text()
        genero = self.edt_genero.text()
        año = self.edt_ano.text()
        duracion = self.editar_duracion.text()
        msg = self.mensaje("Alerta","Se a editado un contacto a travez de su nombre") 
        editar.editar_datos(nombre_buscado,nombre,autor,genero,año,duracion,msg)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QMainWindow()
    ventana = Editorxd(Editor)
    Editor.show()
    sys.exit(app.exec_())
