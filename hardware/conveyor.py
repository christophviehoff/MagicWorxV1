# -*- coding: utf-8 -*-

import wiringpi,piface,expander
import RPi.GPIO as GPIO
import threading
from time import sleep
from transitions import Machine
from ejector import Ejector
from dispenser import Dispenser,connect_to_serial_port,list_of_serial_ports

#Help functions
def swEmergencyStop():
    conveyor.reset()

class Mcard:
    def __init__(self, name):
        self.name=name

class Queue:
    def __init__(self,length):
        self.length=length
        #prepopulate the list with None
        self.items = [None] *self.length

    def show(self):
        #print "".join([str(x) for x in self.items])
        pass

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(4,item)

    def dequeue(self):
        return self.items.pop()

    def index(self,name):
        #dismiss last item
        self.enqueue(name)
        self.dequeue()

    def update(self,pos,item):
        self.items[pos]=item

    def get_name(self,pos):
        return self.items[pos]

    def size(self):
        return len(self.items)

class Conveyor():

    def __init__(self):
        wiringpi.digitalWrite(200,0)
        wiringpi.digitalWrite(201,0)

    def fwd(self):
        wiringpi.digitalWrite(200, 1)
        wiringpi.digitalWrite(201, 0)

    def rev(self):
        wiringpi.digitalWrite(200, 0)
        wiringpi.digitalWrite(201, 1)

    def stop(self):
        wiringpi.digitalWrite(200, 0)
        wiringpi.digitalWrite(201, 0)

    def reset(self):
        wiringpi.digitalWrite(200, 0)
        wiringpi.digitalWrite(201, 0)

class Conveyor_FSM(Machine):

    # states and transitions
    def __init__(self):
        self.running=True
        self.isEnabled = False
        self.isEjectEnabled = False
        self.isDispenseEnabled = False
        self.isOK = False

        # break beam sensor status
        self.break_beam_sensor=False
        # conveyor counter reset
        self.idxcount = 0

        #setup break beam sensor
        GPIO.setmode(GPIO.BCM)
        # GPIO 24 set up as input, pulled up to avoid false detection.
        GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        states = ['init','ready','start', 'stop', 'dispense', 'eject']
        Machine.__init__(self, states=states, initial='init')

        self.add_transition('trigger', 'init', 'ready', conditions='is_enabled')
        self.add_transition('trigger', 'ready', 'start', conditions='is_hw_ok')
        self.add_transition('trigger', 'start', 'stop', conditions='is_beam_broken')
        self.add_transition('trigger', 'stop', 'dispense', conditions='is_dispense_ready')
        self.add_transition('trigger', 'dispense', 'eject')
        self.add_transition('trigger', 'eject', 'ready')

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

    def get_dispenser_status(self):
        return self.dispenserUSB0.request_status(connect_to_serial_port(list_of_serial_ports()))

    def get_break_beam_sensor_status(self):
        return self.break_beam_sensor, self.idxcount

    #what to do when you enter a state


    # define hardware objects at start

    def on_enter_init(self):
        conveyor.stop()
        #TODO : better way to handle when hardware is not there or working
        if self.isDispenseEnabled:
            self.dispenserUSB0 = Dispenser(connect_to_serial_port('/dev/ttyUSB0'))

        if self.isEjectEnabled:
            # create an instance of the ejector class
            try:
                self.ejector1 = Ejector("Bin-1", 0x40, 1)
            except IOError:
                print "no Ejector found"

    def on_enter_ready(self):
        self.isOK = True

    def on_enter_start(self):
        conveyor.fwd()
        #sleep(.2)

    def on_enter_stop(self):
        conveyor.stop()

    def on_enter_dispense(self):
        # conveyor tracking- indexing with a dummy card

        if self.isDispenseEnabled:
            self.dispenserUSB0.dispense(connect_to_serial_port(list_of_serial_ports()))
            q.index(Mcard('Dummy'))
            sleep(1)  #min time
        else: # no card
            q.index(None)
            sleep(1) #slow down to not index too many times, wont work without it

    def on_enter_eject(self):
        if self.isEjectEnabled:
            #first bin!!!
            if q.get_name(13) is None:
                pass
            else:
                self.ejector1.eject(150,400)
                q.update(13,None)
        else:
            sleep(1) #slow down for testing

    #transition conditions

    def is_enabled(self):
        return self.isEnabled

    def is_beam_broken(self):
        self.break_beam_sensor = False
        #print "Waiting for falling edge on port 24"
        GPIO.wait_for_edge(24, GPIO.FALLING)
        self.idxcount +=1
        conveyor.stop() #TODO maybe faster when stpped right here ?
        self.break_beam_sensor = True
        return True
        #return not wiringpi.digitalRead(24)  #212break beam sensor

    def is_hw_ok(self):
        #TODO use for something, check HW status ?
        return self.isOK

    def is_dispense_ready(self):
        if self.isDispenseEnabled:
            try:
                status= self.dispenserUSB0.is_ready(connect_to_serial_port(list_of_serial_ports()))
            except AttributeError:
                status= False  # remains in STOP state until dispenser disabled
            else:
                return status
        else:
            return True  # bypass


