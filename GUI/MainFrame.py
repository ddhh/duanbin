import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage('这是状态栏提升', 5000)
        self.setWindowTitle('PyQt MainWindow例子')

        self.center()

    # 将窗口放在屏幕中间
    def center(self):
        # 获取屏幕大小
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口大小
        size = self.geometry()

        # 移动窗口位置到屏幕中间
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())