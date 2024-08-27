from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import subprocess
            
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400, 600, 600)
    win.setWindowTitle("Scenario Info Setting")
    win.show()
    sys.exit(app.exec_())

window()