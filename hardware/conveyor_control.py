# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conveyor_control.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Controller(object):
    def setupUi(self, Controller):
        Controller.setObjectName("Controller")
        Controller.resize(854, 707)
        self.conveyor_status = QtWidgets.QListWidget(Controller)
        self.conveyor_status.setGeometry(QtCore.QRect(390, 20, 451, 281))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        self.conveyor_status.setFont(font)
        self.conveyor_status.setStyleSheet("#conveyor_status{\n"
"border: 3px solid gray;\n"
"border-radius:12px;\n"
"background:rgb(255,255,127)}")
        self.conveyor_status.setFlow(QtWidgets.QListView.TopToBottom)
        self.conveyor_status.setBatchSize(10)
        self.conveyor_status.setObjectName("conveyor_status")
        self.pb_clear = QtWidgets.QPushButton(Controller)
        self.pb_clear.setGeometry(QtCore.QRect(390, 300, 171, 51))
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
        self.heartbeat = QtWidgets.QPushButton(Controller)
        self.heartbeat.setEnabled(False)
        self.heartbeat.setGeometry(QtCore.QRect(820, 270, 10, 10))
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
        self.controlsBox = QtWidgets.QGroupBox(Controller)
        self.controlsBox.setGeometry(QtCore.QRect(10, 20, 371, 181))
        self.controlsBox.setObjectName("controlsBox")
        self.pb_rev = QtWidgets.QPushButton(self.controlsBox)
        self.pb_rev.setGeometry(QtCore.QRect(10, 40, 51, 51))
        self.pb_rev.setObjectName("pb_rev")
        self.pb_stop = QtWidgets.QPushButton(self.controlsBox)
        self.pb_stop.setGeometry(QtCore.QRect(80, 40, 51, 51))
        self.pb_stop.setObjectName("pb_stop")
        self.pb_fwd = QtWidgets.QPushButton(self.controlsBox)
        self.pb_fwd.setGeometry(QtCore.QRect(150, 40, 51, 51))
        self.pb_fwd.setObjectName("pb_fwd")
        self.pb_reset = QtWidgets.QPushButton(self.controlsBox)
        self.pb_reset.setGeometry(QtCore.QRect(80, 110, 51, 51))
        self.pb_reset.setObjectName("pb_reset")
        self.pb_estop = QtWidgets.QPushButton(self.controlsBox)
        self.pb_estop.setGeometry(QtCore.QRect(230, 40, 121, 121))
        self.pb_estop.setObjectName("pb_estop")
        self.simulationBox = QtWidgets.QGroupBox(Controller)
        self.simulationBox.setGeometry(QtCore.QRect(10, 210, 211, 241))
        self.simulationBox.setObjectName("simulationBox")
        self.chk_enable = QtWidgets.QCheckBox(self.simulationBox)
        self.chk_enable.setGeometry(QtCore.QRect(10, 110, 121, 41))
        self.chk_enable.setBaseSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_enable.setFont(font)
        self.chk_enable.setStyleSheet("QCheckBox::indicator {\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"")
        self.chk_enable.setIconSize(QtCore.QSize(28, 28))
        self.chk_enable.setTristate(False)
        self.chk_enable.setObjectName("chk_enable")
        self.chk_dispense = QtWidgets.QCheckBox(self.simulationBox)
        self.chk_dispense.setGeometry(QtCore.QRect(10, 150, 121, 51))
        self.chk_dispense.setBaseSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_dispense.setFont(font)
        self.chk_dispense.setStyleSheet("QCheckBox::indicator {\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"")
        self.chk_dispense.setIconSize(QtCore.QSize(28, 28))
        self.chk_dispense.setTristate(False)
        self.chk_dispense.setObjectName("chk_dispense")
        self.chk_eject = QtWidgets.QCheckBox(self.simulationBox)
        self.chk_eject.setGeometry(QtCore.QRect(10, 200, 121, 31))
        self.chk_eject.setBaseSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chk_eject.setFont(font)
        self.chk_eject.setStyleSheet("QCheckBox::indicator {\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"")
        self.chk_eject.setIconSize(QtCore.QSize(28, 28))
        self.chk_eject.setTristate(False)
        self.chk_eject.setObjectName("chk_eject")
        self.pb_conveyor_thread = QtWidgets.QPushButton(self.simulationBox)
        self.pb_conveyor_thread.setGeometry(QtCore.QRect(10, 20, 191, 61))
        self.pb_conveyor_thread.setCheckable(True)
        self.pb_conveyor_thread.setObjectName("pb_conveyor_thread")
        self.lbl_conveyor_FSM = QtWidgets.QLabel(self.simulationBox)
        self.lbl_conveyor_FSM.setGeometry(QtCore.QRect(10, 90, 191, 20))
        self.lbl_conveyor_FSM.setObjectName("lbl_conveyor_FSM")
        self.chk_enable.raise_()
        self.chk_dispense.raise_()
        self.chk_eject.raise_()
        self.pb_conveyor_thread.raise_()
        self.lbl_conveyor_FSM.raise_()
        self.sensorBox = QtWidgets.QGroupBox(Controller)
        self.sensorBox.setGeometry(QtCore.QRect(230, 210, 151, 80))
        self.sensorBox.setObjectName("sensorBox")
        self.lcd_breakbeam = QtWidgets.QLCDNumber(self.sensorBox)
        self.lcd_breakbeam.setGeometry(QtCore.QRect(10, 20, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lcd_breakbeam.setFont(font)
        self.lcd_breakbeam.setToolTipDuration(0)
        self.lcd_breakbeam.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.lcd_breakbeam.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_breakbeam.setLineWidth(1)
        self.lcd_breakbeam.setMidLineWidth(0)
        self.lcd_breakbeam.setDigitCount(1)
        self.lcd_breakbeam.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_breakbeam.setProperty("value", 0.0)
        self.lcd_breakbeam.setProperty("intValue", 0)
        self.lcd_breakbeam.setObjectName("lcd_breakbeam")
        self.lcd_idxcounter = QtWidgets.QLCDNumber(self.sensorBox)
        self.lcd_idxcounter.setGeometry(QtCore.QRect(40, 20, 91, 41))
        self.lcd_idxcounter.setObjectName("lcd_idxcounter")
        self.trackingBox = QtWidgets.QGroupBox(Controller)
        self.trackingBox.setGeometry(QtCore.QRect(10, 470, 831, 201))
        self.trackingBox.setObjectName("trackingBox")
        self.pos_0 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_0.setEnabled(True)
        self.pos_0.setGeometry(QtCore.QRect(10, 60, 25, 91))
        self.pos_0.setStyleSheet("#pos_0{\n"
"border-radius:1px}\n"
"\n"
"#pos_0:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_0:!enabled{\n"
"background :red}")
        self.pos_0.setObjectName("pos_0")
        self.pos_1 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_1.setEnabled(True)
        self.pos_1.setGeometry(QtCore.QRect(40, 60, 25, 91))
        self.pos_1.setStyleSheet("#pos_1{\n"
"border-radius:1px}\n"
"\n"
"#pos_1:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_1:!enabled{\n"
"background :red}")
        self.pos_1.setObjectName("pos_1")
        self.pos_2 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_2.setEnabled(True)
        self.pos_2.setGeometry(QtCore.QRect(70, 60, 25, 91))
        self.pos_2.setStyleSheet("#pos_2{\n"
"border-radius:1px}\n"
"\n"
"#pos_2:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_2:!enabled{\n"
"background :red}")
        self.pos_2.setObjectName("pos_2")
        self.pos_3 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_3.setEnabled(True)
        self.pos_3.setGeometry(QtCore.QRect(100, 60, 25, 91))
        self.pos_3.setStyleSheet("#pos_3{\n"
"border-radius:1px}\n"
"\n"
"#pos_3:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_3:!enabled{\n"
"background :red}")
        self.pos_3.setObjectName("pos_3")
        self.pos_4 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_4.setEnabled(True)
        self.pos_4.setGeometry(QtCore.QRect(130, 60, 25, 91))
        self.pos_4.setStyleSheet("#pos_4{\n"
"border-radius:1px}\n"
"\n"
"#pos_4:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_4:!enabled{\n"
"background :red}")
        self.pos_4.setObjectName("pos_4")
        self.pos_5 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_5.setEnabled(True)
        self.pos_5.setGeometry(QtCore.QRect(160, 60, 25, 91))
        self.pos_5.setStyleSheet("#pos_5{\n"
"border-radius:1px}\n"
"\n"
"#pos_5:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_5:!enabled{\n"
"background :red}")
        self.pos_5.setObjectName("pos_5")
        self.pos_6 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_6.setEnabled(True)
        self.pos_6.setGeometry(QtCore.QRect(190, 60, 25, 91))
        self.pos_6.setStyleSheet("#pos_6{\n"
"border-radius:1px}\n"
"\n"
"#pos_6:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_6:!enabled{\n"
"background :red}")
        self.pos_6.setObjectName("pos_6")
        self.pos_7 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_7.setEnabled(True)
        self.pos_7.setGeometry(QtCore.QRect(220, 60, 25, 91))
        self.pos_7.setStyleSheet("#pos_7{\n"
"border-radius:1px}\n"
"\n"
"#pos_7:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_7:!enabled{\n"
"background :red}")
        self.pos_7.setObjectName("pos_7")
        self.pos_8 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_8.setEnabled(True)
        self.pos_8.setGeometry(QtCore.QRect(250, 60, 25, 91))
        self.pos_8.setStyleSheet("#pos_8{\n"
"border-radius:1px}\n"
"\n"
"#pos_8:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_8:!enabled{\n"
"background :red}")
        self.pos_8.setObjectName("pos_8")
        self.pos_9 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_9.setEnabled(True)
        self.pos_9.setGeometry(QtCore.QRect(280, 60, 25, 91))
        self.pos_9.setStyleSheet("#pos_9{\n"
"border-radius:1px}\n"
"\n"
"#pos_9:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_9:!enabled{\n"
"background :red}")
        self.pos_9.setObjectName("pos_9")
        self.pos_10 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_10.setEnabled(True)
        self.pos_10.setGeometry(QtCore.QRect(310, 60, 25, 91))
        self.pos_10.setStyleSheet("#pos_10{\n"
"border-radius:1px}\n"
"\n"
"#pos_10:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_10:!enabled{\n"
"background :red}")
        self.pos_10.setObjectName("pos_10")
        self.pos_11 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_11.setEnabled(True)
        self.pos_11.setGeometry(QtCore.QRect(340, 60, 25, 91))
        self.pos_11.setStyleSheet("#pos_11{\n"
"border-radius:1px}\n"
"\n"
"#pos_11:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_11:!enabled{\n"
"background :red}")
        self.pos_11.setObjectName("pos_11")
        self.pos_12 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_12.setEnabled(True)
        self.pos_12.setGeometry(QtCore.QRect(370, 60, 25, 91))
        self.pos_12.setStyleSheet("#pos_12{\n"
"border-radius:1px}\n"
"\n"
"#pos_12:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_12:!enabled{\n"
"background :red}")
        self.pos_12.setObjectName("pos_12")
        self.pos_13 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_13.setEnabled(True)
        self.pos_13.setGeometry(QtCore.QRect(400, 60, 25, 91))
        self.pos_13.setStyleSheet("#pos_13{\n"
"border-radius:1px}\n"
"\n"
"#pos_13:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_13:!enabled{\n"
"background :red}")
        self.pos_13.setObjectName("pos_13")
        self.pos_14 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_14.setEnabled(True)
        self.pos_14.setGeometry(QtCore.QRect(430, 60, 25, 91))
        self.pos_14.setStyleSheet("#pos_14{\n"
"border-radius:1px}\n"
"\n"
"#pos_14:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_14:!enabled{\n"
"background :red}")
        self.pos_14.setObjectName("pos_14")
        self.pos_15 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_15.setEnabled(True)
        self.pos_15.setGeometry(QtCore.QRect(460, 60, 25, 91))
        self.pos_15.setStyleSheet("#pos_15{\n"
"border-radius:1px}\n"
"\n"
"#pos_15:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_15:!enabled{\n"
"background :red}")
        self.pos_15.setObjectName("pos_15")
        self.pos_16 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_16.setEnabled(True)
        self.pos_16.setGeometry(QtCore.QRect(490, 60, 25, 91))
        self.pos_16.setStyleSheet("#pos_16{\n"
"border-radius:1px}\n"
"\n"
"#pos_16:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_16:!enabled{\n"
"background :red}")
        self.pos_16.setObjectName("pos_16")
        self.pos_17 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_17.setEnabled(True)
        self.pos_17.setGeometry(QtCore.QRect(520, 60, 25, 91))
        self.pos_17.setStyleSheet("#pos_17{\n"
"border-radius:1px}\n"
"\n"
"#pos_17:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_17:!enabled{\n"
"background :red}")
        self.pos_17.setObjectName("pos_17")
        self.pos_18 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_18.setEnabled(True)
        self.pos_18.setGeometry(QtCore.QRect(550, 60, 25, 91))
        self.pos_18.setStyleSheet("#pos_18{\n"
"border-radius:1px}\n"
"\n"
"#pos_18:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_18:!enabled{\n"
"background :red}")
        self.pos_18.setObjectName("pos_18")
        self.pos_19 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_19.setEnabled(True)
        self.pos_19.setGeometry(QtCore.QRect(580, 60, 25, 91))
        self.pos_19.setStyleSheet("#pos_19{\n"
"border-radius:1px}\n"
"\n"
"#pos_19:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_19:!enabled{\n"
"background :red}")
        self.pos_19.setObjectName("pos_19")
        self.pos_20 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_20.setEnabled(True)
        self.pos_20.setGeometry(QtCore.QRect(610, 60, 25, 91))
        self.pos_20.setStyleSheet("#pos_20{\n"
"border-radius:1px}\n"
"\n"
"#pos_20:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_20:!enabled{\n"
"background :red}")
        self.pos_20.setObjectName("pos_20")
        self.pos_21 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_21.setEnabled(True)
        self.pos_21.setGeometry(QtCore.QRect(640, 60, 25, 91))
        self.pos_21.setStyleSheet("#pos_21{\n"
"border-radius:1px}\n"
"\n"
"#pos_21:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_21:!enabled{\n"
"background :red}")
        self.pos_21.setObjectName("pos_21")
        self.pos_22 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_22.setEnabled(True)
        self.pos_22.setGeometry(QtCore.QRect(670, 60, 25, 91))
        self.pos_22.setStyleSheet("#pos_22{\n"
"border-radius:1px}\n"
"\n"
"#pos_22:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_22:!enabled{\n"
"background :red}")
        self.pos_22.setObjectName("pos_22")
        self.pos_23 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_23.setEnabled(True)
        self.pos_23.setGeometry(QtCore.QRect(700, 60, 25, 91))
        self.pos_23.setStyleSheet("#pos_23{\n"
"border-radius:1px}\n"
"\n"
"#pos_23:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_23:!enabled{\n"
"background :red}")
        self.pos_23.setObjectName("pos_23")
        self.pos_24 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_24.setEnabled(True)
        self.pos_24.setGeometry(QtCore.QRect(730, 60, 25, 91))
        self.pos_24.setStyleSheet("#pos_24{\n"
"border-radius:1px}\n"
"\n"
"#pos_24:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_24:!enabled{\n"
"background :red}")
        self.pos_24.setObjectName("pos_24")
        self.pos_25 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_25.setEnabled(True)
        self.pos_25.setGeometry(QtCore.QRect(760, 60, 25, 91))
        self.pos_25.setStyleSheet("pos_25{\n"
"border-radius:1px}\n"
"\n"
"#pos_25:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_25:!enabled{\n"
"background :red}")
        self.pos_25.setObjectName("pos_25")
        self.pos_26 = QtWidgets.QPushButton(self.trackingBox)
        self.pos_26.setEnabled(True)
        self.pos_26.setGeometry(QtCore.QRect(790, 60, 25, 91))
        self.pos_26.setStyleSheet("#pos_26{\n"
"border-radius:1px}\n"
"\n"
"#pos_26:enabled{\n"
"background :green}\n"
"\n"
"\n"
"#pos_26:!enabled{\n"
"background :red}")
        self.pos_26.setObjectName("pos_26")
        self.label_2 = QtWidgets.QLabel(self.trackingBox)
        self.label_2.setGeometry(QtCore.QRect(440, 200, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.trackingBox)
        self.label.setGeometry(QtCore.QRect(400, 30, 25, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.trackingBox)
        self.label_3.setGeometry(QtCore.QRect(430, 30, 25, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.trackingBox)
        self.label_4.setGeometry(QtCore.QRect(460, 30, 25, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.trackingBox)
        self.label_5.setGeometry(QtCore.QRect(490, 30, 25, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.trackingBox)
        self.label_6.setGeometry(QtCore.QRect(520, 30, 25, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.trackingBox)
        self.label_7.setGeometry(QtCore.QRect(550, 30, 25, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.trackingBox)
        self.label_8.setGeometry(QtCore.QRect(610, 30, 25, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.trackingBox)
        self.label_9.setGeometry(QtCore.QRect(640, 30, 25, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.trackingBox)
        self.label_10.setGeometry(QtCore.QRect(670, 30, 25, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.trackingBox)
        self.label_11.setGeometry(QtCore.QRect(700, 30, 25, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.trackingBox)
        self.label_12.setGeometry(QtCore.QRect(730, 30, 25, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.trackingBox)
        self.label_13.setGeometry(QtCore.QRect(760, 30, 25, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.trackingBox)
        self.label_14.setGeometry(QtCore.QRect(400, 160, 25, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.trackingBox)
        self.label_15.setGeometry(QtCore.QRect(430, 160, 25, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.trackingBox)
        self.label_16.setGeometry(QtCore.QRect(460, 160, 25, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.trackingBox)
        self.label_17.setGeometry(QtCore.QRect(490, 160, 25, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.trackingBox)
        self.label_18.setGeometry(QtCore.QRect(520, 160, 25, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.trackingBox)
        self.label_19.setGeometry(QtCore.QRect(550, 160, 25, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.trackingBox)
        self.label_20.setGeometry(QtCore.QRect(610, 160, 25, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.trackingBox)
        self.label_21.setGeometry(QtCore.QRect(640, 160, 25, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.trackingBox)
        self.label_22.setGeometry(QtCore.QRect(670, 160, 25, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.trackingBox)
        self.label_23.setGeometry(QtCore.QRect(700, 160, 25, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.trackingBox)
        self.label_24.setGeometry(QtCore.QRect(730, 160, 25, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.trackingBox)
        self.label_25.setGeometry(QtCore.QRect(760, 160, 25, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.trackingBox)
        self.label_26.setGeometry(QtCore.QRect(130, 30, 25, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.trackingBox)
        self.label_27.setGeometry(QtCore.QRect(340, 30, 25, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.trackingBox)
        self.label_28.setGeometry(QtCore.QRect(790, 30, 25, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.sensorBox_2 = QtWidgets.QGroupBox(Controller)
        self.sensorBox_2.setGeometry(QtCore.QRect(230, 300, 151, 151))
        self.sensorBox_2.setObjectName("sensorBox_2")
        self.pb_get_dispensor_status = QtWidgets.QPushButton(self.sensorBox_2)
        self.pb_get_dispensor_status.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.pb_get_dispensor_status.setObjectName("pb_get_dispensor_status")
        self.lbl_dispense_status = QtWidgets.QLabel(self.sensorBox_2)
        self.lbl_dispense_status.setGeometry(QtCore.QRect(10, 60, 131, 20))
        self.lbl_dispense_status.setObjectName("lbl_dispense_status")
        self.trackingBox.raise_()
        self.controlsBox.raise_()
        self.conveyor_status.raise_()
        self.pb_clear.raise_()
        self.heartbeat.raise_()
        self.simulationBox.raise_()
        self.sensorBox.raise_()
        self.sensorBox_2.raise_()

        self.retranslateUi(Controller)
        self.conveyor_status.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Controller)

    def retranslateUi(self, Controller):
        _translate = QtCore.QCoreApplication.translate
        Controller.setWindowTitle(_translate("Controller", "Conveyor"))
        self.pb_clear.setText(_translate("Controller", "clear"))
        self.heartbeat.setToolTip(_translate("Controller", "heartbeat"))
        self.controlsBox.setTitle(_translate("Controller", "Conveyor"))
        self.pb_rev.setText(_translate("Controller", "REV"))
        self.pb_stop.setText(_translate("Controller", "STOP"))
        self.pb_fwd.setText(_translate("Controller", "FWD"))
        self.pb_reset.setText(_translate("Controller", "Reset"))
        self.pb_estop.setText(_translate("Controller", "Estop"))
        self.simulationBox.setTitle(_translate("Controller", "Simulation"))
        self.chk_enable.setText(_translate("Controller", "Enable"))
        self.chk_dispense.setText(_translate("Controller", "Dispense"))
        self.chk_eject.setText(_translate("Controller", "Eject"))
        self.pb_conveyor_thread.setText(_translate("Controller", "Conveyor thread"))
        self.lbl_conveyor_FSM.setText(_translate("Controller", "State"))
        self.sensorBox.setTitle(_translate("Controller", "Sensor"))
        self.lcd_breakbeam.setToolTip(_translate("Controller", "Card stuck sensor"))
        self.trackingBox.setTitle(_translate("Controller", "Tracking"))
        self.pos_0.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_0.setText(_translate("Controller", "0"))
        self.pos_1.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_1.setText(_translate("Controller", "1"))
        self.pos_2.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_2.setText(_translate("Controller", "2"))
        self.pos_3.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_3.setText(_translate("Controller", "3"))
        self.pos_4.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_4.setText(_translate("Controller", "4"))
        self.pos_5.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_5.setText(_translate("Controller", "5"))
        self.pos_6.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_6.setText(_translate("Controller", "6"))
        self.pos_7.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_7.setText(_translate("Controller", "7"))
        self.pos_8.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_8.setText(_translate("Controller", "8"))
        self.pos_9.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_9.setText(_translate("Controller", "9"))
        self.pos_10.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_10.setText(_translate("Controller", "10"))
        self.pos_11.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_11.setText(_translate("Controller", "11"))
        self.pos_12.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_12.setText(_translate("Controller", "12"))
        self.pos_13.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_13.setText(_translate("Controller", "13"))
        self.pos_14.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_14.setText(_translate("Controller", "14"))
        self.pos_15.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_15.setText(_translate("Controller", "15"))
        self.pos_16.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_16.setText(_translate("Controller", "16"))
        self.pos_17.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_17.setText(_translate("Controller", "17"))
        self.pos_18.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_18.setText(_translate("Controller", "18"))
        self.pos_19.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_19.setText(_translate("Controller", "19"))
        self.pos_20.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_20.setText(_translate("Controller", "20"))
        self.pos_21.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_21.setText(_translate("Controller", "21"))
        self.pos_22.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_22.setText(_translate("Controller", "22"))
        self.pos_23.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_23.setText(_translate("Controller", "23"))
        self.pos_24.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_24.setText(_translate("Controller", "24"))
        self.pos_25.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_25.setText(_translate("Controller", "25"))
        self.pos_26.setToolTip(_translate("Controller", "input green =on, red=off"))
        self.pos_26.setText(_translate("Controller", "26"))
        self.label_2.setText(_translate("Controller", "13"))
        self.label.setText(_translate("Controller", "Bin0"))
        self.label_3.setText(_translate("Controller", "Bin2"))
        self.label_4.setText(_translate("Controller", "Bin4"))
        self.label_5.setText(_translate("Controller", "Bin6"))
        self.label_6.setText(_translate("Controller", "Bin8"))
        self.label_7.setText(_translate("Controller", "Bin10"))
        self.label_8.setText(_translate("Controller", "Bin12"))
        self.label_9.setText(_translate("Controller", "Bin14"))
        self.label_10.setText(_translate("Controller", "Bin16"))
        self.label_11.setText(_translate("Controller", "Bin18"))
        self.label_12.setText(_translate("Controller", "Bin20"))
        self.label_13.setText(_translate("Controller", "Bin22"))
        self.label_14.setText(_translate("Controller", "Bin1"))
        self.label_15.setText(_translate("Controller", "Bin3"))
        self.label_16.setText(_translate("Controller", "Bin5"))
        self.label_17.setText(_translate("Controller", "Bin7"))
        self.label_18.setText(_translate("Controller", "Bin9"))
        self.label_19.setText(_translate("Controller", "Bin11"))
        self.label_20.setText(_translate("Controller", "Bin13"))
        self.label_21.setText(_translate("Controller", "Bin15"))
        self.label_22.setText(_translate("Controller", "Bin17"))
        self.label_23.setText(_translate("Controller", "Bin19"))
        self.label_24.setText(_translate("Controller", "Bin21"))
        self.label_25.setText(_translate("Controller", "Bin23"))
        self.label_26.setText(_translate("Controller", "Disp"))
        self.label_27.setText(_translate("Controller", "Cam"))
        self.label_28.setText(_translate("Controller", "END"))
        self.sensorBox_2.setTitle(_translate("Controller", "dispense"))
        self.pb_get_dispensor_status.setText(_translate("Controller", "request status"))
        self.lbl_dispense_status.setText(_translate("Controller", "State"))

