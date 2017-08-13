
#-*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from ioInterface import Ui_ioInterface
from transitions import Machine
from time import sleep

from Adafruit_MotorHAT import Adafruit_StepperMotor, Adafruit_MotorHAT
from hardware import conveyor, dispenser,stepper,expander,ejector,tof, i2cutil,piface

import wiringpi
import threading,subprocess,smbus
import time
import atexit

watchdog = False

#Constant declarations

#PiFace outputs
PIFACE_RELAY0=200  #LED0
PIFACE_RELAY1=201  #LED1
PIFACE_LED2=202
PIFACE_LED3=203
PIFACE_LED4=204
PIFACE_LED5=205
PIFACE_LED6=206
PIFACE_LED7=207  #used as board level heartbeat

#PiFace outputs
PIFACE_S0=208
PIFACE_S1=209
PIFACE_S2=210
PIFACE_S3=211

ON=1
OFF=0


#Help functions
def swEmergencyStop():
    # motorHAT i2c board1
    stepper1.e_stop()
    # conveyor release
    conveyor1.reset()

#stepper indexing passing stepper object, number of steps, direction and coil sytle
def stepper_worker(stepper, numsteps, direction, style):
    stepper.step(numsteps, direction, style)

#ejector passing GUI start stop angle
def ejector_worker(ejector,servoStart,servoStop):
    ejector.eject(servoStart,servoStop)

class EdgeTrigger(object):
    def __init__(self, callback):
        self.value = None
        self.callback = callback

    def __call__(self, value):
        #if value != self.value:
        #this one will trigger a 0 to 1 transition only
        if value < self.value:
            self.callback(self.value, value)
        self.value = value

#FSM definitions

class Conveyor_FSM(Machine):

    # states and transitions
    def __init__(self):
        self.running=True
        self.isEnabled = False
        self.isEjectEnabled = False
        self.isDispenseEnabled = False

        states = ['init', 'start', 'stop', 'dispense', 'eject']
        Machine.__init__(self, states=states, initial='init')

        self.add_transition('trigger', 'init', 'start', conditions='is_enabled')
        self.add_transition('trigger', 'start', 'stop', conditions='is_beam_broken')
        self.add_transition('trigger', 'stop', 'dispense', conditions='is_ready')
        self.add_transition('trigger', 'dispense', 'eject')
        self.add_transition('trigger', 'eject', 'start')

    # external transition control from GUI

    def shutdown(self):
        self.running=False

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    def enable_eject(self):
        self.isEjectEnabled = True

    def disable_eject(self):
        self.isEjectEnabled = False

    def enable_dispense(self):
        self.isDispenseEnabled = True

    def disable_dispense(self):
        self.isDispenseEnabled = False


    #what to do when you enter a state
    def on_enter_init(self):
        conveyor1.stop()

    def on_enter_start(self):
        conveyor1.fwd()
        sleep(.2)

    def on_enter_stop(self):
        conveyor1.stop()

    def on_enter_dispense(self):
        if self.isDispenseEnabled:
            dispenserUSB0.dispense(dispenser.connect_to_serial_port(dispenser.list_of_serial_ports()))
        else:
            sleep(1) #slow down for testing

    def on_enter_eject(self):
        if self.isEjectEnabled:
            ejector1.eject(150, 600)
        else:
            sleep(1) #slow down for testing

    #transition conditions

    def is_enabled(self):
        return self.isEnabled

    def is_disabled(self):
        return not self.isEnabled


    def is_beam_broken(self):
        return not wiringpi.digitalRead(212)  #break beam sensor wiringpi.digitalRead(15)

    def is_ready(self):
        return True

        #bypass right now when not connected
        #return dispenserUSB0.is_ready(dispenser.connect_to_serial_port(dispenser.list_of_serial_ports()))

