from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Conexion:

    def registrar_datos(self,nombre_musica,autor,genero,año,duracion,alerta):     
        conexion = pymysql.connect(host='localhost',user='root',passwd='J10SK4',db='album')
        try:
            with conexion.cursor() as cursor:
                slq = ("insert into registro(nombre_musica,autor,genero,año,duracion) values(%s,%s,%s,%s,%s)")
                tupla =(nombre_musica,autor,genero,año,duracion)
                cursor.execute(slq,tupla)
                if (cursor):
                    alerta = alerta
                    #self.mensaje("Alerta!!","se ha registrado la musica")
            conexion.commit()
        finally:
            conexion.close()


    def buscar_datos(self,datosl):
        #self.datos = [] Tengo que crear una lista afuera de esto
        datos = datosl
        conexion = pymysql.connect(host='localhost',user='root',passwd='J10SK4',db='album')
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre_musica,autor,genero,año,duracion FROM registro")
                album = cursor.fetchall()
                for musicas in album:
                    row = musicas
                    datos.append((row))
                #return row
        finally:
            conexion.close()

    def eliminar_musica(self,musica,alerta):
        nombre_musica = musica
        conexion = pymysql.connect(host='localhost',user='root',password='J10SK4',db='album')
        try:
            with conexion.cursor() as cursor:                  
                consulta = "DELETE FROM registro WHERE nombre_musica=%s"
                tupla =(nombre_musica)
                cursor.execute(consulta,tupla)
                if (cursor):
                    alerta = alerta
            conexion.commit()
        finally:
                conexion.close()

    def conectar(self,gdatos,tabla):
        datos = gdatos
        tabla_db = tabla
        fila = 0
        for registro in datos:
            columna = 0
            tabla_db.insertRow(fila)
            for elemento in registro:
                celda = QtWidgets.QTableWidgetItem(elemento)#QtWidgets.QTableWidgetItem
                tabla_db.setItem(fila,columna,celda)
                columna += 1
            fila += 1 

    def editar_datos(self,buscar_n,nombre,autor,genero,año,duracion,alerta):
        #nombre_buscado = self.escr_buscar.text()
        buscar_nombre = buscar_n
        conexion = pymysql.connect(host='localhost',user='root',password='J10SK4',db='album')
        try:
            with conexion.cursor() as cursor:                   
                consulta = "UPDATE registro SET nombre_musica=%s, autor=%s,genero=%s, año=%s,\
                            duracion=%s WHERE nombre_musica=%s"
                tupla =(nombre,autor,genero,año,duracion,buscar_nombre)
                cursor.execute(consulta,tupla)
                if (cursor):
                	alerta = alerta
                    #self.mensaje("Alerta!!","se ha registrado la musica")
            conexion.commit()
        finally:
            conexion.close()

