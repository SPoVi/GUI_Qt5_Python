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
import time ## NUEVA LINEA

from qtpy.QtCore import Qt ## NUEVA LINEA
from qtpy.QtWidgets import QApplication, QMainWindow, QSplashScreen ## NUEVA LINEA
from qtpy.QtGui import QIcon, QPixmap ## NUEVA LINEA

'''
Qt: espacio de nombres con información útil que Qt (el framework) usa internamente en todo su código
QPixmap: La usamos únicamente para añadir un mapa de píxeles (nuestra imagen) a la ventana del Splash Screen. 
QSplashScreen: Esta clase no es más que una nueva clase que, nuevamente, hereda de QWidget, como QMainWindow, y que tiene alguna 
               nueva funcionalidad para que creemos la Splash Screen para nuestra aplicación
'''

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

    ##  NUEVAS LINEAS
    # Crea y muestra el splash screen
    path = Path('imgs','splash_screen_kali.png')
    splash_pix = QPixmap(str(path))
    splash = QSplashScreen(
        splash_pix,
        Qt.WindowStaysOnTopHint
    )
    splash.setEnabled(False)
    splash.show()

    # Esto es un simple contador/temporizador para mostrar en la pantalla el splash screen.
    # En el futuro haremos que esto sea más útil
    for i in range(0,5):
        msg = (
            '<h1><font color="white">'
            f'Listo en {5-i}s'
            '</font></h1>'
        )
        splash.showMessage(
            msg,
            int(Qt.AlignBottom) | int(Qt.AlignCenter),
            Qt.black
        )
        time.sleep(1)
        app.processEvents()

    w = MiVentana()
    splash.finish(w)
    sys.exit(app.exec_())

'''
En esta parte ya hacemos uso de algunas de las nuevas cosas que hemos importado:

    - path:  simplemente guarda la ruta a la imagen que vamos a usar de fondo. Esto no es código relacionado 
        con Qt en sí.
    - splash_pix: es una instancia de QPixmap. Nos guarda la imagen en una forma que entiende Qt.
    - splash es la instancia de QSplashScreen. Recibe la imagen en la forma en que la entiende Qt, splash_pix, y, además, 
        le pasamos una marca o flag, Qt.WindowStaysOnTopHint, que le indica que debe permanecer delante del resto de 
        ventanas en el escritorio.
    - splash.setEnabled(False): nos permite decirle al programa que no esté activo a eventos que le podamos pasar, como 
        un click, ya que podemos tener algún efecto indeseado.
    - splash.show(): mediante este método mostramos el Splash Screen en pantalla.
'''