class Bin_FSM(Machine):

    # states and transitions
    def __init__(self, name, high_limit_pin, low_limit_pin, level_limit_pin):
        self.name = name
        self.running=True

        #gui controlled
        self.isEnabled=False

        #tof distance sensor data
        self.distance=0
        self.high_limit=0
        self.ready_limit=100
        self.low_limit=600

        #hardware pin assignments
        self.high_level_pin = high_limit_pin  #65
        self.low_level_pin = low_limit_pin   #66
        self.level_limit_pin = level_limit_pin #81

        self.stepper = stepper.Stepper("Bin-1", 0x60, 1, 65, 66, 81)  # generic stepper object

        states = ['init', 'start', 'up', 'down']
        Machine.__init__(self, states=states, initial='init')

        self.add_transition('trigger', 'init', 'start',conditions='is_enabled')
        self.add_transition('trigger', 'start', 'down')
        self.add_transition('trigger', 'down', 'down', unless='is_low_limit') #loop
        self.add_transition('trigger', 'down', 'up', conditions='is_low_limit')
        self.add_transition('trigger', 'up', 'up', unless='is_high_level') #loop is high_level
        self.add_transition('trigger', 'up', 'down', conditions='is_high_level') #same as loop condittion
        self.add_transition('trigger', 'up', 'down', conditions='is_high_limit')


    # external transition control from GUI

    def shutdown(self):
        self.running = False

    def enable(self):
        self.isEnabled = True

    def disable(self):
        self.isEnabled = False

    # set GUI parameter for distance sensor limits

    def set_high_limit(self,value):
        self.high_limit=value

    def set_ready_limit(self,value):
        self.ready_limit=value

    def set_low_limit(self,value):
        self.low_limit=value

    #state machine task and transitions

    def on_enter_init(self):
        self.stepper.stop()

    def on_enter_start(self):
        self.stepper.stop()

    def on_enter_up(self):
        #while not wiringpi.digitalRead(self.high_level_pin) and wiringpi.digitalRead(self.level_limit_pin) :
        self.stepper.oneStep_up()

    def on_enter_down(self):
        # while not wiringpi.digitalRead(self.low_level_pin) :
        self.stepper.oneStep_down()

    #transitions

    def is_enabled(self):
        return self.isEnabled

    def is_disabled(self):
        return not self.isEnabled

    def is_high_limit(self):
        return wiringpi.digitalRead(self.high_level_pin)

    def is_low_limit(self):
        return wiringpi.digitalRead(self.low_level_pin)

    def is_high_level(self):
        return wiringpi.digitalRead(self.high_level_pin)\
               or not wiringpi.digitalRead(self.level_limit_pin) # or tof_sensor1.get_distance() <= self.ready_limit

    def is_distance_ready(self):
        return tof_sensor1.get_distance() < self.ready_limit

