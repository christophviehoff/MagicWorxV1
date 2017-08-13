# -*- coding: utf-8 -*-

"""
implentation of 3x MCP 32007 ioplus baord configurations
for limit switches and reflective sensors
"""
import RPi.GPIO as GPIO
import wiringpi,smbus,sys


def cb_beam_broken(channel):
    print "beam broken event detected"


def init():

    wiringpi.wiringPiSetup()  # initialise wiringpi in native pin mode

    # setup break beam sensor
    GPIO.setmode(GPIO.BCM)
    # GPIO 24 set up as input, pulled up to avoid false detection.
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #######################################################################
    # IO expander setup ioplus board 1, bus1 (Switches) and bus2 (Sensors)
    #######################################################################

    # wiringpi.mcp23017Setup(pin_base, i2c_addr) Bus 1 (16 switches)
    # 0 =input, 1 =output , 2 =PWM


    try:
        smbus.SMBus(1).read_byte_data(0x20, 0x00)
    except IOError:
        print "Could not open the i2c bus Expander IO at address 0x20."
        print "Please check that i2c devices are connected and powered up"
        #sys.exit()
    else:

        wiringpi.mcp23017Setup(65, 0x20)

        wiringpi.pinMode(65, 2)  # sets GPA0 to input PWM fro neopixel
        wiringpi.pinMode(66, 0)  # sets GPA1 to input
        wiringpi.pinMode(67, 0)  # sets GPA2 to input
        wiringpi.pinMode(68, 0)  # sets GPA3 to input
        wiringpi.pinMode(69, 0)  # sets GPA4 to input
        wiringpi.pinMode(70, 0)  # sets GPA5 to input
        wiringpi.pinMode(71, 0)  # sets GPA6 to input
        wiringpi.pinMode(72, 0)  # sets GPA7 to input
        wiringpi.pinMode(73, 0)  # sets GPB0 to input
        wiringpi.pinMode(74, 0)  # sets GPB1 to input
        wiringpi.pinMode(75, 0)  # sets GPB2 to input
        wiringpi.pinMode(76, 0)  # sets GPB3 to input
        wiringpi.pinMode(77, 0)  # sets GPB4 to input
        wiringpi.pinMode(78, 0)  # sets GPB5 to input
        wiringpi.pinMode(79, 0)  # sets GPB6 to input
        wiringpi.pinMode(80, 0)  # sets GPB7 to input

    # Note: MCP23017 has no internal pull-down, so we use pull-up instead and a NC contact to GND
    # 0= deactivate, 1 =pull-down, 2=pull-up

        wiringpi.pullUpDnControl(65, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(66, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(67, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(68, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(69, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(70, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(71, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(72, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(73, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(74, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(75, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(76, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(77, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(78, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(79, 2)  # set internal pull-up
        wiringpi.pullUpDnControl(80, 2)  # set internal pull-up

    # wiringpi.mcp23017Setup(pin_base, i2c_addr) Bus 2 (8 sensors + 8 spare)

    try:
        smbus.SMBus(1).read_byte_data(0x21, 0x00)
    except IOError:
        print "Could not open the i2c bus Expander IO at address 0x21."
        print "Please check that i2c devices are connected and powered up"
        #sys.exit()
    else:
        wiringpi.mcp23017Setup(81, 0x21)

        wiringpi.pinMode(81, 0)  # sets GPA0 to input
        wiringpi.pinMode(82, 0)  # sets GPA1 to input
        wiringpi.pinMode(83, 0)  # sets GPA2 to input
        wiringpi.pinMode(84, 0)  # sets GPA3 to input
        wiringpi.pinMode(85, 0)  # sets GPA4 to input
        wiringpi.pinMode(86, 0)  # sets GPA5 to input
        wiringpi.pinMode(87, 0)  # sets GPA6 to input
        wiringpi.pinMode(88, 0)  # sets GPA7 to input
        wiringpi.pinMode(89, 0)  # sets GPB0 to input
        wiringpi.pinMode(90, 0)  # sets GPB1 to input
        wiringpi.pinMode(91, 0)  # sets GPB2 to input
        wiringpi.pinMode(92, 0)  # sets GPB3 to input
        wiringpi.pinMode(93, 0)  # sets GPB4 to input
        wiringpi.pinMode(94, 0)  # sets GPB5 to input
        wiringpi.pinMode(95, 0)  # sets GPB6 to input
        wiringpi.pinMode(96, 0)  # sets GPB7 to input

    # Note: no internal pull-up for sensors required
        wiringpi.pullUpDnControl(81, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(82, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(83, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(84, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(85, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(86, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(87, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(88, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(89, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(90, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(91, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(92, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(93, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(94, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(95, 0)  # set internal pull-up
        wiringpi.pullUpDnControl(96, 0)  # set internal pull-up

    #######################################################################
    # IO expander setup ioplus board 2, bus1 (Switches) and bus2 (Sensors)
    #######################################################################

    try:
        smbus.SMBus(1).read_byte_data(0x22, 0x00)
    except IOError:
        print "Could not open the i2c bus Expander IO at address 0x22."
        print "Please check that i2c devices are connected and powered up"
        #sys.exit()
    else:
        wiringpi.mcp23017Setup(97, 0x22)
        wiringpi.pinMode(97, 0)  # sets GPB0 to input
        wiringpi.pullUpDnControl(97, 2)  # set internal pull-up

    try:
        smbus.SMBus(1).read_byte_data(0x23, 0x00)
    except IOError:
        print "Could not open the i2c bus Expander IO at address 0x23."
        print "Please check that i2c devices are connected and powered up"
        #sys.exit()
    else:
        wiringpi.mcp23017Setup(115, 0x23)
        wiringpi.pinMode(115, 0)  # sets GPB0 to input

    #######################################################################
    # IO expander setup ioplus board 3, bus1 (Switches) and bus2 (Sensors)
    #######################################################################

    try:
        smbus.SMBus(1).read_byte_data(0x24, 0x00)
    except IOError:
        print "Could not open the i2c bus Expander IO at address 0x24."
        print "Please check that i2c devices are connected and powered up"
        #sys.exit()
    else:
        wiringpi.mcp23017Setup(131, 0x24)
        wiringpi.pinMode(131, 0)  # sets GPB0 to input
        wiringpi.pullUpDnControl(131, 2)  # set internal pull-up


    try:
        smbus.SMBus(1).read_byte_data(0x25, 0x00)
    except IOError:
        print "Could not open the i2c bus Expander IO at address 0x25."
        print "Please check that i2c devices are connected and powered up"
        #sys.exit()
    else:
        wiringpi.mcp23017Setup(147, 0x25)
        wiringpi.pinMode(147, 0)  # sets GPB0 to input



