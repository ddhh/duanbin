import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QRegExp, QRegExpValidator

class MyTable(QWidget):
    def __init__(self):
        super(MyTable, self).__init__()
        self._cost_type = ['产量', '员工工资', '基本工资', '社保', '其他', '合计', '可控支出']
        self.initUI()

    def initUI(self):
        self.resize(1280, 720)
        conLayout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setRowCount(93)
        self.table.setColumnCount(24)

        header_labels = []
        for i in range(6):
            s1 = '%d月实际-金额' % (i+1)
            s2 = '%d月实际-吨耗' % (i+1)
            header_labels.append(s1)
            header_labels.append(s2)
            s1 = '%d月分解-金额' % (i + 1)
            s2 = '%d月费解-吨耗' % (i + 1)
            header_labels.append(s1)
            header_labels.append(s2)

        self.table.setHorizontalHeaderLabels(header_labels)
        self.table.setVerticalHeaderLabels(self._cost_type)

        # for i in range(12):
        #     self.table.setSpan(0, 2*i+1, 1, 2)
        #     self.table.setSpan(2, 2*i+1, 1, 2)
        #     self.table.setItem(0, 2*i+1, self.setItem('%d月实际' % (i+1)))
        #
        #     self.table.setItem(1, 2*i+1, self.setItem('金额'))
        #     self.table.setItem(1, 2*i+2, self.setItem('吨耗'))
        #
        # for i in range(len(self._cost_type)):
        #     self.table.setItem(2+i, 0, self.setItem(self._cost_type[i]))

        # twheader = QTableWidget()
        # twheader.setRowCount(2)
        # twheader.setColumnCount(26)
        # twheader.horizontalHeader().setVisible(False)
        # twheader.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # twheader.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # twheader.setFocusPolicy(Qt.NoFocus)
        #
        # conLayout.addWidget(twheader)

        # self.table.itemChanged.connect(self.table_item_changed)
        self.table.itemSelectionChanged.connect(self.table_item_changed)


        conLayout.addWidget(self.table)

        self.btn_layout = QHBoxLayout()

        self.save_button = QPushButton('记得随时保存')
        self.cal_button = QPushButton('计算')
        self.create_button = QPushButton('生成excel')
        self.btn_layout.addWidget(self.save_button)
        self.btn_layout.addWidget(self.cal_button)
        self.btn_layout.addWidget(self.create_button)
        conLayout.addLayout(self.btn_layout)
        self.setLayout(conLayout)

        for i in range(93):
            for j in range(24):
                # self.table.setItem(i, j, self.setItem('0.00'))
                edit = QLineEdit('0.00')
                edit.textChanged.connect(self.text_changed)
                edit.setValidator(QRegExpValidator(QRegExp('^\d+(\.\d+)?$')))
                self.table.setCellWidget(i, j, edit)

        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def setItem(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        return item

    def table_item_changed(self):
        selected_items = self.table.selectedIndexes()
        row = selected_items[0].row()
        column = selected_items[0].column()
        print(row, column, 12*93)
        # if len(selected_items) == 0 or len(selected_items) > 1:
        #     print(0)
        #     return
        # item = selected_items[0]
        # item.setText('')
        #
        # item_row = self.table.row(item)
        # item_column = self.table.column(item)
        #
        # print(item_row, item_column)

    def text_changed(self):
        selected_indexes = self.table.selectedIndexes()
        row = selected_indexes[0].row()
        column = selected_indexes[0].column()
        print(self.table.cellWidget(row, column).text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTable = MyTable()
    myTable.show()
    sys.exit(app.exec_())
