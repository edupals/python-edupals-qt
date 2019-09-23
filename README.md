# Python helpers to build qt apps


## Translators

This library provide helper to use po files (gettext) between ts files.

- example

```python

from edupals.qt.translator import QTranslatorGettext
from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication(sys.argv)
qtg = QTranslatorGettext()
qtg.load('miappdomain')
app.installTranslator(qtg)
app.exec_()

```

### Extract strings from ui file

pylupdate5 *.ui -ts miapp.ts

### Convert ts files to po files

lconvert miapp.ts -o miapp.po


