#!/usr/bin/env python
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
from time import sleep

device = ssd1306(port=1, address=0x3C) # for RPi rev 2 port(smbus) = 1
font = ImageFont.load_default()

with canvas(device) as draw:
    draw.text((0, 0), "*** Hello World ***", font=font, fill="white")
    draw.text((0, 10), "Hello World! :)", font=font, fill="white")

sleep(3) # Wait 3 seconds.
device.command(0xAE) # Display OFF.
sleep(1) # Wait 1 second.
device.command(0xAF) # Display ON.
sleep(1)
device.command(0xAE)
sleep(1)
device.command(0xAF)
