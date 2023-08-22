from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.add_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_lineEdit.setText("")
        self.add_lineEdit.setObjectName("add_lineEdit")
        self.gridLayout.addWidget(self.add_lineEdit, 0, 0, 1, 3)
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())
        self.add_pushButton.setObjectName("add_pushButton")
        self.gridLayout.addWidget(self.add_pushButton, 1, 0, 1, 1)
        self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete_it())
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.gridLayout.addWidget(self.delete_pushButton, 1, 1, 1, 1)
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clear_it())
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.gridLayout.addWidget(self.clear_pushButton, 1, 2, 1, 1)
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.gridLayout.addWidget(self.mylist_listWidget, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_it(self):
        item = self.add_lineEdit.text()
        self.mylist_listWidget.addItem(item)
        self.add_lineEdit.setText("")

    def delete_it(self):
        clicked = self.mylist_listWidget.currentRow()
        self.mylist_listWidget.takeItem(clicked)

    def clear_it(self):
        self.mylist_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.add_pushButton.setText(_translate("MainWindow", "Add To The List"))
        self.delete_pushButton.setText(_translate("MainWindow", "Delete From List"))
        self.clear_pushButton.setText(_translate("MainWindow", "Clear List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
