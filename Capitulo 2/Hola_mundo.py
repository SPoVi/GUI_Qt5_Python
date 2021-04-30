'''
Curso de creacion de GUIs con Qt5 y Python

Author: Kiko Correoso
WebSite: https://pybonacci.org
Licencia: MIT
'''

import os
os.environ['QT_API'] = 'pyside2' #Variable de entorno
import sys

from qtpy.QtWidgets import QApplication, QWidget
# QApplication : cualquier aplicacion debe crear una instania de esta clase
# QWidget: Es la clase base (plantilla) de todos los widgets. Los widgets vienen a ser las interfaces que permiten
# interactuar al usuario con el GUI (botones, lineas de texto, deslizadores...)
if __name__ == '__main__':

    app = QApplication(sys.argv) # creacion de instancia
    ''' Proporciona  acceso a la informacion global como la carpeta de la aplicacion, la hoja de
    estilos usada, el tamaño de la pantalla en la que corre el GUI
    
    Le pasamos sys.argv como argumento: Esto nos permite recoger los argumentos que le pasamos a traves de la linea de 
    comandos. En este caso el nombre del programa.
    
    Puede recibir una serie de argumentos desde la linea de comandos que le permiten definir su estado interno'''

    w = QWidget()
    w.resize(500,300)
    w.move(0,0)
    w.setWindowTitle("Hola, Mundo")
    w.show()

    sys.exit(app.exec_()) # iniciamos bule de eventos o event loop

    ''' En el ejemplo creamos una instancia QWidget, que es la ventana que vemos. A este le podriamos pasar un objeto 
    padre (un objeto al que perteneceria nuestra instancia w. Como no le pasamos ningun padre esta sera la ventana padre,
    vetana principal de nuestra aplicacion o una ventana top level. 
    
    La instancia w dispone de varios metodos (funciones)'''

    ''' El event loop:
    Esperar/escuchar/estar pendiende de eventos/señales
    
    Espera que suceda algo como un click en un boton, el cambio de estado de una celda en una tabla, un timeout de un 
    temporizador,... y la reaccion del GUI a estos eventos'''