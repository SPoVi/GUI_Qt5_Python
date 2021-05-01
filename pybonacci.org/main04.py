'''
Capitulo 7 : Menu

Este capitulo describe como crear menus y submenus de la ventana principal y algunas peculiaridades más de Qt
'''

import os
os.environ['QT_API'] = 'pyside2'
import sys
from pathlib import Path

from qtpy.QtWidgets import QApplication, QMainWindow
from qtpy.QtGui import QIcon


class MiVentana(QMainWindow):

    def __init__(self):
        super().__init__()
        self._create_ui()

    def _create_ui(self):
        self.resize(500, 300)
        self.move(0,0)
        self.setWindowTitle('Hola, QMainWindow')
        ruta_icono = Path('.','imgs','instagram.png')
        self.setWindowIcon(QIcon(str(ruta_icono)))
        self.statusBar().showMessage('Ready')
        self._create_menu() ## NUEVA LINEA
        self.show()

    ## NUEVAS LINEAS
    def _create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File') # Lo que quieres que aparezca en el menu
        file_menu = menubar.addMenu('&Help')
        file_menu = menubar.addMenu('Options') # Si quitamos el & perdemos la navegacion rapida

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MiVentana()
    sys.exit(app.exec_())