if __name__ == "__main__":
    import sys, atexit

    # Help functions
    def terminate():
        print 'Program terminated by user via emergency stop'

    # GUI stuff
    from PyQt5 import QtCore, QtWidgets
    from conveyor_control import Ui_Controller
    from cfgreader import read_bin_config

    toggle = False

    # main bin test GUI program class
    class MyConveyor(Ui_Controller):

        def __init__(self, dialog):
            Ui_Controller.__init__(self)
            self.setupUi(dialog)
            # Step 1a :  register callbacks for user interface events and sensors
            self.pb_clear.clicked.connect(self.cb_clear)
            self.pb_fwd.clicked.connect(self.cb_fwd)
            self.pb_rev.clicked.connect(self.cb_rev)
            self.pb_stop.clicked.connect(self.cb_stop)
            self.pb_reset.clicked.connect(self.cb_reset)
            self.pb_estop.clicked.connect(self.cb_estop)
            self.pb_get_dispensor_status.clicked.connect(self.cb_get_dispensor_status)
            # create state machine
            self.belt = Conveyor_FSM()
            self.running = True  #enable state machine

            #threads
            self.pb_conveyor_thread.clicked.connect(self.cb_conveyor_thread)


            # read configuration of default target, default is Bin-1

            # probably use this for  sorting recipes
            self.config = read_bin_config('Bin1')


            # create status update
            self.conveyor_status.addItem('[info] {}'.format("piface ready"))

            # conveyor counter
            self.idxcount = 0

        # Step 2a :  write callback function for button events

        def cb_clear(self):
            self.conveyor_status.clear()

        def cb_fwd(self):
            conveyor.fwd()

        def cb_rev(self):
            conveyor.rev()

        def cb_stop(self):
            conveyor.stop()

        def cb_reset(self):
            conveyor.reset()
            self.idxcount = 0
            self.lcd_idxcounter.display(self.idxcount)

        def cb_estop(self):
            conveyor.reset()

        def cb_get_dispensor_status(self):
            self.lbl_dispense_status.setText(self.belt.get_dispenser_status())


        # Step 2b :  write to gui about the status
        # Sorting recipe loaded or something like that




        #treads:
        def cb_conveyor_thread(self):
            # tConveyor = threading.Thread()
            tConveyor = threading.Thread(name="Conveyor started", target=self.run_conveyor_FSM)
            tConveyor.daemon = True
            tConveyor.start()

        # run Finite State maxchines

        def shutdown(self):
            self.running = False

        def run_conveyor_FSM(self):
            txt = threading.currentThread().getName()
            self.conveyor_status.addItem('[info] {} , thread running'.format(txt))

            while self.running:

                if self.chk_enable.isChecked():
                    self.belt.enable()
                    self.belt.trigger()
                else:
                    self.belt.disable()
                    self.belt.to_init()
                    sleep(.5)

                if self.chk_dispense.isChecked():
                    self.belt.enable_dispense()
                else:
                    self.belt.disable_dispense()

                if self.chk_eject.isChecked():
                    self.belt.enable_eject()
                else:
                    self.belt.disable_eject()



        # Step 3a : Qtimer polling for inputs

        #500ms
        def watchdog(self):
            global toggle
            toggle ^= True
            if toggle:
                self.heartbeat.setEnabled(1)
                wiringpi.digitalWrite(207, 1)  #piFace LED7
            else:
                self.heartbeat.setEnabled(0)
                wiringpi.digitalWrite(207, 0)

        #10ms
        def io_polling(self):

            # create FSM updates on UI

            self.lbl_conveyor_FSM.setText(self.belt.state)

            # Step 3b : update lcd/led displays for all sensors

            # fet sensor status information from conveyor obj
            sensor,idxcount =  self.belt.get_break_beam_sensor_status()

            self.lcd_idxcounter.display(idxcount)

            if sensor:  # 212 break beam sensor wiringpi.digitalRead(212):
                self.lcd_breakbeam.display(1)
                wiringpi.digitalWrite(202,1)  # display on piface LED 3 as weell right next to relay LEDS's
            else:
                self.lcd_breakbeam.display(0)
                wiringpi.digitalWrite(202, 0)

            #update tracking positions
            if q.get_name(0) is None:
                self.pos_0.setEnabled(0)
            else:
                self.pos_0.setEnabled(1)

            if q.get_name(1) is None:
                self.pos_1.setEnabled(0)
            else:
                self.pos_1.setEnabled(1)

            if q.get_name(2) is None:
                self.pos_2.setEnabled(0)
            else:
                self.pos_2.setEnabled(1)

            if q.get_name(3) is None:
                self.pos_3.setEnabled(0)
            else:
                self.pos_3.setEnabled(1)

            if q.get_name(4) is None:
                self.pos_4.setEnabled(0)
            else:
                self.pos_4.setEnabled(1)

            if q.get_name(5) is None:
                self.pos_5.setEnabled(0)
            else:
                self.pos_5.setEnabled(1)

            if q.get_name(6) is None:
                self.pos_6.setEnabled(0)
            else:
                self.pos_6.setEnabled(1)

            if q.get_name(7) is None:
                self.pos_7.setEnabled(0)
            else:
                self.pos_7.setEnabled(1)

            if q.get_name(8) is None:
                self.pos_8.setEnabled(0)
            else:
                self.pos_8.setEnabled(1)

            if q.get_name(9) is None:
                self.pos_9.setEnabled(0)
            else:
                self.pos_9.setEnabled(1)

            if q.get_name(10) is None:
                self.pos_10.setEnabled(0)
            else:
                self.pos_10.setEnabled(1)

            if q.get_name(11) is None:
                self.pos_11.setEnabled(0)
            else:
                self.pos_11.setEnabled(1)

            if q.get_name(12) is None:
                self.pos_12.setEnabled(0)
            else:
                self.pos_12.setEnabled(1)

            if q.get_name(13) is None:
                self.pos_13.setEnabled(0)
            else:
                self.pos_13.setEnabled(1)

            if q.get_name(14) is None:
                self.pos_14.setEnabled(0)
            else:
                self.pos_14.setEnabled(1)

            if q.get_name(15) is None:
                self.pos_15.setEnabled(0)
            else:
                self.pos_15.setEnabled(1)

            if q.get_name(16) is None:
                self.pos_16.setEnabled(0)
            else:
                self.pos_16.setEnabled(1)

            if q.get_name(17) is None:
                self.pos_17.setEnabled(0)
            else:
                self.pos_17.setEnabled(1)

            if q.get_name(18) is None:
                self.pos_18.setEnabled(0)
            else:
                self.pos_18.setEnabled(1)

            if q.get_name(19) is None:
                self.pos_19.setEnabled(0)
            else:
                self.pos_19.setEnabled(1)

            if q.get_name(20) is None:
                self.pos_20.setEnabled(0)
            else:
                self.pos_20.setEnabled(1)

            if q.get_name(21) is None:
                self.pos_21.setEnabled(0)
            else:
                self.pos_21.setEnabled(1)

            if q.get_name(22) is None:
                self.pos_22.setEnabled(0)
            else:
                self.pos_22.setEnabled(1)

            if q.get_name(23) is None:
                self.pos_23.setEnabled(0)
            else:
                self.pos_23.setEnabled(1)

            if q.get_name(24) is None:
                self.pos_24.setEnabled(0)
            else:
                self.pos_24.setEnabled(1)

            if q.get_name(25) is None:
                self.pos_25.setEnabled(0)
            else:
                self.pos_25.setEnabled(1)

            if q.get_name(26) is None:
                self.pos_26.setEnabled(0)
            else:
                self.pos_26.setEnabled(1)

    # main program start

    # IO expander setup SPI piFace2 (for conveyor relay control)
    piface.init()
    #expander.init()
    # Create conveyor object
    conveyor = Conveyor()
    q=Queue(27)  # 26 position


    # create user interface MyBinControl
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QTabWidget()
    prog = MyConveyor(dialog)

    dialog.show()

    # setup timers to run heartbeat every 1/2 sec
    timer = QtCore.QTimer()
    timer.timeout.connect(prog.watchdog)
    timer.start(500)

    # interface input/output updates every 50 ms
    iotimer = QtCore.QTimer()
    iotimer.timeout.connect(prog.io_polling)
    iotimer.start(10)


    # regsiter software e-stop

    atexit.register(swEmergencyStop)

    # start the whole thing
    sys.exit(app.exec_())