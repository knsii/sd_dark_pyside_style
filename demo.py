import os
import sys
from PySide2 import QtWidgets,QtCore
from PySide2.QtUiTools import QUiLoader



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        file = QtCore.QFile("demo.ui")
        self.setWindowTitle("sd dark style")
        file.open(file.ReadOnly)
        loader = QUiLoader()
        loader.load(file,self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    # start with file:/// to make image url inside qss relative
    app.setStyleSheet("file:///styles/dark.qss")

    window.show()

    app.exec_()



