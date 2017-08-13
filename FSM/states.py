# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'states.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 450)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_3.setGeometry(QtCore.QRect(560, 70, 91, 81))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1.setGeometry(QtCore.QRect(110, 70, 91, 81))
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 40, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(340, 70, 91, 81))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(580, 40, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(130, 40, 55, 16))
        self.label_1.setObjectName("label_1")
        self.status_msg = QtWidgets.QListWidget(Form)
        self.status_msg.setGeometry(QtCore.QRect(110, 170, 541, 192))
        self.status_msg.setObjectName("status_msg")
        self.pushButton_start = QtWidgets.QPushButton(Form)
        self.pushButton_start.setGeometry(QtCore.QRect(110, 380, 93, 28))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_1 = QtWidgets.QCheckBox(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(210, 130, 101, 20))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QCheckBox(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 130, 101, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QCheckBox(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 390, 101, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lbl_FSM_States = QtWidgets.QLabel(Form)
        self.lbl_FSM_States.setGeometry(QtCore.QRect(330, 370, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_FSM_States.setFont(font)
        self.lbl_FSM_States.setObjectName("lbl_FSM_States")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "B"))
        self.label_3.setText(_translate("Form", "C"))
        self.label_1.setText(_translate("Form", "A"))
        self.pushButton_start.setText(_translate("Form", "start"))
        self.pushButton_1.setText(_translate("Form", "Transition AB"))
        self.pushButton_2.setText(_translate("Form", "Transition BC"))
        self.pushButton_3.setText(_translate("Form", "Enable FSM"))
        self.lbl_FSM_States.setText(_translate("Form", "FSM state...."))

