#!/usr/bin/python3

import serial
from time import sleep

baudrate = 115200 
protocol_len = 0x20
command_code = 0x40
max_val = 0xffff
chanels_count = 14
setted_elems = 3
# Открываем последовательный порт
ser = serial.Serial('/dev/ttyS1', baudrate, bytesize=8, parity='N', stopbits=1, timeout=1, xonxoff=False, rtscts=False)
print('success opened')
# Формируем пакет данных с углами roll, pitch и yaw
roll = 1000
pitch = 1500
yaw = 2000
default = 1500

# Преобразуем шестнадцатеричное число protocol_len в десятичное и затем в байты
protocol_len_decimal = int(protocol_len)
protocol_len_bytes = protocol_len_decimal.to_bytes(1, 'big')
command_code_decimal = int(command_code)
command_code_bytes = command_code_decimal.to_bytes(1, 'big')

data = protocol_len_bytes + command_code_bytes + roll.to_bytes(2, 'little') + pitch.to_bytes(2, 'little') + yaw.to_bytes(2, 'little')

for _ in range(chanels_count - setted_elems):
    data += default.to_bytes(2, 'little')

# Вычисляем checksum
checksum = int(max_val) - (roll + pitch + yaw + default*(chanels_count - setted_elems))
data += checksum.to_bytes(2, 'little')
#data += int(max_val).to_bytes(1, 'big')
#ser.open()
try:
    while True:
        # Отправляем данные через последовательный порт
        ser.write(data)
        sleep(0.5)
        print('in:')
except KeyboardInterrupt:
    # Закрываем порт
    ser.close()