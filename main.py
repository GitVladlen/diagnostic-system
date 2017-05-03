import xlrd
import math
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.mainwindow import Ui_MainWindow


# =======================================================================
class Application(object):
    def __init__(self):
        pass

    def load_data(self, file_name, sheet_name):
        try:
            book = xlrd.open_workbook(file_name)
        except Exception as e:
            print(e)
            return None

        if sheet_name not in book.sheet_names():
            return None

        sh = book.sheet_by_name(sheet_name)

        return sh
        pass

    def get_value_from_data(self, sh, obj_index, value_name):
        row_value_codes = sh.row(0)
        row_obj_values = sh.row(2 + obj_index)

        val_index = None
        for c_index, cell in enumerate(row_value_codes):
            if cell.value == value_name:
                val_index = c_index
                break

        if val_index is None:
            return None

        return row_obj_values[val_index].value
        pass

    def _1_x(self, value):
        return 1.0 / value

    def _xx(self, value):
        return value ** 2

    def _xxx(self, value):
        return value ** 3

    def _sqrt(self, value):
        return math.sqrt(value)

    def _exp(self, value):
        return math.exp(value)

    def _ln(self, value):
        return math.log(value)

    def test(self, sh, da_sh):
        # for rx in range(sh.nrows):
        #     print(sh.row(rx))

        obj_index = 0

        val_names = [
            "x4",
            "x11",
            "x28",
            "x29",
            "x33",
            "x36",
            "x42",
            "x50",

            "x0",
            "x9",
            "x12",
            "x15",
            "x21",
            "x40",
            "x43",
            "x47",
            "x61",
            "x63",
        ]

        values = {}
        for val_name in val_names:
            values[val_name] = self.get_value_from_data(sh, obj_index, val_name)

        values.update(dict(
            x9_1_x=self._1_x(values["x9"]),
            x21_1_x=self._1_x(values["x21"]),
            x40_1_x=self._1_x(values["x40"]),
            x61_1_x=self._1_x(values["x61"]),
            x43_xx=self._xx(values["x43"]),
            x43_xxx=self._xxx(values["x43"]),
            x47_sqrt=self._sqrt(values["x47"]),
            x63_sqrt=self._sqrt(values["x63"]),
            x0_ln=self._ln(values["x0"]),
            x12_exp=self._exp(values["x12"]),
            x15_exp=self._exp(values["x15"]),
            x43_exp=self._exp(values["x43"]),
            x63_exp=self._exp(values["x63"]),
        ))

        result_1 = 0
        result_2 = 0
        for rx in range(da_sh.nrows):
            row = da_sh.row(rx)
            val_name, koef_val_1, koef_val_2 = row[0].value, row[1].value, row[2].value
            if val_name != "const":
                print("{}: {} -> {} * {} -> {} * {}".format(rx, val_name, values[val_name], koef_val_1, values[val_name], koef_val_2))
                result_1 += values[val_name] * koef_val_1
                result_2 += values[val_name] * koef_val_2
            else:
                print("{}: const -> {} -> {}".format(rx, koef_val_1, koef_val_2))
                result_1 += koef_val_1
                result_2 += koef_val_2

        print("Result {}".format(result_1))
        print("Result {}".format(result_2))
        pass

    def run(self):
        sh = self.load_data("./test-data/6  клапаны.xls", "Лист4")

        if sh is None:
            return

        da_sh = self.load_data("./test-data/da_data.xlsx", "Sheet1")

        if da_sh is None:
            return

        self.test(sh, da_sh)
        pass
    pass


# =======================================================================
if __name__ == '__main__':
    # app = Application()
    # app.run()

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
# =======================================================================