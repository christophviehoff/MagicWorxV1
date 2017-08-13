
import wiringpi
import pifacedigitalio
from time import sleep

PIFACE=200
PIFACE_OUT=200  # output bits 0...7
PIFACE_IN=208   # input  bits 8..15

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


def init():
   #somehow enables piface
    pifacedigital = pifacedigitalio.PiFaceDigital()

    #######################################################################
    # IO expander setup SPI piFace2 (for conveyor relay control)
    #######################################################################


    wiringpi.mcp23s17Setup(PIFACE,0,0)
        #0..7 ARE THE OUTPUTS r1,r2
        #8,9,10,11 INPUTS s1..4
        #12 BREAK bEam



if __name__ == "__main__":

    init()

    #just the LED's
    for pin in range(3,8):
        wiringpi.digitalWrite(PIFACE + pin, ON)
        sleep(1)

    for pin in range(3, 8):
        wiringpi.digitalWrite(PIFACE + pin, OFF)

    print "piface LED test complete !"