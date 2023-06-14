#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RepkaPi.GPIO as GPIO
GPIO.setboard(GPIO.REPKAPI3)
GPIO.setmode(GPIO.BOARD)
from time import sleep

pin = 11
GPIO.setup(pin, GPIO.OUT)

try:
    print ("Press CTRL+C to exit")
    while True:
        GPIO.output(pin, 1)
        sleep(0.1)
        GPIO.output(pin, 0)
        sleep(0.1)
        GPIO.output(pin, 1)
        sleep(0.1)
        GPIO.output(pin, 0)
        sleep(0.5)

except KeyboardInterrupt:
    GPIO.output(pin, 0)
    GPIO.cleanup()
    print ("Bye.")