import smbus2 #Добавляем модули
import time #Добавляем модули

# Инициализация шины I2C
bus = smbus2.SMBus(1)

# Адрес датчика BH1750
address = 0x23

# Команда для измерения освещенности в непрерывном режиме, разрешение 1 люкс
command = 0x10

# Отправка команды датчику
bus.write_byte(address, command)

# Задержка для измерения
time.sleep(0.5)

# Чтение данных из датчика
data = bus.read_i2c_block_data(address, command, 2)

# Преобразование данных в освещенность
illuminance = (data[1] + (256 * data[0])) / 1.2

# Вывод результатов
print("Освещенность: {} люкс".format(illuminance))

