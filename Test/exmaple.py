import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(800,400)
widget.setWindowTitle("This is PyQt Widget example")
widget.show()
exit(app.exec_())