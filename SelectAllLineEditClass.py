from PyQt5 import QtCore, QtGui, QtWidgets
class SelectAllLineEdit(QtWidgets.QLineEdit):
    def __init__(self,admin):
        self.admin = admin
        super(SelectAllLineEdit, self).__init__()
    def mousePressEvent(self, e):
        self.selectAll()