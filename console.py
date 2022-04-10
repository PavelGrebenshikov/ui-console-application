# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 801, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_output = QLabel(self.verticalLayoutWidget)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setStyleSheet(u"font-size: 18px;\n"
"font-family: sans-serif;")
        self.label_output.setTextFormat(Qt.AutoText)
        self.label_output.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_output)

        self.input_text = QLineEdit(self.verticalLayoutWidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setStyleSheet(u"height: 50px;")

        self.verticalLayout.addWidget(self.input_text)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 400, 411, 161))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.radio_read_to_file = QRadioButton(self.gridLayoutWidget)
        self.radio_read_to_file.setObjectName(u"radio_read_to_file")

        self.gridLayout.addWidget(self.radio_read_to_file, 3, 0, 1, 1)

        self.radio_list_files = QRadioButton(self.gridLayoutWidget)
        self.radio_list_files.setObjectName(u"radio_list_files")

        self.gridLayout.addWidget(self.radio_list_files, 4, 0, 1, 1)

        self.radio_remove_list = QRadioButton(self.gridLayoutWidget)
        self.radio_remove_list.setObjectName(u"radio_remove_list")

        self.gridLayout.addWidget(self.radio_remove_list, 0, 0, 1, 1)

        self.radio_write_to_file = QRadioButton(self.gridLayoutWidget)
        self.radio_write_to_file.setObjectName(u"radio_write_to_file")

        self.gridLayout.addWidget(self.radio_write_to_file, 2, 0, 1, 1)

        self.radio_bubble = QRadioButton(self.gridLayoutWidget)
        self.radio_bubble.setObjectName(u"radio_bubble")

        self.gridLayout.addWidget(self.radio_bubble, 1, 0, 1, 1)

        self.radio_quick_sort = QRadioButton(self.gridLayoutWidget)
        self.radio_quick_sort.setObjectName(u"radio_quick_sort")

        self.gridLayout.addWidget(self.radio_quick_sort, 0, 1, 1, 1)

        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(420, 400, 381, 161))
        self.button_start.setStyleSheet(u"font-size: 24px;\n"
"font-family: sans-serif;\n"
"\n"
"\n"
"QPushButton::hover {\n"
"	color: #fff;\n"
"	background-color: #222;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_output.setText("")
        self.radio_read_to_file.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0434 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.radio_list_files.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.radio_remove_list.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c \u0432\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u0441\u043f\u0438\u0441\u043a\u0438", None))
        self.radio_write_to_file.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c \u0432 \u0444\u0430\u0439\u043b", None))
        self.radio_bubble.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u0443\u0437\u044b\u0440\u044c\u043a\u043e\u043c", None))
        self.radio_quick_sort.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u0430\u044f \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
    # retranslateUi

