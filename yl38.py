#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RepkaPi.GPIO as GPIO
from time import sleep

GPIO.setboard(GPIO.REPKAPI3)
GPIO.setmode(GPIO.SUNXI)
pin = "PA9"

GPIO.setup(pin, GPIO.IN) 
sleep(0.1)
print(GPIO.input(pin))

GPIO.cleanup()

