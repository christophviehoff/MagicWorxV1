# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'leds.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Controller(object):
    def setupUi(self, Controller):
        Controller.setObjectName("Controller")
        Controller.setEnabled(True)
        Controller.resize(619, 219)
        self.inputsP0 = QtWidgets.QGroupBox(Controller)
        self.inputsP0.setGeometry(QtCore.QRect(10, 60, 271, 71))
        self.inputsP0.setObjectName("inputsP0")
        self.led_7 = QtWidgets.QPushButton(self.inputsP0)
        self.led_7.setGeometry(QtCore.QRect(230, 30, 25, 25))
        self.led_7.setStyleSheet("#led_7{\n"
"border-radius:12px}\n"
"\n"
"#led_7:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_7:!enabled{\n"
"background :red}")
        self.led_7.setText("")
        self.led_7.setObjectName("led_7")
        self.led_6 = QtWidgets.QPushButton(self.inputsP0)
        self.led_6.setGeometry(QtCore.QRect(200, 30, 25, 25))
        self.led_6.setStyleSheet("#led_6{\n"
"border-radius:12px}\n"
"\n"
"#led_6:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_6:!enabled{\n"
"background :red}")
        self.led_6.setText("")
        self.led_6.setObjectName("led_6")
        self.led_4 = QtWidgets.QPushButton(self.inputsP0)
        self.led_4.setGeometry(QtCore.QRect(140, 30, 25, 25))
        self.led_4.setStyleSheet("#led_4{\n"
"border-radius:12px}\n"
"\n"
"#led_4:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_4:!enabled{\n"
"background :red}")
        self.led_4.setText("")
        self.led_4.setObjectName("led_4")
        self.led_0 = QtWidgets.QPushButton(self.inputsP0)
        self.led_0.setEnabled(True)
        self.led_0.setGeometry(QtCore.QRect(20, 30, 25, 25))
        self.led_0.setStyleSheet("#led_0{\n"
"border-radius:12px}\n"
"\n"
"#led_0:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_0:!enabled{\n"
"background :red}")
        self.led_0.setText("")
        self.led_0.setObjectName("led_0")
        self.led_1 = QtWidgets.QPushButton(self.inputsP0)
        self.led_1.setGeometry(QtCore.QRect(50, 30, 25, 25))
        self.led_1.setStyleSheet("#led_1{\n"
"border-radius:12px}\n"
"\n"
"#led_1:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_1:!enabled{\n"
"background :red}")
        self.led_1.setText("")
        self.led_1.setObjectName("led_1")
        self.led_2 = QtWidgets.QPushButton(self.inputsP0)
        self.led_2.setGeometry(QtCore.QRect(80, 30, 25, 25))
        self.led_2.setStyleSheet("#led_2{\n"
"border-radius:12px}\n"
"\n"
"#led_2:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_2:!enabled{\n"
"background :red}")
        self.led_2.setText("")
        self.led_2.setObjectName("led_2")
        self.led_3 = QtWidgets.QPushButton(self.inputsP0)
        self.led_3.setGeometry(QtCore.QRect(110, 30, 25, 25))
        self.led_3.setStyleSheet("#led_3{\n"
"border-radius:12px}\n"
"\n"
"#led_3:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_3:!enabled{\n"
"background :red}")
        self.led_3.setText("")
        self.led_3.setObjectName("led_3")
        self.led_5 = QtWidgets.QPushButton(self.inputsP0)
        self.led_5.setGeometry(QtCore.QRect(170, 30, 25, 25))
        self.led_5.setStyleSheet("#led_5{\n"
"border-radius:12px}\n"
"\n"
"#led_5:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_5:!enabled{\n"
"background :red}")
        self.led_5.setText("")
        self.led_5.setObjectName("led_5")
        self.led_7.raise_()
        self.led_6.raise_()
        self.led_4.raise_()
        self.led_1.raise_()
        self.led_2.raise_()
        self.led_3.raise_()
        self.led_5.raise_()
        self.led_0.raise_()
        self.inputsP1 = QtWidgets.QGroupBox(Controller)
        self.inputsP1.setGeometry(QtCore.QRect(10, 140, 271, 71))
        self.inputsP1.setObjectName("inputsP1")
        self.led_9 = QtWidgets.QPushButton(self.inputsP1)
        self.led_9.setGeometry(QtCore.QRect(50, 30, 25, 25))
        self.led_9.setStyleSheet("#led_9{\n"
"border-radius:12px}\n"
"\n"
"#led_9:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_9:!enabled{\n"
"background :red}")
        self.led_9.setText("")
        self.led_9.setObjectName("led_9")
        self.led_10 = QtWidgets.QPushButton(self.inputsP1)
        self.led_10.setGeometry(QtCore.QRect(80, 30, 25, 25))
        self.led_10.setStyleSheet("#led_10{\n"
"border-radius:12px}\n"
"\n"
"#led_10:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_10:!enabled{\n"
"background :red}")
        self.led_10.setText("")
        self.led_10.setObjectName("led_10")
        self.led_11 = QtWidgets.QPushButton(self.inputsP1)
        self.led_11.setGeometry(QtCore.QRect(110, 30, 25, 25))
        self.led_11.setStyleSheet("#led_11{\n"
"border-radius:12px}\n"
"\n"
"#led_11:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_11:!enabled{\n"
"background :red}")
        self.led_11.setText("")
        self.led_11.setObjectName("led_11")
        self.led_12 = QtWidgets.QPushButton(self.inputsP1)
        self.led_12.setGeometry(QtCore.QRect(140, 30, 25, 25))
        self.led_12.setStyleSheet("#led_12{\n"
"border-radius:12px}\n"
"\n"
"#led_12:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_12:!enabled{\n"
"background :red}")
        self.led_12.setText("")
        self.led_12.setObjectName("led_12")
        self.led_13 = QtWidgets.QPushButton(self.inputsP1)
        self.led_13.setGeometry(QtCore.QRect(170, 30, 25, 25))
        self.led_13.setStyleSheet("#led_13{\n"
"border-radius:12px}\n"
"\n"
"#led_13:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_13:!enabled{\n"
"background :red}")
        self.led_13.setText("")
        self.led_13.setObjectName("led_13")
        self.led_14 = QtWidgets.QPushButton(self.inputsP1)
        self.led_14.setGeometry(QtCore.QRect(200, 30, 25, 25))
        self.led_14.setStyleSheet("#led_14{\n"
"border-radius:12px}\n"
"\n"
"#led_14:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_14:!enabled{\n"
"background :red}")
        self.led_14.setText("")
        self.led_14.setObjectName("led_14")
        self.led_15 = QtWidgets.QPushButton(self.inputsP1)
        self.led_15.setEnabled(True)
        self.led_15.setGeometry(QtCore.QRect(230, 30, 25, 25))
        self.led_15.setStyleSheet("#led_15{\n"
"border-radius:12px}\n"
"\n"
"#led_15:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_15:!enabled{\n"
"background :red}")
        self.led_15.setText("")
        self.led_15.setObjectName("led_15")
        self.led_8 = QtWidgets.QPushButton(self.inputsP1)
        self.led_8.setGeometry(QtCore.QRect(20, 30, 25, 25))
        self.led_8.setStyleSheet("#led_8{\n"
"border-radius:12px}\n"
"\n"
"#led_8:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_8:!enabled{\n"
"background :red}")
        self.led_8.setText("")
        self.led_8.setObjectName("led_8")
        self.input_selector = QtWidgets.QComboBox(Controller)
        self.input_selector.setGeometry(QtCore.QRect(10, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_selector.setFont(font)
        self.input_selector.setObjectName("input_selector")
        self.input_selector.addItem("")
        self.input_selector.addItem("")
        self.input_selector.addItem("")
        self.input_selector.addItem("")
        self.input_selector.addItem("")
        self.input_selector.addItem("")
        self.heartbeat = QtWidgets.QPushButton(Controller)
        self.heartbeat.setEnabled(False)
        self.heartbeat.setGeometry(QtCore.QRect(590, 200, 10, 10))
        self.heartbeat.setAutoFillBackground(False)
        self.heartbeat.setStyleSheet("\n"
"#heartbeat {\n"
"border-radius:2px}\n"
"\n"
"#heartbeat:enabled {\n"
"background :yellow}\n"
"\n"
"#heartbeat:!enabled {\n"
"background: orange}\n"
"\n"
"")
        self.heartbeat.setText("")
        self.heartbeat.setCheckable(False)
        self.heartbeat.setChecked(False)
        self.heartbeat.setFlat(False)
        self.heartbeat.setObjectName("heartbeat")
        self.led_status = QtWidgets.QListWidget(Controller)
        self.led_status.setGeometry(QtCore.QRect(300, 20, 311, 141))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        self.led_status.setFont(font)
        self.led_status.setStyleSheet("#led_status{\n"
"border: 3px solid gray;\n"
"border-radius:12px;\n"
"background:rgb(255,255,127)}")
        self.led_status.setFlow(QtWidgets.QListView.TopToBottom)
        self.led_status.setBatchSize(10)
        self.led_status.setObjectName("led_status")
        self.pb_clear = QtWidgets.QPushButton(Controller)
        self.pb_clear.setGeometry(QtCore.QRect(300, 160, 171, 51))
        self.pb_clear.setStyleSheet("#pb_clear{\n"
"border: 3px solid gray;\n"
"border-radius:12px;\n"
"background:white\n"
"}")
        self.pb_clear.setCheckable(True)
        self.pb_clear.setChecked(False)
        self.pb_clear.setAutoRepeat(False)
        self.pb_clear.setAutoExclusive(True)
        self.pb_clear.setObjectName("pb_clear")
        self.inputsP1.raise_()
        self.inputsP0.raise_()
        self.input_selector.raise_()
        self.heartbeat.raise_()
        self.led_status.raise_()
        self.pb_clear.raise_()

        self.retranslateUi(Controller)
        self.led_status.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Controller)

    def retranslateUi(self, Controller):
        _translate = QtCore.QCoreApplication.translate
        Controller.setWindowTitle(_translate("Controller", "led display"))
        self.inputsP0.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.inputsP0.setTitle(_translate("Controller", "  Inputs P0.0 - 0.7"))
        self.led_7.setToolTip(_translate("Controller", "input bit 7"))
        self.led_6.setToolTip(_translate("Controller", "input bit 6"))
        self.led_4.setToolTip(_translate("Controller", "input bit 4"))
        self.led_0.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.led_1.setToolTip(_translate("Controller", "input bit 1"))
        self.led_2.setToolTip(_translate("Controller", "input bit 2"))
        self.led_3.setToolTip(_translate("Controller", "input bit 3"))
        self.led_5.setToolTip(_translate("Controller", "input bit 5"))
        self.inputsP1.setToolTip(_translate("Controller", "outputs green=on, red=off"))
        self.inputsP1.setTitle(_translate("Controller", "  Inputs P1.0 - 1.7"))
        self.led_9.setToolTip(_translate("Controller", "input bit 3"))
        self.led_10.setToolTip(_translate("Controller", "input bit 5"))
        self.led_11.setToolTip(_translate("Controller", "input bit 1"))
        self.led_12.setToolTip(_translate("Controller", "input bit 6"))
        self.led_13.setToolTip(_translate("Controller", "input bit 7"))
        self.led_14.setToolTip(_translate("Controller", "input bit 4"))
        self.led_15.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.led_8.setToolTip(_translate("Controller", "input bit 2"))
        self.input_selector.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.input_selector.setItemText(0, _translate("Controller", "0x20"))
        self.input_selector.setItemText(1, _translate("Controller", "0x21"))
        self.input_selector.setItemText(2, _translate("Controller", "0x22"))
        self.input_selector.setItemText(3, _translate("Controller", "0x23"))
        self.input_selector.setItemText(4, _translate("Controller", "0x24"))
        self.input_selector.setItemText(5, _translate("Controller", "0x25"))
        self.heartbeat.setToolTip(_translate("Controller", "heartbeat"))
        self.pb_clear.setText(_translate("Controller", "clear"))

