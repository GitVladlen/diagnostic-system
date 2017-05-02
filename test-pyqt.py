import sys

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.uic import compileUi


if __name__ == '__main__':
    # app = QApplication(sys.argv)

    # w = QWidget()
    # w.resize(500, 500)
    # w.move(300, 300)
    # w.setWindowTitle('My Window Title')
    # w.show()

    # sys.exit(app.exec_())
    with open("./ui/mainwin.py", "w") as out_file:
        compileUi("./ui/mainwin.ui", out_file, True)