#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smbus2
import bme280
import json
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
import time
from time import sleep
import RepkaPi.GPIO as GPIO
GPIO.setboard(GPIO.REPKAPI3)
GPIO.setmode(GPIO.BOARD)

pin = 11
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, 1)
sleep(0.1)

pin2 = 13
GPIO.setup(pin2, GPIO.IN) 
sleep(0.1)
no_water = GPIO.input(pin2)    
sleep(0.1)

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)
temper=data.temperature
press= data.pressure
humi=data.humidity

address = 0x23
command = 0x10
bus.write_byte(address, command)
time.sleep(0.5)
data = bus.read_i2c_block_data(address, command, 2)
illuminance = round((data[1] + (256 * data[0])) / 1.2)

device = ssd1306(port=1, address=0x3C)
font = ImageFont.load_default()
with canvas(device) as draw:
    draw.text((0, 0), "temp: " + str(round(temper, 1)) + " C", font=font, fill="white")
    draw.text((0, 10), "press: "  + str(round(press, 1)) + " hPa", font=font, fill="white")
    draw.text((0, 20), "humi: "  + str(round(humi, 1)) + " %", font=font, fill="white")
    draw.text((0, 30), "luxur: "  + str(round(illuminance, 1)) + " Lux", font=font, fill="white")
    if no_water:
      draw.text((0, 40), "No water: "  + str(no_water), font=font, fill="white")
    else:
      draw.text((0, 40), "WATER DETECTED!", font=font, fill="white")
sleep(10)
device.command(0xAE)

sleep(1)
GPIO.output(pin, 0)
sleep(0.1)
GPIO.cleanup()
