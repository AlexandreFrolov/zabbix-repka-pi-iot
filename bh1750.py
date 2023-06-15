import smbus2
import time

bus = smbus2.SMBus(1)
address = 0x23
command = 0x10

bus.write_byte(address, command)
time.sleep(0.5)
data = bus.read_i2c_block_data(address, command, 2)
illuminance = round((data[1] + (256 * data[0])) / 1.2)
print(illuminance)

