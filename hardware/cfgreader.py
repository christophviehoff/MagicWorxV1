from configobj import ConfigObj
from validate import Validator
import sys


def read_bin_config(target):

    validator = Validator()
    config = ConfigObj('../configurations/bin_control.ini' ,configspec='../configurations/bin_control_configspec.ini')

    #   Validator converts type automatically
    result = config.validate(validator)
    if not result:
        print 'Config file validation failed!'
        sys.exit(1)

    return config[target]



def read_camera_config(target):

    validator = Validator()
    config = ConfigObj('../configurations/camera.ini' ,configspec='../configurations/camera_configspec.ini')

    #   Validator converts type automatically
    result = config.validate(validator)
    if not result:
        print 'Config file validation failed!'
        sys.exit(1)

    camera_cfg = config[target]

    name = camera_cfg['name']
    startY = camera_cfg['startY']
    endY = camera_cfg['endY']
    startX = camera_cfg['startX']
    endX = camera_cfg['endX']


    return name,startY,endY,startX,endX