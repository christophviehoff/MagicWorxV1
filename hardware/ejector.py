import Adafruit_PCA9685
from time import sleep
import threading


class Ejector(threading.Thread):

    def __init__(self,name,address,port_number):
        super(Ejector, self).__init__()
        self.setDaemon(True)
        self.running = False
        #object attributes
        self.name = name
        self.address = address
        self.port_number=port_number
        #setup pulses
        self.pwm = Adafruit_PCA9685.PCA9685(self.address)
        self.pwm.set_pwm_freq(60)
        #  Configure min and max servo pulse lengths
        #self.servo_min = servo_min # 150 self.servoStart.value()  # Min pulse length out of 4096
        #self.servo_max = servo_max # 600 self.servoStop.value()  # Max pulse length out of 4096

    # flow control

    def shutdown(self):
        self.running = False

    def run(self):
        # started by thread.start() method initial position
        self.running = True

        #while self.running:
        #    pass

    def eject_test(self,servo_min,servo_max):

        self.servo_min=servo_min
        self.servo_max=servo_max

        #16 max per object

    #sequence
        for port in range (0, 16):
            self.pwm.set_pwm(self.port_number + port, 0, self.servo_max)
            sleep(1)
            self.pwm.set_pwm(self.port_number + port, 0, self.servo_min)
            sleep(1)

    #same time
        for port in range(0, 16):
            self.pwm.set_pwm(self.port_number + port, 0, self.servo_max)
        sleep(1)
        for port in range(0, 16):
            self.pwm.set_pwm(self.port_number + port, 0, self.servo_min)
        sleep(1)


    def eject(self,servo_min,servo_max):

        self.servo_min=servo_min
        self.servo_max=servo_max

        self.pwm.set_pwm(self.port_number, 0, self.servo_max)
        sleep(1)
        self.pwm.set_pwm(self.port_number, 0, self.servo_min)
        sleep(1)


if __name__ == "__main__":

    import sys, atexit
    from gpiozero import Button
    from i2cutil import is_connected_to_device, list_of_i2c_servos

    # Help functions
    def terminate():
        print 'Program terminated by user via emergency stop'

    # GUI stuff
    from PyQt5 import QtCore, QtWidgets
    from ejector_control import Ui_Controller
    from cfgreader import read_bin_config

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
    class MyEjectors(Ui_Controller):

        def __init__(self, dialog):
            Ui_Controller.__init__(self)
            self.setupUi(dialog)
            self.running = False
            # Step 1a :  register callbacks for user interface events and sensors
            self.pb_clear.clicked.connect(self.cb_clear)
            self.bin_selector.currentIndexChanged.connect(self.cb_bin_selector)

            #threads
            self.pb_eject.clicked.connect(self.thread_eject)
            self.pb_eject_test.clicked.connect(self.thread_eject_test)

            # register 0 to 1 'rising edge'  edge detector callback

            # read configuration of default target, default is Bin-1
            self.servo = read_bin_config('Bin0')

            # create main hardware object
            # check and create a list of dices
            self.i2c_list = list_of_i2c_servos()

            if self.i2c_list:
                self.led_ready.setEnabled(1)
                self.ejector_status.addItem('[info] {}'.format(self.i2c_list))
                self.ejector_status.addItem('[info] {} device(s) detected.'.format(len(self.i2c_list)))
                # create a daefault ejector object at first address found
                self.ejector = Ejector("Bin-0", int(self.i2c_list[0], 16), 0)
            else:
                self.led_ready.setEnabled(0)
                self.ejector_status.addItem('[info] no device(s) detected.')

            #quick test eject
            #self.ejector.eject(150,600)
            #print "ejectors initialized and test complete !"

            # set qcombo box to first address
            self.bin_selector.setCurrentText(self.servo['name'])


        # Step 2a :  write callback function for button events



        # Step 2b :  write to gui about the status

        def cb_bin_selector(self):
            # read configuration of target from qcombobox via header
            # and convert to hex address
            # add how to get from bin1 to object creation
            self.servo = read_bin_config(self.bin_selector.currentText())

            if is_connected_to_device(int(self.servo['servo_address'],16)):
                self.ejector_status.addItem('[info] {} ready.'.format(self.servo['name']))
                self.ejector = Ejector(self.servo['name'], int(self.servo['servo_address'],16), self.servo['servo_port'])
                self.led_ready.setEnabled(1)
                self.ejector.start()
            else:
                self.led_ready.setEnabled(0)
                self.ejector_status.addItem('[ERR ] {} not ready.'.format(self.servo['name']))

        def cb_clear(self):
            self.ejector_status.clear()

        # Step 2c :  FALLING edge detector callbacks

        #treads:
        def thread_eject(self):
            tEject = threading.Thread(name='eject', target=self.eject)
            tEject.daemon = True
            tEject.start()

        def thread_eject_test(self):
            tEject_test = threading.Thread(name='eject', target=self.eject_test)
            tEject_test.daemon = True
            tEject_test.start()

        #thread worker :
        def eject(self):
            self.ejector_status.addItem('[cmd ] {} ejecting.'.format(self.servo['name']))
            self.ejector.eject(self.sliderA.value(), self.sliderB.value())
            self.ejector_status.addItem('[cmd ] {} done.'.format(self.servo['name']))

        # thread worker :
        def eject_test(self):
            self.ejector_status.addItem('[cmd ] all bins sequencing.')
            self.ejector.eject_test(self.sliderA.value(), self.sliderB.value())
            self.ejector_status.addItem('[cmd ] all bins done.')

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

            pass

            # Step 3c : register edge detection status changes for all sensors

            # main program start

    #  initalize the io hardware interfaces

    # check if i2c bus devices are present
    if not is_connected_to_device(0x70):
        print "no i2c device found at address 0x70!"
        # sys.exit(1)

    # create user interface MyBinControl
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QTabWidget()
    prog = MyEjectors(dialog)

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