import sys
from PyQt5.QtWidgets import *


class MyTable(QWidget):
    def __init__(self):
        super(MyTable, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(1280, 800)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(93)
        tableWidget.setColumnCount(26)
        conLayout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels([chr(i) for i in range(65, 65+26)])

        tableWidget.setSpan(0, 0, 1, 26)
        self.setLayout(conLayout)
        # self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTable = MyTable()
    myTable.show()
    sys.exit(app.exec_())