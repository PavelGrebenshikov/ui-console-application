from PySide2 import QtWidgets
from console import Ui_MainWindow
import sys
import os
import math
import ast

class ConsoleApplicaiton(QtWidgets.QMainWindow, Ui_MainWindow):
    # Конструктор класса
    def __init__(self):
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        # Показать наше окно
        self.show()


        self.button_start.clicked.connect(self.start)
    
    def start(self):
        if self.radio_remove_list.isChecked():
            self.remove_lists()
        elif self.radio_bubble.isChecked():
            self.bubble_algorithms()
        elif self.radio_write_to_file.isChecked():
            self.write_to_file()
        elif self.radio_read_to_file.isChecked():
            self.read_from_file()
        elif self.radio_quick_sort.isChecked():
            self.quick_sort()

    def bubble_algorithms(self):
        getValue = self.input_text.text().split(",")
        lst = [int(item) for item in getValue if isinstance(item, str)]
        for num in range(len(lst) - 1):
            for tnum in range(len(lst) - num - 1):
                if lst[tnum] > lst[tnum + 1]:
                    lst[tnum], lst[tnum + 1] = lst[tnum + 1], lst[tnum]
        self.label_output.setText(", ".join(map(str, lst)))
    
    def write_to_file(self):
        try:
            with open(file=os.getcwd() + "\\WIOpenfile.txt", mode="w", encoding="UTF-8") as file:
                file.write(self.input_text.text())
        except:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Произошла ошибка при записи в файл")
            msgBox.exec_()

    def read_from_file(self):
        try:
            with open(file=os.getcwd() + "\\WIOpenfile.txt", mode="r", encoding="UTF-8") as file:
                file.readlines()
        except:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Произошла ошибка при чтении файла")
            msgBox.exec_()

    def remove_lists(self):
        try:
            self.label_output.setText(str(sum(ast.literal_eval(self.input_text.text()), [])))
        except:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Формат ввода: [[20, 30, 40, 100], [20, 30, 50, 10]]")
            msgBox.exec_()

    def quick_sort(self):
        getValue = self.input_text.text().split(',')
        lst = [int(item) for item in getValue]
        less = []
        equal = []
        greater = []
        if len(lst) > 1:
            el = lst[0]
            for x in lst:
                if x < el:
                    less.append(x)
                elif x == el:
                    equal.append(x)
                elif x > el:
                    greater.append(x)
            self.label_output.setText(", ".join(map(str, sorted(less)+equal+sorted(greater))))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    console = ConsoleApplicaiton()
    console.setWindowTitle("Console application UI")
    sys.exit(app.exec_())