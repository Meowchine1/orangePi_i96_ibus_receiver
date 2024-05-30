#!/usr/bin/python3

import serial

baudrate = 115200 
protocol_len = 0x20  # Используем шестнадцатеричное число напрямую, без кавычек
command_code = 0x40   # Используем шестнадцатеричное число напрямую, без кавычек

# Открываем последовательный порт
ser = serial.Serial('/dev/ttyS1', baudrate)
 
# Формируем пакет данных с углами roll, pitch и yaw
roll = 1000
pitch = 1500
yaw = 2000

# Преобразуем шестнадцатеричное число protocol_len в десятичное и затем в байты
protocol_len_decimal = int(protocol_len)
protocol_len_bytes = protocol_len_decimal.to_bytes(1, 'big')
command_code_decimal = int(command_code)
command_code_bytes = command_code_decimal.to_bytes(1, 'big')

data = protocol_len_bytes + command_code_bytes + roll.to_bytes(2, 'little') + pitch.to_bytes(2, 'little') + yaw.to_bytes(2, 'little')

# Вычисляем checksum
checksum = 65535 - (roll + pitch + yaw)
data += checksum.to_bytes(2, 'little')

try:
    while True:
        # Отправляем данные через последовательный порт
        ser.write(data)
except KeyboardInterrupt:
    # Закрываем порт
    ser.close()