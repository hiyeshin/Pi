from Adafruit_ADS1x15 import ADS1x15
from time import sleep

adc = ADS1x15()

while True:
        result_2 = adc.readADCSingleEnded(2)
        print "A2 : "
        print result_2
        sleep(.5)

        result_3 = adc.readADCSingleEnded(3)
        print "A3 : "
        print result_3
        sleep(.5)