#main GUI program
class MyGuiProgram(Ui_ioInterface):

    def __init__(self, dialog):
        Ui_ioInterface.__init__(self)
        self.setupUi(dialog)

        # create state machine
        self.belt = Conveyor_FSM()
        self.bin1 = Bin_FSM( 1, 65, 66, 81)   #bin number,high_limit_pin,low_limit_pinl,lvl_limit_pin for control logic
        self.running = True

        #just for run method in seperate Thread
        self.stepper1 = stepper.Stepper("Bin-1", 0x60, 1, 65, 66, 81)

        #register callbacks for button events
        #dispenser buttons
        self.btnDispense.clicked.connect(self.cb_dispense)
        self.btnGetStatus.clicked.connect(self.cb_get_status)
        self.btnReset.clicked.connect(self.cb_reset_card_dispenser)
        self.btnInit.clicked.connect(self.cb_write_hold_card)

        #stepper buttons
        self.btnUP.clicked.connect(self.cb_up)
        self.btnDN.clicked.connect(self.cb_down)

        #ejector buttons
        self.btnEject.clicked.connect(self.cb_eject)

        #Relay board conveyor control buttons
        self.btnFwd.clicked.connect(self.cb_fwd)
        self.btnStop.clicked.connect(self.cb_stop)
        self.btnRev.clicked.connect(self.cb_rev)
        self.btnReset.clicked.connect(self.cb_reset)

        #start thread from UI

        self.btnAUTO_THREAD.clicked.connect(self.cb_bin1_thread)
        self.btnMANUAL_THREAD.clicked.connect(self.cb_manual_thread)
        self.btnCONVEYOR_THREAD.clicked.connect(self.cb_conveyor_thread)

        # register 0 to 1 'rising edge'  edge detector callback
        self.detector_bin1_stuck = EdgeTrigger(self.cb_bin1_card_stuck)
        self.detector_bin1_high_limit = EdgeTrigger(self.cb_bin1_high_limit)
        self.detector_bin1_low_limit = EdgeTrigger(self.cb_bin1_low_limit)
        self.detector_conveyor_index= EdgeTrigger(self.cb_conveyor_index)
        self.detector_bin1_level_limit = EdgeTrigger(self.cb_bin1_level_limit)

        # max counts interleaved mode for progress bar display
        self.cnt_max=6000
        self.cnt=0
        self.idxcount=0

        #self.bin1.run()  #run bin1 thread method
        self.stepper1.start()

        #threads get started here
    def cb_auto_thread(self):
        #tauto = threading.Thread()
        tAuto = threading.Thread(name="EjectorBin1 AUTO started", target=self.run_bin1_FSM)
        tAuto.daemon=True
        tAuto.start()

    def cb_manual_thread(self):
        #tmanual = threading.Thread()
        tManual = threading.Thread(name="EjectorBin1 MANUAL started", target=self.stepper)
        tManual.daemon=True
        tManual.start()

    def cb_conveyor_thread(self):
        # tConveyor = threading.Thread()
        tConveyor = threading.Thread(name="Conveyor started", target=self.run_conveyor_FSM)
        tConveyor.daemon = True
        tConveyor.start()

    def cb_bin1_thread(self):
        # tConveyor = threading.Thread()
        tBin1 = threading.Thread(name="Bin started", target=self.run_bin1_FSM)
        tBin1.daemon = True
        tBin1.start()


    #run Finite State maxchines

    def shutdown(self):
        self.running = False

    def run_conveyor_FSM(self):
        txt = threading.currentThread().getName()
        self.Input_Status.addItem(txt)

        while self.running:

            if self.btnEnableDispense.isChecked():
                self.belt.enable_dispense()
            else:
                self.belt.disable_dispense()

            if self.btnEnableEject.isChecked():
                self.belt.enable_eject()
            else:
                self.belt.disable_eject()

            if self.btnEnable.isChecked():
                self.belt.enable()
                self.belt.trigger()
            else:
                self.belt.disable()
                self.belt.to_init()
                sleep(.5)

    def run_bin1_FSM(self):
        self.cnt = 0
        txt = threading.currentThread().getName()
        self.Input_Status.addItem(txt)

        while self.running:

            #reset counter at high or low limit
            if wiringpi.digitalRead(65) or wiringpi.digitalRead(66):
                self.cnt=0

            # indexing counter display based on state
            if self.bin1.is_up() and self.btnEnableCycle.isChecked():
                self.cnt +=1
                self.CycleCountBin1.display(self.cnt)
                self.bin1Level.setValue(self.cnt)
                # self.progressBar.setValue(self.cnt)

            if self.bin1.is_down() and self.btnEnableCycle.isChecked():
                self.cnt -= 1
                self.CycleCountBin1.display(self.cnt)
                self.bin1Level.setValue(self.cnt + self.cnt_max)
                # self.progressBar.setValue(self.cnt + self.cnt_max)

            if self.btnEnableCycle.isChecked():
                self.bin1.enable()   # enable initial transitions
                self.bin1.trigger()
            else:
                self.bin1.disable()
                sleep(.5)

    #callbacks from button presses
    #manual indexing of stepper and ejector via a thread to not interrupt GUI

    def cb_up(self):
        txt = "stepper up event triggered!"
        self.Input_Status.addItem(txt)
        st1 = threading.Thread(name="my up thread",target=stepper_worker,
                               args=(stepper1, 4, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE))
        st1.start()

    def cb_down(self):
        txt = "stepper dn event triggered!"
        self.Input_Status.addItem(txt)
        st1 = threading.Thread(name="my dn thread",target=stepper_worker,
                               args=(stepper1, 4, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE))
        st1.start()

    def cb_eject(self):
        # manual ejector control (passing GUI elements)
        txt = "ejector event triggered!"
        self.Input_Status.addItem(txt)
        st1 = threading.Thread(name="my ejector thread", target=ejector_worker,
                               args=(ejector1,self.servoStart.value(), self.servoStop.value()))
        st1.start()

    #manual dispenser controls

    def cb_dispense(self):
        dispenserUSB0.dispense(dispenser.connect_to_serial_port(dispenser.list_of_serial_ports()))

    def cb_reset_card_dispenser(self):
        dispenserUSB0.reset_card_dispenser(dispenser.connect_to_serial_port(dispenser.list_of_serial_ports()))

    def cb_write_hold_card(self):
        dispenserUSB0.write_hold_card(dispenser.connect_to_serial_port(dispenser.list_of_serial_ports()))

    def cb_get_status(self):
        self.lblDispenserStatus.setText(
            dispenserUSB0.request_status(dispenser.connect_to_serial_port(dispenser.list_of_serial_ports())))

    #manual conveyor controls

    def cb_fwd(self):
        conveyor1.fwd()

    def cb_rev(self):
        conveyor1.rev()

    def cb_stop(self):
        conveyor1.stop()

    def cb_reset(self):
        conveyor1.reset()
        self.idxcount = 0
        self.lcd_idxcounter.display(self.idxcount)

    #manual stepper control via a dial
    #rewrite somehow into s FSM ???
    def stepper(self):

        self.cnt = 0
        txt = threading.currentThread().getName()
        self.Input_Status.addItem(txt)

        while True:
            if self.bin1Level_target.value()> self.bin1Level.value() and not self.bin1_high_limit :
                stepper1.up()
                self.cnt = self.cnt + 1
                self.CycleCountBin1.display(self.cnt)
                self.bin1Level.setValue(self.cnt)

            elif self.bin1Level_target.value()< self.bin1Level.value() and not self.bin1_low_limit :
                stepper1.down()
                self.cnt = self.cnt-1
                self.CycleCountBin1.display(self.cnt)
                self.bin1Level.setValue(self.cnt)

            else:
                stepper1.stop()
            #update progressbar
            self.progressBar.setValue(self.cnt)

    # edge detector callbacks functions for the sensors

    def cb_bin1_level_limit(self,oldVal, newVal):
        txt = "bin1 level reached"
        self.Input_Status.addItem(txt)

    def cb_conveyor_index(self, oldVal, newVal):
        self.idxcount = self.idxcount + 1
        self.lcd_idxcounter.display(self.idxcount)

    def cb_bin1_card_stuck(self,oldVal, newVal):
        txt = "bin1 card stuck"
        self.Input_Status.addItem(txt)

    def cb_bin1_high_limit(self,oldVal, newVal):
        txt = "bin1 high limit reached!"
        self.Input_Status.addItem(txt)
        txt = str(abs(self.cnt))
        self.Input_Status.addItem(txt)
        #reset counter
        self.cnt = 0

    def cb_bin1_low_limit(self, oldVal, newVal):
        txt = "bin1 low limit reached!"
        self.Input_Status.addItem(txt)
        txt = str(abs(self.cnt))
        self.Input_Status.addItem(txt)
        #reset counter
        self.cnt = 0

    #Qtimer based functions

    def io_polling(self):


    #sometimes missing the event in other loops that are faster
        # assign inputs to monitor with edge detector
        self.detector_bin1_stuck(wiringpi.digitalRead(81))
        self.detector_bin1_level_limit(not wiringpi.digitalRead(82))

        self.detector_bin1_high_limit(wiringpi.digitalRead(65))
        self.detector_bin1_low_limit(wiringpi.digitalRead(66))

        #raspberry PiFace I/O
        self.detector_conveyor_index(not wiringpi.digitalRead(212))  #break beam sesnor wiringpi.digitalRead(15))

        #create new signals for UI
        self.ok_to_run=not wiringpi.digitalRead(65) and not wiringpi.digitalRead(66)
        self.bin1_high_limit = wiringpi.digitalRead(65)
        self.bin1_low_limit = wiringpi.digitalRead(66)
        self.beam_broken=not wiringpi.digitalRead(212)  #break beam sesnor wiringpi.digitalRead(15)
        self.bin1_stuck = wiringpi.digitalRead(81)
        self.bin1_level_limit=not wiringpi.digitalRead(82)

        #create FSM updates on UI
        self.lblBin1_FSM.setText(self.bin1.state)
        self.lblConveyor_FSM.setText(self.belt.state)

        #create lcd displays
        #self.tofDistance.display(tof_sensor1.get_distance())
        #self.progressBar.setValue(tof_sensor1.get_distance())
        #self.bin1.set_distance(tof_sensor1.get_distance())
        #self.bin1.set_ready_limit(self.tofDistanceSP.intValue())

        if wiringpi.digitalRead(65):
            self.lcd_65.display(1)
        else:
            self.lcd_65.display(0)

        if wiringpi.digitalRead(66):
            self.lcd_66.display(1)
        else:
            self.lcd_66.display(0)

        if wiringpi.digitalRead(81):
            self.lcd_81.display(1)
        else:
            self.lcd_81.display(0)

        if wiringpi.digitalRead(82):
            self.lcd_82.display(1)
        else:
            self.lcd_82.display(0)

        if wiringpi.digitalRead(212):  #break beam sesnor wiringpi.digitalRead(15):
            self.lcd_15.display(1)
        else:
            self.lcd_15.display(0)

    def heartbeat(self):
        global watchdog
        watchdog^=True
        if watchdog:
            self.lcd_0.display(1)
            wiringpi.digitalWrite(PIFACE_LED7,ON)
        else:
            self.lcd_0.display(0)
            wiringpi.digitalWrite(PIFACE_LED7,OFF)

