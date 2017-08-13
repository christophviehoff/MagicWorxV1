"""
    def up(self):
        txt = "stepper up event triggered!"
        self.Input_Status.addItem(txt)
        st1 = threading.Thread(name="my up thread",target=stepper_worker,
                               args=(stepper1, 4, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE,))
        st1.start()

    def dn(self):
        txt = "stepper dn event triggered!"
        self.Input_Status.addItem(txt)
        st1 = threading.Thread(name="my dn thread",target=stepper_worker,
                               args=(stepper1, 4, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE,))
        st1.start()

    def stop(self):
        txt = "stepper stop event triggered!"
        self.Input_Status.addItem(txt)
"""

# Subclassing QThread
# http://qt-project.org/doc/latest/qthread.html
class AThread(QThread):

    def run(self):
        count = 0
        while count < 10:
            time.sleep(1)
            print("A Increasing")
            count += 1

thread = AThread()
thread.finished.connect(app.exit)
thread.start()

import wiringpi


def io_setup():
    wiringpi.wiringPiSetup()  # initialise wiringpi in native pin mode

    # bteak beam sensor
    wiringpi.pinMode(15, 0)  # sets GPIO14 to input
    wiringpi.pullUpDnControl(15, 2)  # set internal pull-up

    # Relay boards
    wiringpi.pinMode(0, 1)  # sets GPIO0 to output
    wiringpi.pinMode(2, 1)  # sets GPIO2 to output
    wiringpi.pinMode(3, 1)  # sets GPIO3 to ouput

    # expander IO
    pin_base = 65  # lowest available starting number is 65
    i2c_addr = 0x20  # A0, A1, A2 pins all wired to GND

    wiringpi.mcp23017Setup(pin_base, i2c_addr)  # set up the pins and i2c address

    # Note: MCP23017 has no internal pull-down, so we use pull-up instead and a NC contact to GND
    wiringpi.pinMode(65, 0)  # sets GPA0 to input
    wiringpi.pullUpDnControl(65, 2)  # set internal pull-up
    wiringpi.pinMode(66, 0)  # sets GPA1  to input
    wiringpi.pullUpDnControl(66, 2)  # set internal pull-up

    # Our second chip is now ready to use pins 81 (GPA0) – 96 (GPB7).
    wiringpi.mcp23017Setup(81, 0x21)


# bin cycling program for testing
def bin1_control(self):
    txt = threading.currentThread().getName()
    self.Input_Status.addItem(txt)
    going_dn = True
    going_up = False
    self.cnt = 0

    # using (not wiringpi.digitalRead(65) and not wiringpi.digitalRead(66)) might be faster
    # ok_to_run updated in polling every 250ms

    while True:

        if not self.bin1_low_limit and going_dn:
            stepper.rev(stepper1)
            self.cnt = self.cnt - 1
            self.CycleCountBin1.display(self.cnt)
            self.bin1Level.setValue(self.cnt + self.cnt_max)
            self.progressBar.setValue(self.cnt + self.cnt_max)
        else:
            going_dn = False
            going_up = True
            if not self.bin1_high_limit and going_up:
                stepper.fwd(stepper1)
                self.cnt = self.cnt + 1
                self.CycleCountBin1.display(self.cnt)
                self.bin1Level.setValue(self.cnt)
                self.progressBar.setValue(self.cnt)
            else:
                going_dn = True
                going_up = False

                # states and transitions


def __init__(self):
    states = ['init', 'start', 'up', 'down']
    Machine.__init__(self, states=states, queued=True, auto_transitions=False, initial='init')
    self.add_transition('trigger', 'init', 'start')
    self.add_transition('trigger', 'start', 'down')
    self.add_transition('trigger', 'down', 'up', conditions='is_low_limit')
    self.add_transition('trigger', 'up', 'down', conditions='is_high_level')
    self.add_transition('trigger', 'up', 'down', conditions='is_high_limit')


    # example on how to "enable" skip OVER a step


