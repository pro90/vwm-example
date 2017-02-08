#!/usr/bin/python3

import sys
import imp
import test
from PySide2.QtWidgets import QWidget, QMainWindow, QTextEdit, \
    QVBoxLayout, QApplication, QMessageBox
# from PySide2.QtGui import QDragEnterEvent, QDropEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        self.text = QTextEdit()
        self.text.setBaseSize(100, 200)
        self.text.setText(open("test.py").read())
        self.verticalLayout = QVBoxLayout(mainWidget)
        self.verticalLayout.setContentsMargins(20, 100, 20, 20)
        self.verticalLayout.addWidget(self.text)
        self.setAcceptDrops(True)
#        verticalLayout.addWidget(text)
#        self.setLayout(self.verticalLayout)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        open("test.py", 'w').write(self.text.toPlainText())
        imp.reload(test)
        message = QMessageBox(self)
        message.setText("result: " + str(test.foo()))
        message.exec_()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
