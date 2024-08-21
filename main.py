import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from nhr import Ui_MainWindow

# pyinstaller --onefile --add-data "yunda_kuaiyun.txt;."
# --add-data "yunda_biaozhun.txt;." --add-data "wudizhongtong.txt;." main.py


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('EE.ico'))

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