if not self.btnEnableDispense.isChecked():
    # skip dispense
    if self.belt.is_dispense():
        self.belt.to_eject()

if not self.btnEnableEject.isChecked():
    # skip over eject
    if self.belt.is_dispense() or self.belt.is_work():
        self.belt.to_start()




 #Create stepper objects
    #mh1 = Adafruit_MotorHAT(addr=0x60)

    #stepper 1
    #stepper1 = mh1.getStepper(200, 1)
    #stepper1.setSpeed(30)

    # stepper 2
    #stepper2 = mh1.getStepper(200, 2)
    #stepper2.setSpeed(30)

    #mh1.getMotor(1).run(Adafruit_MotorHAT.BRAKE)
    #mh1.getMotor(2).run(Adafruit_MotorHAT.BRAKE)


def fwd(stepper):
    stepper.step(4,Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)

def rev(stepper):
    stepper.step(4,Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

def stop(stepper):
    stepper.step(4,Adafruit_MotorHAT.BRAKE,Adafruit_MotorHAT.INTERLEAVE)

print "running"
            if self.isEnabled:
                if not wiringpi.digitalRead(self.low_level_pin) and going_dn:
                    self.oneStep()
                else:
                    going_dn = False
                    if not wiringpi.digitalRead(self.high_level_pin) and not going_dn:
                        self.oneStep_up()
                    else:
                        going_dn = True

if (not wiringpi.digitalRead(self.high_level_pin) and wiringpi.digitalRead(self.level_limit_pin)) and going_up:
    self.oneStep_up()
else:
    self.stop()

    if wiringpi.digitalRead(self.level_limit_pin):
        going_up = False

    if not going_up:
        self.step(600, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
        self.running = False
        going_up = True


        def load_camera_image(self):
            # Create the in-memory stream
            stream = io.BytesIO()
            with picamera.PiCamera() as camera:
                camera.start_preview()
                time.sleep(.1)
                camera.capture(stream, format='jpeg')
            # "Rewind" the stream to the beginning so we can read its content
            stream.seek(0)
            image = Image.open(stream)
            return np.asarray(image, dtype="int32")



# initialize the camera and grab a reference to the raw camera capture
            camera = PiCamera()
            camera.resolution = (640, 480)
            camera.framerate = 32
            rawCapture = PiRGBArray(camera, size=(640, 480))
            # allow the camera to warmup
            time.sleep(0.1)
            # capture frames from the camera
            for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                # grab the raw NumPy array representing the image - this array
                # will be 3D, representing the width, height, and # of channels
                image = frame.arra
                # show the frame
                cv2.imshow("Frame", image)
                key = cv2.waitKey(1) & 0xFF
                # clear the stream in preparation for the next frame
                rawCapture.truncate(0)
                #  if the `q` key was pressed, break from the loop
                if key == ord("q"):
                    break
import smbus,time

# For the PCA 953X and 955X series, the chips with 8 GPIO's have these port numbers
# The chips with 16 GPIO's have the first port for each type at double these numbers
# IE The first config port is 6


# register for chip PCA9555 16 bit

INPUT_PORT = 0
OUTPUT_PORT = 2
POLARITY_PORT = 4
CONFIG_PORT = 6


class PCA95XX(object):

    def __init__(self, busnum, address, num_gpios):

        assert num_gpios >= 0 and num_gpios <= 16, "Number of GPIOs must be between 0 and 16"
        self.bus = smbus.SMBus(busnum)
        self.address = address
        self.num_gpios = num_gpios

        if num_gpios <= 8:
            self.direction = self.bus.read_byte_date(address, CONFIG_PORT)
            self.outputvalue = self.bus.read_byte_data(address, OUTPUT_PORT)

        elif num_gpios > 8 and num_gpios <= 16:
            self.direction = self.bus.read_word_data(address, CONFIG_PORT << 1)
            self.outputvalue = self.bus.read_word_data(address, OUTPUT_PORT << 1)

    def _changebit(self, bitmap, bit, value):

        assert value == 1 or value == 0, "Value is %s must be 1 or 0" % value

        if value == 0:

            return bitmap & ~(1 << bit)

        elif value == 1:

            return bitmap | (1 << bit)


    # Change the value of bit PIN on port PORT to VALUE.  If the

    # current pin state for the port is passed in as PORTSTATE, we

    # will avoid doing a read to get it.  The port pin state must be

    # complete if passed in (IE it should not just be the value of the

    # single pin we are trying to change)

    def _readandchangepin(self, port, pin, value, portstate = None):

        assert pin >= 0 and pin < self.num_gpios, "Pin number %s is invalid, only 0-%s are valid" % \
        (pin, self.num_gpios)

        if not portstate:

            if self.num_gpios <= 8:

                portstate = self.bus.read_byte_data(self.address, port)

            elif self.num_gpios > 8 and self.num_gpios <= 16:

                portstate = self.bus.read_word_data(self.address, port << 1)

        newstate = self._changebit(portstate, pin, value)

        if self.num_gpios <= 8:

            self.bus.write_byte_data(self.address, port, newstate)

        else:

            self.bus.write_word_data(self.address, port << 1, newstate)

        return newstate

    # Polarity inversion

    def polarity(self, pin, value):

        return self._readandchangepin(POLARITY_PORT, pin, value)

    # Pin direction

    def config(self, pin, mode):

        self.direction = self._readandchangepin(CONFIG_PORT, pin, mode, self.direction)

        return self.direction

    def output(self, pin, value):

        assert self.direction & (1 << pin) == 0, "Pin %s not set to output" % pin

        self.outputvalue = self._readandchangepin(OUTPUT_PORT, pin, value, self.outputvalue)

        return self.outputvalue

    def input(self, pin):

        assert self.direction & (1 << pin) != 0, "Pin %s not set to input" % pin

        if self.num_gpios <= 8:

            value = self.bus.read_byte_data(self.address, INPUT_PORT)

        elif self.num_gpios > 8 and self.num_gpios <= 16:

            value = self.bus.read_word_data(self.address, INPUT_PORT << 1)

        return value & (1 << pin)

# RPi.GPIO compatible interface for PCA95XX You can pass this class
# along to anything that expects an RPi.GPIO module and it should work
# fine.

class PCA95XX_GPIO(object):
    OUT = 0

    IN = 1

    BCM = 0

    BOARD = 0

    def __init__(self, busnum, address, num_gpios):
        self.chip = PCA95XX(busnum, address, num_gpios)

    def setmode(self, mode):
        # do nothing

        pass

    def setup(self, pin, mode):
        self.chip.config(pin, mode)

    def input(self, pin):
        return self.chip.input(pin)

    def output(self, pin, value):
        self.chip.output(pin, value)

if __name__ == "__main__":

    # create a new PCA9555 object
    ioExpander = PCA95XX(1,0x21,16)

    #set 1 for input
    ioExpander.config(0, 1)

    while True:
    # if button is pressed, invert output
    #if ioExpander.getInput() & 0x8000:
    #    print "pin 15 "
        if ioExpander.input(0) :
            print "pin 0 "




        def cb_live(self):
            try:
                start = time.time()

                #TODO just take an image
                # initialize the camera and grab a reference to the raw camera capture
                camera = PiCamera(resolution=(640,480))
                rawCapture = PiRGBArray(camera)

                # allow the camera to warmup
                time.sleep(0.1)

                # grab an image from the camera
                camera.capture(rawCapture, format="bgr")
                image = rawCapture.array

                imgT = imutils.rotate_bound(image, -90)  # right side up

                cropped=imgT[20:80,10:300]

                cv2.imwrite("../pictures/cropped.jpeg", cropped)

                # run google cloud visison analysis
                result, vertices = run_detect_text()
                # show text description
                self.gcv_result.setText(result)

                #cv2.imwrite(("../log_files/{}.jpeg").format(result))
                # update displays and store result
                end = time.time() - start
                self.lcd_update_time.display(end)

            except TypeError:
                print "No image frame"