if __name__ == '__main__':

    #check what hardware is connected
    i2cutil.check_i2c_devices()

    #initalize the io hardware interfaces here so they can be used by the UI and the FSM !!!!
    expander.init()
    piface.init()

    #piFace SPI interface
    conveyor1 = conveyor.Conveyor()

    '''

    #Create instance objects from class definitions in hardware that exists
    if i2cutil.is_connected_to_device(0x29):
        tof_sensor1 = tof.VL6180X(address=0x29, debug=False)
        tof_sensor1.default_settings()

    if i2cutil.is_connected_to_device(0x41):
        ejector1 = ejector.Ejector("Bin-1", 0x41, 1)

    if i2cutil.is_connected_to_device(0x60):
        stepper1 = stepper.Stepper("Bin-1", 0x60, 1, 65, 66, 81)
'''
    #create and instance of the dispenser class
    dispenserUSB0 = dispenser.Dispenser(dispenser.connect_to_serial_port('/dev/ttyUSB0'))


    #create user interface150
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QTabWidget()
    prog = MyGuiProgram(dialog)

    dialog.show()

    #setup timers to run input updates
    timer=QtCore.QTimer()
    timer.timeout.connect(prog.heartbeat)
    timer.start(500)

    #interface updates
    iotimer = QtCore.QTimer()
    iotimer.timeout.connect(prog.io_polling)
    iotimer.start(50)

    #regsiter software e-stop
    atexit.register(swEmergencyStop)

    #start the whole thing
    sys.exit(app.exec_())