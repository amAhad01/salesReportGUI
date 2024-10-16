from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

def mBuilder(message):
    m = QMessageBox()
    m.setIcon(QMessageBox.Icon.Critical)
    m.setWindowTitle('Error')
    m.setWindowIcon(QIcon('icons/error.svg'))
    m.setText(message)
    m.exec()

def errorfunc():
    mBuilder("Invalid Beginning Year's Number!")

def errorfunc2():
    mBuilder("Invalid Beginning Month's Number!")

def errorfunc3():
    mBuilder("You Can't Have Equal Beginning and Ending Time!")
