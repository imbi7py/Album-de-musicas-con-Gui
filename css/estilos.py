from PyQt5 import QtGui

class Estilos:

	def estilo_registro(self,Pantalla):
		Pantalla_registro = Pantalla
		Pantalla_registro.setStyleSheet("QMainWindow{\n"
"background: #343d46;\n"
"color: #f9ae5d;\n"
"}\n"

"QLineEdit{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color:#FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color:rgb(34,36,44);\n"
"}\n"

"QLineEdit:hover{\n"
"border: 2px solid rgb(48,170,255);\n"
"}\n"

"QLineEdit:focus{\n"
"border: 2px solid rgb(85,170,255);\n"
"background-color: rgb(43,45,56);\n"
"}\n"

"QPushButton {\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(48,170,255);\n"
"background-color: #343d46;\n"
"color: #f9b052;\n"
"font-size: 12px;\n"
"}\n"

"QPushButton:hover {\n"
"font-size: 15px;\n"
"font-weight: bold; \n"
"border: 1.5px solid #e76768;\n"
"}")

	def estilo_eliminar(self,eliminar):
		eliminador = eliminar
		eliminador.setStyleSheet("QMainWindow{\n"
"background:#343d46;\n"
"}\n"

"QLineEdit{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color:#FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color:rgb(34,36,44);\n"
"}\n"

"QLineEdit:hover{\n"
"border: 2px solid rgb(48,170,255);\n"
"}\n"

"QLineEdit:focus{\n"
"border: 2px solid rgb(85,170,255);\n"
"background-color: rgb(43,45,56);\n"
"}\n"

"QPushButton {\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(48,170,255);\n"
"background-color: #343d46;\n"
"color: #f9b052;\n"
"font-size: 12px;\n"
"}\n"

"QPushButton:hover {\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"border: 1.5px solid #e76768;\n"
"}\n"

"QScrollBar{\n"
"background : #343d46;\n"
"border: 1px solid #343d46;}\n"

"QScrollBar::handle{\n"
"background : #699ec6;}\n"

"QScrollBar::handle::pressed{\n"
"background : #e76768;}\n"

"QScrollBar::add-page, QScrollBar::sub-page{\n"
"background: none;\n"
"}\n"

"QScrollBar::add-line, QScrollBar::sub-line{\n"
"background : #343d46;\n"
"border: 1px solid #343d46;}\n"

"QPushButton {\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(48,170,255);\n"
"background-color: #343d46;\n"
"color: #f9b052;\n"
"font-size: 12px;\n"
"}\n"

"QComboBox{\n"
"color: #f9b052;\n"
"background: #343d46}\n"

"QComboBox QAbstractItemView { \n" 
"selection-background-color: #343d46;\n "
"selection-color: #f9b052; }\n"                                          
                              
"QHeaderView::section {\n"
"color: #e76768;\n"
"background-color: #343d46;\n"
"border: 1px solid rgb(34,36,44);\n"
"}\n"

"QTableWidget QTableCornerButton::section {\n"
"background-color: #343d46;\n"
    #"border: 1px solid rgb(34,36,44);\n"
"}"

"QTableView{\n"
"color: #f9b052;\n"
"border: 3px;\n"
"background: #343d46;\n"
"}\n"

"QTableView::item:focus{\n"
"selection-background-color: #343d46\n"
";}\n"

"QTableView:verticalScrollBar{\n"
"width: 30px;\n"
" color:black;\n"
"}")

	def estilo_buscar(self,buscarlf):
		buscador = buscarlf
		buscador.setStyleSheet("QMainWindow{\n"
"background:#343d46;\n"
"}\n"

"QLineEdit{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color:#FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color:rgb(34,36,44);\n"
"}\n"

"QLineEdit:hover{\n"
"border: 2px solid rgb(48,170,255);\n"
"}\n"

"QLineEdit:focus{\n"
"border: 2px solid rgb(85,170,255);\n"
"background-color: rgb(43,45,56);\n"
"}\n"

"QPushButton {\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(48,170,255);\n"
"background-color: #343d46;\n"
"color: #f9b052;\n"
"font-size: 12px;\n"
"}\n"

"QPushButton:hover {\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"border: 1.5px solid #e76768;\n"
"}\n"

"QScrollBar{\n"
"background : #343d46;\n"
"border: 1px solid #343d46;}\n"
"QScrollBar::handle{\n"
"background : #699ec6;}\n"
"QScrollBar::handle::pressed{\n"
"background : #e76768;}\n"
"QScrollBar::add-page, QScrollBar::sub-page{\n"
"background: none;\n"
"}\n"

"QScrollBar::add-line, QScrollBar::sub-line{\n"
"background : #343d46;\n"
"border: 1px solid #343d46;}\n"
"QPushButton {\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(48,170,255);\n"
"background-color: #343d46;\n"
"color: #f9b052;\n"
"font-size: 12px;\n"
"}\n"

"QComboBox{\n"
"color: #f9b052;\n"
"background: #343d46}\n"

"QComboBox QAbstractItemView { \n" 
"selection-background-color: #343d46;\n "
"selection-color: #f9b052; }\n"                                          
                              
"QHeaderView::section {\n"
"color: #e76768;\n"
"background-color: #343d46;\n"
"border: 1px solid rgb(34,36,44);\n"
"}\n"

"QTableWidget QTableCornerButton::section {\n"
"background-color: #343d46;\n"
    #"border: 1px solid rgb(34,36,44);\n"
"}"
"QTableView{\n"
"color: #f9b052;\n"
"border: 3px;\n"
"background: #343d46;\n"
"}\n"

"QTableView::item:focus{\n"
"selection-background-color: #343d46\n"
";}\n"

"QTableView:verticalScrollBar{\n"
"width: 30px;\n"
" color:black;\n"
"}")

	def estilo_editar(self,editar):
		editor = editar
		editor.setStyleSheet("QMainWindow{\n"
"background:#343d46;\n"
"}\n"

"QLineEdit{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color:#FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color:rgb(34,36,44);\n"
"}\n"

"QLineEdit:hover{\n"
"border: 2px solid rgb(48,170,255);\n"
"}\n"

"QLineEdit:focus{\n"
"border: 2px solid rgb(85,170,255);\n"
"background-color: rgb(43,45,56);\n"
"}\n"

"QScrollBar{\n"
"background : #343d46;\n"
"border: 1px solid #343d46;}\n"

"QScrollBar::handle{\n"
"background : #699ec6;}\n"

"QScrollBar::handle::pressed{\n"
"background : #e76768;}\n"

"QScrollBar::add-page, QScrollBar::sub-page{\n"
"background: none;\n"
"}\n"

"QScrollBar::add-line, QScrollBar::sub-line{\n"
"background : #343d46;\n"
"border: 1px solid #343d46;}\n"

"QPushButton {\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(48,170,255);\n"
"background-color: #343d46;\n"
"color: #f9b052;\n"
"font-size: 12px;\n"
"}\n"

"QPushButton:hover {\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"border: 1.5px solid #e76768;\n"
"}\n"

"QTableView{\n"
"color: #f9b052;\n"
"border: 3px;\n"
"background: #343d46;\n"
"}\n"

"QTableView::item:focus{\n"
"selection-background-color: #343d46\n"
";}\n"

"QComboBox{\n"
"color: #f9b052;\n"
"background: #343d46}\n"

"QComboBox QAbstractItemView { \n" 
"selection-background-color: #343d46;\n "
"selection-color: #f9b052; }\n"                                          
                              
"QHeaderView::section {\n"
"color: #e76768;\n"
"background-color: #343d46;\n"
"border: 1px solid rgb(34,36,44);\n"
"}\n"

"QTableWidget QTableCornerButton::section {\n"
"background-color: #343d46;\n"
    #"border: 1px solid rgb(34,36,44);\n"
"}")

	def estilo_index(self,index):
		albun_musica = index
		albun_musica.setStyleSheet("QMainWindow{\n"
"background: #20252b;\n"
"}\n"

"QPushButton{\n"
"border-radius: 7px; \n"
"border: 1.5px solid #699ec6;\n"
"background: #343d46;\n"
"color: #f9b052;\n"
"font-size: 12px;\n"
"}\n"

"QPushButton:hover {\n"
"font-size: 15px;\n"
"font-weight: bold; \n"
"border: 1.5px solid #e76768;\n"
"}")
