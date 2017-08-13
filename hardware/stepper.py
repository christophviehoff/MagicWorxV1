# -*- coding: utf-8 -*-

import threading
import wiringpi
from Adafruit_MotorHAT import Adafruit_MotorHAT
from time import sleep
from i2cPCA9555 import PCA9555





class Stepper(threading.Thread):

    def __init__(self,name,stepper_address ,port,io_address,pin_low_limit_sns,pin_high_limit_sns):
        super(Stepper, self).__init__()
        self.setDaemon(True)
        self.running = False
         # Create stepper objects
        self.name = name
        self.stepper_address= stepper_address
        self.port= port # motorhat uses port 1 and 2
        self.io_address=io_address

        self.pin_high_limit_sns = pin_high_limit_sns
        self.pin_low_limit_sns = pin_low_limit_sns

        #defaults
        self.isEnabled = True
        self.number_of_steps = 0
        self.direction = Adafruit_MotorHAT.BRAKE
        self.style = Adafruit_MotorHAT.INTERLEAVE
        #create MotorHat object
        self.motor_hat = Adafruit_MotorHAT(self.stepper_address)
        #create stepper object
        self.stepper = self.motor_hat.getStepper(200,self.port)
        self.stepper.setSpeed(60)
        #create IO object
        self.expander=PCA9555(self.io_address)


    # flow control

    def shutdown(self):
        self.running=False

    def enable(self):
        self.isEnabled=True

    def disable(self):
        self.isEnabled=False

    def run(self):

        #started by thread.start() method initial position

        # print("{} started!".format(self.getName()))              # "Thread-x started!"
        self.running=True

        while self.running:

            if self.isEnabled:
                if not self.expander.digitalRead(self.pin_high_limit_sns):
                    self.oneStep_up()
                else:
                    sleep(.05) #make sure it hits the switch and doesn't bounce
                    self.stop()
                    self.running=False   #self.running-False exits thread

        # Pretend to work for a second
        # print("{} finished!".format(self.getName()))             # "Thread-x finished!"

    #stepper commands

    def up(self):
        self.stepper.step(4,Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)

    def down(self):
        self.stepper.step(4,Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

    def stop(self):
        self.stepper.step(0,Adafruit_MotorHAT.BRAKE,Adafruit_MotorHAT.INTERLEAVE)

    def release(self):
        self.stepper.step(0,Adafruit_MotorHAT.RELEASE,Adafruit_MotorHAT.INTERLEAVE)

    def oneStep_up(self):
        self.stepper.oneStep(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)

    def oneStep_down(self):
        self.stepper.oneStep(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

    #generic API

    def step(self,number_of_steps, direction, style):
        self.number_of_steps = number_of_steps
        self.direction = direction
        self.style = style
        self.stepper.step(self.number_of_steps, self.direction,self.style)

    def oneStep(self,direction, style):
        self.direction = direction
        self.style = style
        self.stepper.oneStep(self.direction, self.style)

    def e_stop(self):
        #coil 1 and 2, 3 and 4
        #TODO: rewrite use 1=true,etc
        if self.port == 1:
            self.motor_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
            self.motor_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        elif self.port == 2:
            self.motor_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
            self.motor_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
        else:
            self.motor_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
            self.motor_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
            self.motor_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
            self.motor_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


if __name__ == "__main__":

    # Help functions
    def terminate():
       print 'Program terminated by user via emergency stop'

    # STEPPER BIN CONTROLLER  GUI SETUP

    import sys
    from i2cutil import is_connected_to_device,list_of_i2c_steppers
    from cfgreader import read_bin_config

    # GUI stuff
    from PyQt5 import QtCore, QtWidgets
    from bincontrol import Ui_Controller
    import expander,piface
    import sys,atexit

    toggle = False
    PIFACE=200

    class EdgeTrigger(object):
        def __init__(self, callback):
            self.value = None
            self.callback = callback

        def __call__(self, value):
            # if value != self.value:
            # this one will trigger a 0 to 1 transition only
            if value < self.value:
                self.callback(self.value, value)
            self.value = value

    # main bin test GUI program class
    class MyBinControl(Ui_Controller):

        def __init__(self, dialog):
            Ui_Controller.__init__(self)
            self.setupUi(dialog)
            self.running=False
        # Step 1a :  register callbacks for user interface events and sensors

            self.pb_to_top.clicked.connect(self.thread_to_top)
            self.pb_up.clicked.connect(self.cb_up)
            self.pb_cycle.clicked.connect(self.thread_cycle)
            self.pb_stop.clicked.connect(self.cb_stop)
            self.pb_down.clicked.connect(self.cb_down)
            self.pb_to_bottom.clicked.connect(self.thread_to_bottom)
            self.pb_clear.clicked.connect(self.cb_clear)
            self.pb_e_stop.clicked.connect(self.cb_e_stop)

            self.bin_selector.currentIndexChanged.connect(self.cb_bin_selector)

        # register 0 to 1 'rising edge'  edge detector callback
            self.detector_high_limit_sns = EdgeTrigger(self.cb_high_limit_sns)
            self.detector_low_limit_sns = EdgeTrigger(self.cb_low_limit_sns)

        # create main hardware object
        # name, stepper_address, stepper_port,servo_address,servo_port,io_address pin_low_level_sns, pin_high_level_sns, pin_top_level_sns,enabled

            #read bin configuration of default target, default is Bin-1
            self.bin=read_bin_config('Bin0')

            # check and create a list of dices
            self.i2c_list = list_of_i2c_steppers()
            self.bin_status.addItem('[info] {}'.format(self.i2c_list))
            self.bin_status.addItem('[info] {} devices detected.'.format(len(self.i2c_list)))
            #check and create default setup
            if self.bin['enabled']:   # from configuration
                self.controls_group.setEnabled(True)
                self.bin_status.addItem('[info] {} enabled'.format(self.bin['name']))
            else:
                self.controls_group.setEnabled(False)
                self.bin_status.addItem('[info] {} disabled'.format(self.bin['name']))

            if is_connected_to_device(int(self.bin['stepper_address'],16)):
                self.controls_group.setEnabled(True)
                self.bin_status.addItem('[info] {} ready.'.format(self.bin['name']))
                self.stepper = Stepper(self.bin['name'],int(self.bin['stepper_address'],16),self.bin['stepper_port'],int(self.bin['io_address'],16)
                                       ,self.bin['pin_low_limit_sns'],self.bin['pin_high_limit_sns'])
                self.stepper.start()
            else:
                self.controls_group.setEnabled(False)
                self.bin_status.addItem('[ERR ] {} not ready.'.format(self.bin['name']))

            # create IO object

            #TODO do as above
            self.expander = PCA9555(int(self.bin['io_address'],16))

            # max counts interleaved mode for progress bar display
            self.cnt_max = 5650 # initil calibration value
            self.cnt = 0

        # Step 2a :  write callback function for button events
        # Step 2b :  write to gui about the status

        def cb_bin_selector(self):

            #stop all motion before switching
            self.running=False
            self.cb_stop()

             # read configuration of target from qcombobox via header
            self.bin = read_bin_config(self.bin_selector.currentText())


            if is_connected_to_device(int(self.bin['stepper_address'],16)):
                self.controls_group.setEnabled(True)
                self.bin_status.addItem('[info] {} ready.'.format(self.bin['name']))
                self.stepper = Stepper(self.bin['name'], int(self.bin['stepper_address'], 16), self.bin['stepper_port'],int(self.bin['io_address'],16)
                                       ,self.bin['pin_low_limit_sns'], self.bin['pin_high_limit_sns'])
            else:
                self.controls_group.setEnabled(False)
                self.bin_status.addItem('[ERR ] {} not ready.'.format(self.bin['name']))

            if self.bin['enabled']:
                self.controls_group.setEnabled(True)
                self.bin_status.addItem('[info] {} enabled.'.format(self.bin['name']))
            else:
                self.controls_group.setEnabled(False)
                self.bin_status.addItem('[info] {} disabled'.format(self.bin['name']))



        # Threads
        # needs to be a thread !!!!!! otherwise ui freezes111

        def thread_to_top(self):
            tBinTop = threading.Thread(name="to_top", target=self.to_top)
            tBinTop.daemon = True
            tBinTop.start()

        def thread_to_bottom(self):
            tBinBot = threading.Thread(name="to_bottom", target=self.to_bottom)
            tBinBot.daemon = True
            tBinBot.start()

        def thread_cycle(self):
            tCycle = threading.Thread(name="cycle", target=self.cycle)
            tCycle.daemon = True
            tCycle.start()

        #thread target workers

        def to_top(self):
            self.pb_to_top.setDisabled(True)  # only run one tread, disable button to start another
            self.running = False
            self.cb_stop()
            self.bin_status.addItem('[cmd ] to top')
            self.running = True

            sleep(1)
            while not self.expander.digitalRead(self.bin['pin_high_limit_sns']) and self.running and self.power_on.isChecked():
                self.stepper.oneStep_up()
                self.cnt += 1
                self.bar_bin_level.setValue(self.cnt+self.cnt_max)
                self.lcd_bin_level_sns.display(self.cnt)

            self.bin_status.addItem('[info] {} counts'.format(self.cnt))

            if self.expander.digitalRead(self.bin['pin_high_limit_sns)']) :
                self.cnt=0
            self.pb_to_top.setDisabled(False)

        def to_bottom(self):
            self.pb_to_bottom.setDisabled(True)# only run one tread, disable button to start another
            self.running = False
            self.cb_stop()
            self.bin_status.addItem('[cmd ] to bottom')
            self.running = True

            sleep(1)
            while not self.expander.digitalRead(self.bin['pin_low_limit_sns']) and self.running and self.power_on.isChecked():
                self.stepper.oneStep_down()
                self.cnt -= 1
                self.bar_bin_level.setValue(self.cnt_max + self.cnt )
                self.lcd_bin_level_sns.display(self.cnt)

            #calibration of range when bin is empty
            self.bin_status.addItem('[info] {} counts'.format(self.cnt))
            self.pb_to_bottom.setDisabled(False)

        def cycle(self):

            self.pb_cycle.setDisabled(True)# only run one tread, disable button to start another
            self.cb_stop()
            self.bin_status.addItem('[cmd ] cycling')
            self.running = True

            while self.running and self.power_on.isChecked():
                self.to_bottom()
                self.to_top()

            self.pb_cycle.setDisabled(False)

        #no thread needed here, too short of a command tio casue a significat delay in the UI update

        def cb_up(self):
            self.bin_status.addItem('[cmd ] up')
            self.stepper.up()
            self.cnt += 1
            self.bar_bin_level.setValue(self.cnt + self.cnt_max)
            self.lcd_bin_level_sns.display(self.cnt)

        def cb_stop(self):
            self.bin_status.addItem('[cmd ] stop')
            self.stepper.stop()
            self.running=False  #end run thread.


        def cb_e_stop(self):
            self.stepper.stop()
            self.running = False  # end run thread.
            self.bin_status.addItem('[cmd ] emergency-stop')
            self.bin_status.addItem('[cmd ] exiting program')
            sys.exit(1) #terminate program

        def cb_down(self):
            self.bin_status.addItem('[cmd ] down')
            self.stepper.down()
            self.cnt -= 1
            self.bar_bin_level.setValue(self.cnt + self.cnt_max)
            self.lcd_bin_level_sns.display(self.cnt)

        def cb_clear(self):
            self.bin_status.clear()

        # Step 2c :  rising edghe detector callbacks

        def cb_top_limit_sns(self,oldVal, newVal):
            #self.bin_status.addItem('[info] at top limit')
            pass

        def cb_high_limit_sns(self,oldVal, newVal):
            self.bin_status.addItem('[info] at high limit')

        def cb_low_limit_sns(self,oldVal, newVal):
            self.bin_status.addItem('[info] at low limit')

        # Step 3a : Qtimer polling for inputs

        def watchdog(self):
            global toggle
            toggle ^= True
            if toggle:
                self.heartbeat.setEnabled(1)
            else:
                self.heartbeat.setEnabled(0)

        def io_polling(self):

        # Step 3b : update lcd/led displays for all 3 sensors

            if self.expander.digitalRead(self.bin['pin_high_limit_sns']):
                self.lcd_high_limit_sns.display(1)
                self.led_high_limit_sns.setEnabled(1)
            else:
                self.lcd_high_limit_sns.display(0)
                self.led_high_limit_sns.setEnabled(0)

            if self.expander.digitalRead(self.bin['pin_low_limit_sns']):
                self.lcd_low_limit_sns.display(1)
                self.led_low_limit_sns.setEnabled(1)
            else:
                self.lcd_low_limit_sns.display(0)
                self.led_low_limit_sns.setEnabled(0)

            if self.power_on.isChecked():
                wiringpi.digitalWrite(PIFACE + 2,1)
            else:
                wiringpi.digitalWrite(PIFACE + 2,0)

        # Step 3c : register edge detection status changes for all  3 sensors

            self.detector_high_limit_sns(self.expander.digitalRead(self.bin['pin_high_limit_sns']))
            self.detector_low_limit_sns(self.expander.digitalRead(self.bin['pin_low_limit_sns']))

    # main program start

    #  initalize the io hardware interfaces
    # expander.init()
    piface.init()

    #check if i2c bus devices are present
    if not is_connected_to_device(0x70):
        print "no stepper i2c device found!"
        #sys.exit(1)

    # create user interface MyBinControl
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QTabWidget()
    prog = MyBinControl(dialog)

    dialog.show()

    # setup timers to run heartbeat every 1/2 sec
    timer = QtCore.QTimer()
    timer.timeout.connect(prog.watchdog)
    timer.start(500)

    # interface input/output updates every 50 ms
    iotimer = QtCore.QTimer()
    iotimer.timeout.connect(prog.io_polling)
    iotimer.start(50)

    # regsiter software e-stop
    atexit.register(terminate)

    # start the whole thing
    sys.exit(app.exec_())