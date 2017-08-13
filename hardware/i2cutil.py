import smbus,subprocess,sys


def check_i2c_devices():
    print
    print "listing of all i2c devices on the i2cbus"
    print
    subprocess.call(['i2cdetect', '-y', '1'])
    # check if any i2c devices are present
    print
    if not is_connected_to_device(0x70): sys.exit()


def is_connected_to_device(address):
    try:
        smbus.SMBus(1).read_byte_data(address,0x00)
    except IOError:
        print "Could not open the i2c bus at address {} ".format(hex(address))
        print "Please check that i2c device is connected and powered up"
        print
        return False
    else:
        return True


def list_of_i2c_devices():
    # list of available com ports
    i2c_devices = []
    # select only the dispenser via the VID identifier
    for address in range(0x00,0x71):
        try:
            smbus.SMBus(1).read_byte_data(address, 0x00)
        except IOError:
            pass
        else:
            i2c_devices.append(hex(address))

    return i2c_devices

def list_of_i2c_servos():
    # list of available com ports
    i2c_devices = []
    # select only the dispenser via the VID identifier
    for address in range(0x40,0x4F):
        try:
            smbus.SMBus(1).read_byte_data(address, 0x00)
        except IOError:
            pass
        else:
            i2c_devices.append(hex(address))

    return i2c_devices

def list_of_i2c_steppers():
    # list of available com ports
    i2c_devices = []
    # select only the dispenser via the VID identifier
    for address in range(0x60,0x6F):
        try:
            smbus.SMBus(1).read_byte_data(address, 0x00)
        except IOError:
            pass
        else:
            i2c_devices.append(hex(address))

    return i2c_devices

def list_of_i2c_io():
    # list of available com ports
    i2c_devices = []
    # select only the dispenser via the VID identifier
    for address in range(0x20,0x2F):
        try:
            smbus.SMBus(1).read_byte_data(address, 0x00)
        except IOError:
            pass
        else:
            i2c_devices.append(hex(address))

    return i2c_devices




if __name__ == "__main__":

    print list_of_i2c_devices()

    print "i2c scan test test complete !"