#!/usr/bin/env python3

from PyQt5 import QtWidgets, uic
import sys
import translator as gtranslator

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('formulario.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
x = gtranslator.QGTranslator()
x.load('prueba')
app.installTranslator(x)
#window = Ui()
window = QtWidgets.QMainWindow()
uic.loadUi('formulario2.ui', window)
window.show()
app.exec_()
