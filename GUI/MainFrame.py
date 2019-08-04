import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QRegExp, QRegExpValidator


class MyTable(QWidget):
    def __init__(self):
        super(MyTable, self).__init__()
        self._cost_type = ['产量',
                          '员工成本', '工资', '奖金', '福利费', '养老金', '医疗保险',
                          '失业保险', '工伤保险', '生育保险', '住房公积金', '提前退休福利',
                          '住房补贴', '独生子女补助', '职工教育经费', '工会经费', '其他',
                          '甲醇', '洗油', '硫酸', '机物料消耗（包括液碱）', '水费', '电费',
                          '劳保费', '折旧费', '修理费', '油耗', '车修', '低值易耗品摊销',
                          '保险费', '招待费', '差旅费', '办公费', '其它物料', '润滑油',
                          '药品', '化验费', '动力煤', '安全生产费', '电话费', '设备检测费',
                          '大修费', '防暑降温费', '煤气费用', '劳务费用', '生产车辆费用',
                          '生产车辆油耗', '生产车辆备件', '生产车辆保险', '其它费用',
                          '催化剂摊销', '蒸汽', '污水处理', '氢气（天然气）', '解析气',
                          '租赁费', '脱硫费用', '排污费', '环保费', '驰放气', '其他',
                          '导热油', '熔盐', '以下中煤使用：干熄焦费用', '污水深度处理',
                          '脱硫脱硝费用', '15MW制造费用', '后脱硫费用', '以下三维使用：循环水',
                          '纯水', '直流水', '氮气', '仪用空气', '固定资产投资利息', '铺底流资',
                          '银行利息收入', '手续费', '财产保险', '印花税', '房产税', '土地税',
                          '证件费', '电仪服务费', '河道维护费', '价格调控基金', '税金及附加', '福利费',
                          '合计',
                          '可控费用']
        self.initUI()

    def initUI(self):
        self.resize(1280, 700)
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

        self.table.itemChanged.connect(self.table_item_changed)

        # self.table.itemSelectionChanged.connect(self.table_item_changed)


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
                # edit.textChanged.connect(self.text_changed)
                edit.focusOutEvent(self.text_changed)
                edit.setValidator(QRegExpValidator(QRegExp('^\d+(\.\d\d)?$')))
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
        text = self.table.cellWidget(row, column).text()
        if text == '':
            return
        print(text)
        num = float(text)
        print('%.2f' % num)
        # self.table.cellWidget(row, column).setText(num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTable = MyTable()
    myTable.show()
    sys.exit(app.exec_())
