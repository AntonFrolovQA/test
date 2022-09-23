# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\c.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculatorForm(object):
    def setupUi(self, CalculatorForm):
        CalculatorForm.setObjectName("CalculatorForm")
        CalculatorForm.resize(360, 395)
        CalculatorForm.setStyleSheet("QWidget {\n"
"    background-color:black;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color:white;\n"
"    width:75px;\n"
"    height:75px;\n"
"    font-size:35px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:lightgreen;\n"
"    width:77px;\n"
"    height:77px;\n"
"    font-size:40px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:pink;\n"
"    width:72px;\n"
"    height:72px;\n"
"    font-size:35px;\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(CalculatorForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 341, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_4.setObjectName("Button_4")
        self.gridLayout.addWidget(self.Button_4, 1, 0, 1, 1)
        self.Button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_8.setObjectName("Button_8")
        self.gridLayout.addWidget(self.Button_8, 0, 1, 1, 1)
        self.Button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_1.setObjectName("Button_1")
        self.gridLayout.addWidget(self.Button_1, 3, 0, 1, 1)
        self.Button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_3.setObjectName("Button_3")
        self.gridLayout.addWidget(self.Button_3, 3, 2, 1, 1)
        self.Button_Devide = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Devide.setStyleSheet("background-color:yellow;")
        self.Button_Devide.setObjectName("Button_Devide")
        self.gridLayout.addWidget(self.Button_Devide, 4, 3, 1, 1)
        self.Button_Plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Plus.setStyleSheet("background-color:yellow;")
        self.Button_Plus.setObjectName("Button_Plus")
        self.gridLayout.addWidget(self.Button_Plus, 4, 1, 1, 1)
        self.Button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_9.setObjectName("Button_9")
        self.gridLayout.addWidget(self.Button_9, 0, 2, 1, 1)
        self.Button_Multiply = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Multiply.setStyleSheet("background-color:yellow;")
        self.Button_Multiply.setObjectName("Button_Multiply")
        self.gridLayout.addWidget(self.Button_Multiply, 3, 3, 1, 1)
        self.Button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_5.setObjectName("Button_5")
        self.gridLayout.addWidget(self.Button_5, 1, 1, 1, 1)
        self.Button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_2.setObjectName("Button_2")
        self.gridLayout.addWidget(self.Button_2, 3, 1, 1, 1)
        self.Button_Minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Minus.setStyleSheet("background-color:yellow;")
        self.Button_Minus.setObjectName("Button_Minus")
        self.gridLayout.addWidget(self.Button_Minus, 4, 2, 1, 1)
        self.Button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_7.setObjectName("Button_7")
        self.gridLayout.addWidget(self.Button_7, 0, 0, 1, 1)
        self.Button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_6.setObjectName("Button_6")
        self.gridLayout.addWidget(self.Button_6, 1, 2, 1, 1)
        self.Button_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_0.setObjectName("Button_0")
        self.gridLayout.addWidget(self.Button_0, 4, 0, 1, 1)
        self.Button_Equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Equal.setStyleSheet("background-color:green;")
        self.Button_Equal.setObjectName("Button_Equal")
        self.gridLayout.addWidget(self.Button_Equal, 0, 3, 1, 1)
        self.Button_Float = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_Float.setStyleSheet("background-color:yellow;")
        self.Button_Float.setObjectName("Button_Float")
        self.gridLayout.addWidget(self.Button_Float, 1, 3, 1, 1)
        self.ShowResultSpace = QtWidgets.QLineEdit(CalculatorForm)
        self.ShowResultSpace.setGeometry(QtCore.QRect(10, 10, 251, 51))
        self.ShowResultSpace.setStyleSheet("background-color:white;\n"
"font-size:25px;")
        self.ShowResultSpace.setObjectName("ShowResultSpace")
        self.Button_C = QtWidgets.QPushButton(CalculatorForm)
        self.Button_C.setGeometry(QtCore.QRect(270, 10, 81, 51))
        self.Button_C.setStyleSheet("background-color:red;")
        self.Button_C.setObjectName("Button_C")

        self.retranslateUi(CalculatorForm)
        QtCore.QMetaObject.connectSlotsByName(CalculatorForm)

    def retranslateUi(self, CalculatorForm):
        _translate = QtCore.QCoreApplication.translate
        CalculatorForm.setWindowTitle(_translate("CalculatorForm", "Form"))
        self.Button_4.setText(_translate("CalculatorForm", "4"))
        self.Button_8.setText(_translate("CalculatorForm", "8"))
        self.Button_1.setText(_translate("CalculatorForm", "1"))
        self.Button_3.setText(_translate("CalculatorForm", "3"))
        self.Button_Devide.setText(_translate("CalculatorForm", ":"))
        self.Button_Plus.setText(_translate("CalculatorForm", "+"))
        self.Button_9.setText(_translate("CalculatorForm", "9"))
        self.Button_Multiply.setText(_translate("CalculatorForm", "x"))
        self.Button_5.setText(_translate("CalculatorForm", "5"))
        self.Button_2.setText(_translate("CalculatorForm", "2"))
        self.Button_Minus.setText(_translate("CalculatorForm", "-"))
        self.Button_7.setText(_translate("CalculatorForm", "7"))
        self.Button_6.setText(_translate("CalculatorForm", "6"))
        self.Button_0.setText(_translate("CalculatorForm", "0"))
        self.Button_Equal.setText(_translate("CalculatorForm", "="))
        self.Button_Float.setText(_translate("CalculatorForm", ","))
        self.Button_C.setText(_translate("CalculatorForm", "C"))


