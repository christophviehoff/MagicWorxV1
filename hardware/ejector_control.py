# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejector_control.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Controller(object):
    def setupUi(self, Controller):
        Controller.setObjectName("Controller")
        Controller.resize(618, 336)
        self.bin_selector = QtWidgets.QComboBox(Controller)
        self.bin_selector.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bin_selector.setFont(font)
        self.bin_selector.setObjectName("bin_selector")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.bin_selector.addItem("")
        self.pb_clear = QtWidgets.QPushButton(Controller)
        self.pb_clear.setGeometry(QtCore.QRect(250, 280, 171, 51))
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
        self.ejector_status = QtWidgets.QListWidget(Controller)
        self.ejector_status.setGeometry(QtCore.QRect(250, 10, 361, 271))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        self.ejector_status.setFont(font)
        self.ejector_status.setStyleSheet("#led_status{\n"
"border: 3px solid gray;\n"
"border-radius:12px;\n"
"background:rgb(255,255,127)}")
        self.ejector_status.setFlow(QtWidgets.QListView.TopToBottom)
        self.ejector_status.setBatchSize(10)
        self.ejector_status.setObjectName("ejector_status")
        self.heartbeat = QtWidgets.QPushButton(Controller)
        self.heartbeat.setEnabled(False)
        self.heartbeat.setGeometry(QtCore.QRect(600, 320, 10, 10))
        self.heartbeat.setAutoFillBackground(False)
        self.heartbeat.setStyleSheet("\n"
"#heartbeat {\n"
"border-radius:2px}\n"
"\n"
"#heartbeat:enabled {\n"
"background :grey}\n"
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
        self.pb_eject = QtWidgets.QPushButton(Controller)
        self.pb_eject.setGeometry(QtCore.QRect(10, 50, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_eject.setFont(font)
        self.pb_eject.setObjectName("pb_eject")
        self.led_ready = QtWidgets.QPushButton(Controller)
        self.led_ready.setEnabled(True)
        self.led_ready.setGeometry(QtCore.QRect(10, 300, 25, 25))
        self.led_ready.setStyleSheet("#led_ready{\n"
"border-radius:12px}\n"
"\n"
"#led_ready:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#led_ready:!enabled{\n"
"background :red}")
        self.led_ready.setText("")
        self.led_ready.setObjectName("led_ready")
        self.label = QtWidgets.QLabel(Controller)
        self.label.setGeometry(QtCore.QRect(50, 300, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sliderA = QtWidgets.QSlider(Controller)
        self.sliderA.setGeometry(QtCore.QRect(10, 190, 231, 22))
        self.sliderA.setMinimum(150)
        self.sliderA.setMaximum(600)
        self.sliderA.setProperty("value", 150)
        self.sliderA.setOrientation(QtCore.Qt.Horizontal)
        self.sliderA.setObjectName("sliderA")
        self.sliderB = QtWidgets.QSlider(Controller)
        self.sliderB.setGeometry(QtCore.QRect(10, 230, 231, 22))
        self.sliderB.setMinimum(150)
        self.sliderB.setMaximum(600)
        self.sliderB.setProperty("value", 580)
        self.sliderB.setOrientation(QtCore.Qt.Horizontal)
        self.sliderB.setObjectName("sliderB")
        self.pb_eject_test = QtWidgets.QPushButton(Controller)
        self.pb_eject_test.setGeometry(QtCore.QRect(130, 50, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_eject_test.setFont(font)
        self.pb_eject_test.setObjectName("pb_eject_test")
        self.lcdNumber = QtWidgets.QLCDNumber(Controller)
        self.lcdNumber.setGeometry(QtCore.QRect(150, 250, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Controller)
        self.ejector_status.setCurrentRow(-1)
        self.sliderB.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(Controller)

    def retranslateUi(self, Controller):
        _translate = QtCore.QCoreApplication.translate
        Controller.setWindowTitle(_translate("Controller", "Ejector"))
        self.bin_selector.setToolTip(_translate("Controller", "<html><head/><body><p>Select a Bin.</p></body></html>"))
        self.bin_selector.setItemText(0, _translate("Controller", "Bin0"))
        self.bin_selector.setItemText(1, _translate("Controller", "Bin1"))
        self.bin_selector.setItemText(2, _translate("Controller", "Bin2"))
        self.bin_selector.setItemText(3, _translate("Controller", "Bin3"))
        self.bin_selector.setItemText(4, _translate("Controller", "Bin4"))
        self.bin_selector.setItemText(5, _translate("Controller", "Bin5"))
        self.bin_selector.setItemText(6, _translate("Controller", "Bin6"))
        self.bin_selector.setItemText(7, _translate("Controller", "Bin7"))
        self.bin_selector.setItemText(8, _translate("Controller", "Bin8"))
        self.bin_selector.setItemText(9, _translate("Controller", "Bin9"))
        self.bin_selector.setItemText(10, _translate("Controller", "Bin10"))
        self.bin_selector.setItemText(11, _translate("Controller", "Bin11"))
        self.bin_selector.setItemText(12, _translate("Controller", "Bin12"))
        self.bin_selector.setItemText(13, _translate("Controller", "Bin13"))
        self.bin_selector.setItemText(14, _translate("Controller", "Bin14"))
        self.bin_selector.setItemText(15, _translate("Controller", "Bin15"))
        self.bin_selector.setItemText(16, _translate("Controller", "Bin16"))
        self.bin_selector.setItemText(17, _translate("Controller", "Bin17"))
        self.bin_selector.setItemText(18, _translate("Controller", "Bin19"))
        self.bin_selector.setItemText(19, _translate("Controller", "Bin20"))
        self.bin_selector.setItemText(20, _translate("Controller", "Bin21"))
        self.bin_selector.setItemText(21, _translate("Controller", "Bin22"))
        self.bin_selector.setItemText(22, _translate("Controller", "Bin23"))
        self.pb_clear.setText(_translate("Controller", "clear"))
        self.heartbeat.setToolTip(_translate("Controller", "heartbeat"))
        self.pb_eject.setText(_translate("Controller", "Single eject"))
        self.led_ready.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.label.setText(_translate("Controller", "ready"))
        self.pb_eject_test.setText(_translate("Controller", "Sequence eject"))

