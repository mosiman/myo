from PyQt5 import QtWidgets, uic
import sys

MAINUI = "main.ui"
RECORDUI = "record.ui"

class recordUI(QtWidgets.QMainWindow):
    def __init__(self, uiName):
        super(mainUI, self).__init__()
        uic.loadUi(uiName, self)

        # load objects


        # Event callbacks

class mainUI(QtWidgets.QMainWindow):
    def __init__(self, uiName):
        super(mainUI, self).__init__()
        uic.loadUi(uiName, self)

        # load objects

        self.pbtnAddGesture = self.findChild(QtWidgets.QPushButton, 'pbtnAddGesture')
        self.txtGesture = self.findChild(QtWidgets.QTextEdit, 'txtGesture')
        self.lstGestures = self.findChild(QtWidgets.QListView, 'lstGestures')

        # Event callbacks

        self.pbtnAddGesture.clicked.connect(self.test)

        self.show()

    def test(self):
        print(self.txtGesture.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = mainUI("main.ui")
    sys.exit(app.exec_())
