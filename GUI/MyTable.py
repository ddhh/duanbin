import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyTable(QTableView):
    def __init__(self, itemModel):
        super(MyTable, self).__init__()
        self.itemModel = itemModel
        self.setModel(itemModel)
        self.frozenTableView = QTableView()

        self.__initUI()

        self.connect(self.horizontalHeader(), QHeaderView.sectionResized(), self.updateSectionWidth())

        self.connect(self.horizontalHeader(), QHeaderView.sectionResized(), self.updateSectionHeight())

        self.connect(self.frozenTableView.verticalScrollBar(), QAbstractSlider.valueChanged(), self.verticalScrollBar(), QAbstractSlider.setValue())

        self.connect(self.verticalScrollBar(), QAbstractSlider.valueChanged(), self.frozenTableView.verticalScrollBar(), QAbstractSlider.setValue())

    def __initUI(self):
        self.frozenTableView.setModel(self.model())
        self.frozenTableView.setFocusProxy(Qt.NoFocus)
        self.frozenTableView.verticalHeader().hide()
        self.frozenTableView.horizontalHeader().setSectionResizeModel(QHeaderView.Fixed)

        self.viewport().stackUnder(self._fozenTableView)

        self.frozenTableView.setStyleSheet("QTableView { border: none;"
                                       "background-color: #8EDE21;"
                                       "selection-background-color: #999}")
        self.frozenTableView.setSelectionModel(self.selectionModel())
        col = 1
        while col < self.model().columnCount():
            self.frozenTableView.setColumnHidden(col, True)

        self.frozenTableView.setColumnWidth(0, self.columnWidth(0))

        self.frozenTableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frozenTableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frozenTableView.show()

        self.updateFrozenTableGeometry()

        self.setHorizontalScrollMode(self.ScrollPerPixel)
        self.setVerticalScrollMode(self.ScrollPerPixel)
        self.frozenTableView.setVerticalScrollMode(self.ScrollPerPixel)

    def __updateFrozenTableGemetry(self):
        self._fozenTableView.setGeometry(self.verticalHeader().width() + self.frameWidth(), self.frameWidth(), self.columnWidth(0), self.viewport().height() + self.horizontalHeader().height())

    def resizeEvent(self, QResizeEvent):
        QTableView.resizeEvent(QResizeEvent)
        self.__updateFrozenTableGemetry()

    def moveCursor(self, QAbstractItemView_CursorAction, Union, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None):
        current = QTableView.moveCursor(QAbstractItemView_CursorAction, Qt_KeyboardModifiers)
        if QAbstractItemView_CursorAction == self.MoveLeft and current.column() >0 and self.visualRect(current).topLeft().x() < self._fozenTableView.columnWidth(0):
            newValue = self.horizontalScrollBar().value() + self.visualRect(current).topLeft().x() - self.horizontalScrollBar().columnWidth(0)
            self.horizontalScrollBar().setValue(newValue)

        return current

    def updateSectionWidth(self, logicalIndex, newSize):
        if logicalIndex == 0:
            self._fozenTableView.setColumnWidth(0, newSize)
            self.__updateFrozenTableGemetry()

    def updateSectionHeight(self, logicalIndex, oldSize, newSize):
        self._fozenTableView.setRowHeight(logicalIndex, newSize)




