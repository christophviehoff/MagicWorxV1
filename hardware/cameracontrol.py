# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameracontrol.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Controller(object):
    def setupUi(self, Controller):
        Controller.setObjectName("Controller")
        Controller.setEnabled(True)
        Controller.resize(1089, 770)
        self.pb_capture = QtWidgets.QPushButton(Controller)
        self.pb_capture.setGeometry(QtCore.QRect(30, 730, 75, 23))
        self.pb_capture.setObjectName("pb_capture")
        self.heartbeat = QtWidgets.QPushButton(Controller)
        self.heartbeat.setEnabled(True)
        self.heartbeat.setGeometry(QtCore.QRect(510, 730, 10, 10))
        self.heartbeat.setStyleSheet("#heartbeat{\n"
"border-radius:12px}\n"
"\n"
"#heartbeat:enabled{\n"
"background:orange}\n"
"\n"
"#heartbeat:!enabled{\n"
"background:rgb(240, 240, 240)}")
        self.heartbeat.setText("")
        self.heartbeat.setObjectName("heartbeat")
        self.lcd_update_time = QtWidgets.QLCDNumber(Controller)
        self.lcd_update_time.setGeometry(QtCore.QRect(120, 730, 64, 23))
        self.lcd_update_time.setSmallDecimalPoint(True)
        self.lcd_update_time.setDigitCount(4)
        self.lcd_update_time.setObjectName("lcd_update_time")
        self.pb_live = QtWidgets.QPushButton(Controller)
        self.pb_live.setGeometry(QtCore.QRect(300, 730, 75, 23))
        self.pb_live.setObjectName("pb_live")
        self.pb_update = QtWidgets.QPushButton(Controller)
        self.pb_update.setGeometry(QtCore.QRect(190, 730, 75, 23))
        self.pb_update.setObjectName("pb_update")
        self.groupBox = QtWidgets.QGroupBox(Controller)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 520, 700))
        self.groupBox.setObjectName("groupBox")
        self.videoFrame = QtWidgets.QLabel(self.groupBox)
        self.videoFrame.setGeometry(QtCore.QRect(20, 30, 480, 640))
        self.videoFrame.setObjectName("videoFrame")
        self.groupBox_2 = QtWidgets.QGroupBox(Controller)
        self.groupBox_2.setGeometry(QtCore.QRect(550, 20, 520, 700))
        self.groupBox_2.setObjectName("groupBox_2")
        self.imageFrame = QtWidgets.QLabel(self.groupBox_2)
        self.imageFrame.setGeometry(QtCore.QRect(10, 30, 480, 101))
        self.imageFrame.setObjectName("imageFrame")
        self.gcv_result = QtWidgets.QLabel(self.groupBox_2)
        self.gcv_result.setGeometry(QtCore.QRect(10, 140, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gcv_result.setFont(font)
        self.gcv_result.setObjectName("gcv_result")
        self.groupBox.raise_()
        self.pb_capture.raise_()
        self.heartbeat.raise_()
        self.lcd_update_time.raise_()
        self.pb_live.raise_()
        self.pb_update.raise_()
        self.groupBox_2.raise_()

        self.retranslateUi(Controller)
        QtCore.QMetaObject.connectSlotsByName(Controller)

    def retranslateUi(self, Controller):
        _translate = QtCore.QCoreApplication.translate
        Controller.setWindowTitle(_translate("Controller", "Controller"))
        self.pb_capture.setText(_translate("Controller", "capture"))
        self.pb_live.setText(_translate("Controller", "document"))
        self.pb_update.setText(_translate("Controller", "update!"))
        self.groupBox.setTitle(_translate("Controller", "live Video"))
        self.videoFrame.setText(_translate("Controller", "video frame"))
        self.groupBox_2.setTitle(_translate("Controller", "snapshot--> Gvision"))
        self.imageFrame.setText(_translate("Controller", "image frame"))
        self.gcv_result.setText(_translate("Controller", "Google Cloud Vision Results"))

