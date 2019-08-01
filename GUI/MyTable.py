import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyTable(QWidget):
    def __init__(self):
        super(MyTable, self).__init__()
        self._cost_type = ['产量', '员工工资', 'a', 'b', 'c']
        self.initUI()

    def initUI(self):
        self.resize(900, 600)
        conLayout = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(93)
        tableWidget.setColumnCount(26)
        tableWidget.setHorizontalHeaderLabels([chr(i) for i in range(65, 65+26)])

        for i in range(12):
            tableWidget.setSpan(0, 2*i+1, 1, 2)
            tableWidget.setSpan(2, 2*i+1, 1, 2)
            tableWidget.setItem(0, 2*i+1, self.setItem('%d月实际' % (i+1)))

            tableWidget.setItem(1, 2*i+1, self.setItem('金额'))
            tableWidget.setItem(1, 2*i+2, self.setItem('吨耗'))

        for i in range(len(self._cost_type)):
            tableWidget.setItem(2+i, 0, self.setItem(self._cost_type[i]))

        # twheader = QTableWidget()
        # twheader.setRowCount(2)
        # twheader.setColumnCount(26)
        # twheader.horizontalHeader().setVisible(False)
        # twheader.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # twheader.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # twheader.setFocusPolicy(Qt.NoFocus)
        #
        # conLayout.addWidget(twheader)
        conLayout.addWidget(tableWidget)

        self.setLayout(conLayout)

        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def setItem(self,text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)

        return item


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTable = MyTable()
    myTable.show()
    sys.exit(app.exec_())
