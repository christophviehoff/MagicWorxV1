#!/usr/bin/python

# I2C test program for a PCA9555

import smbus

pins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# class for easier using PCA9555 chips on an I2C bus
class PCA9555():
    # open Linux device /dev/ic2-1
    i2c = smbus.SMBus(1)

    # construct a new object with the I2C address of the PCA9555
    def __init__(self, address):
        self.address = address
        self.setInputDirection(0xFFFF)  # all pins are inputs by default now


    # write a 16 bit value to a register pair
    # write low byte of value to register reg,
    # and high byte of value to register reg+1
    def writeRegisterPair(self, reg, value):
        low = value & 0xff
        high = (value >> 8) & 0xff
        self.i2c.write_byte_data(self.address, reg, low)
        self.i2c.write_byte_data(self.address, reg + 1, high)

    # read a 16 bit value from a register pair
    def readRegisterPair(self, reg):
        low = self.i2c.read_byte_data(self.address, reg)
        high = self.i2c.read_byte_data(self.address, reg + 1)
        return low | (high << 8)

    # set IO ports to input, if the corresponding direction bit is 1,
    # otherwise set it to output
    def setInputDirection(self, direction):
        self.writeRegisterPair(6, direction)

    # set the IO port outputs
    def setOutput(self, value):
        self.writeRegisterPair(2, value)

    # read the IO port inputs
    def getInput(self):
        return self.readRegisterPair(0)

    def digitalRead(self,pin):
        if self.getInput() & (0x0001<< pin):  # MASK PIN 0 of a 16 bit word
            return 1
        else:
            return 0
if __name__ == "__main__":

    import sys, atexit
    from i2cutil import is_connected_to_device,list_of_i2c_io

    # Help functions
    def terminate():
       print 'Program terminated by user via emergency stop'

    # GUI stuff
    from PyQt5 import QtCore, QtWidgets
    from leds import Ui_Controller

    toggle = False

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
    class MyLeds(Ui_Controller):

        def __init__(self, dialog):
            Ui_Controller.__init__(self)
            self.setupUi(dialog)
            self.running=False
        # Step 1a :  register callbacks for user interface events and sensors
            self.pb_clear.clicked.connect(self.cb_clear)

            self.input_selector.currentIndexChanged.connect(self.cb_input_selector)

        # register 0 to 1 'rising edge'  edge detector callback
            self.detector_pin_0 = EdgeTrigger(self.cb_pin_0)
            self.detector_pin_1 = EdgeTrigger(self.cb_pin_1)

        # create main hardware object
            # check and create a list of devices
            self.i2c_list = list_of_i2c_io()
            self.led_status.addItem('[info] {}'.format(self.i2c_list))
            self.led_status.addItem('[info] {} device(s) detected.'.format(len(self.i2c_list)))


            # create a new PCA9555 object at first address found
            self.ioExpander = PCA9555(int(self.i2c_list[0], 16))


            #set qcombo box to first address
            self.input_selector.setCurrentText(self.i2c_list[0])

            #set all pins to input
            #sudo i2cdump - y 1 0x20 register 6 &7 for configuration of port 0 and port 11
            #self.ioExpander.setInputDirection(1 << 0)  # pin 0 input only
            #self.ioExpander.setInputDirection(0xFFFF)  # all pins

        # Step 2a :  write callback function for button events
        # Step 2b :  write to gui about the status


        def cb_input_selector(self):
            # read configuration of target from qcombobox via header
            # and convert to hex address
            self.address = int(self.input_selector.currentText(),16)
            if is_connected_to_device(self.address):
                self.led_status.addItem('[info] {} ready.'.format(hex(self.address)))
                self.ioExpander = PCA9555(self.address)
                #self.ioExpander.setInputDirection(0xFFFF)  # all pins
            else:
                self.led_status.addItem('[ERR ] {} not ready.'.format(hex(self.address)))

        def cb_clear(self):
            self.led_status.clear()


        # Step 2c :  FALLING edge detector callbacks
        def cb_pin_0(self, oldVal, newVal):
            self.led_status.addItem('[info] pin0 detected')

        def cb_pin_1(self, oldVal, newVal):
            self.led_status.addItem('[info] pin1 detected')


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

            if  self.ioExpander.digitalRead(0):
                self.led_0.setEnabled(1)
            else:
                self.led_0.setEnabled(0)

            if  self.ioExpander.digitalRead(1):
                self.led_1.setEnabled(1)
            else:
                self.led_1.setEnabled(0)

            if  self.ioExpander.digitalRead(2):
                self.led_2.setEnabled(1)
            else:
                self.led_2.setEnabled(0)

            if  self.ioExpander.digitalRead(3):
                self.led_3.setEnabled(1)
            else:
                self.led_3.setEnabled(0)

            if  self.ioExpander.digitalRead(4):
                self.led_4.setEnabled(1)
            else:
                self.led_4.setEnabled(0)

            if  self.ioExpander.digitalRead(5):
                self.led_5.setEnabled(1)
            else:
                self.led_5.setEnabled(0)

            if  self.ioExpander.digitalRead(6):
                self.led_6.setEnabled(1)
            else:
                self.led_6.setEnabled(0)

            if  self.ioExpander.digitalRead(7):
                self.led_7.setEnabled(1)
            else:
                self.led_7.setEnabled(0)

            if  self.ioExpander.digitalRead(8):
                self.led_8.setEnabled(1)
            else:
                self.led_8.setEnabled(0)

            if  self.ioExpander.digitalRead(9):
                self.led_9.setEnabled(1)
            else:
                self.led_9.setEnabled(0)

            if  self.ioExpander.digitalRead(10):
                self.led_10.setEnabled(1)
            else:
                self.led_10.setEnabled(0)

            if  self.ioExpander.digitalRead(11):
                self.led_11.setEnabled(1)
            else:
                self.led_11.setEnabled(0)

            if  self.ioExpander.digitalRead(12):
                self.led_12.setEnabled(1)
            else:
                self.led_12.setEnabled(0)

            if  self.ioExpander.digitalRead(13):
                self.led_13.setEnabled(1)
            else:
                self.led_13.setEnabled(0)

            if  self.ioExpander.digitalRead(14):
                self.led_14.setEnabled(1)
            else:
                self.led_14.setEnabled(0)

            if self.ioExpander.digitalRead(15):  #MASK PIN 15
                self.led_15.setEnabled(1)
            else:
                self.led_15.setEnabled(0)


        # Step 3c : register edge detection status changes for all sensors

            self.detector_pin_0(self.ioExpander.digitalRead(0))
            self.detector_pin_1(self.ioExpander.digitalRead(1))

    # main program start

    #  initalize the io hardware interfaces

    #check if i2c bus devices are present
    if not is_connected_to_device(0x20):
        print "no i2c device found at address 0x20!"
        #sys.exit(1)

    # create user interface MyBinControl
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QTabWidget()
    prog = MyLeds(dialog)

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