'''
Curso de creacion de GUIs con Qt5 y Python

Author: Kiko Correoso
WebSite: https://pybonacci.org
Licencia: MIT

Main02.py
    - Usar QMAinWindow como ventana principal

    - Añadir una barra de estado.
'''

import os

os.environ['QT_API'] = 'pyside2' #Variable de entorno
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
        self.move(0, 0)
        self.setWindowTitle('Hola, Icono refactorizado')
        ruta_icono = Path('.', 'imgs', 'instagram.png')
        self.setWindowIcon(QIcon(str(ruta_icono)))
        self.statusBar().showMessage('Ready')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MiVentana()
    sys.exit(app.exec_())