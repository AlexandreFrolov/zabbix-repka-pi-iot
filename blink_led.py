#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RepkaPi.GPIO as GPIO
from time import sleep

GPIO.setboard(GPIO.REPKAPI3)

#GPIO.setmode(GPIO.BOARD)
#pin = 11

#GPIO.setmode(GPIO.BCM)
#pin = 17

GPIO.setmode(GPIO.SUNXI)
pin = "PA8"

GPIO.setup(pin, GPIO.OUT)

try:
    print ("Press CTRL+C to exit")
    while True:
        GPIO.output(pin, 1)
        sleep(0.1)
        GPIO.output(pin, 0)
        sleep(1)
except KeyboardInterrupt:
    GPIO.output(pin, 0)
    GPIO.cleanup()
    print ("Bye.")