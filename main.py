from PyQt5 import QtWidgets
from main_form import Ui_MainWindow

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec_()