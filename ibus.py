import serial


baudrate = 115200 
protocol_len = b'\x20'
command_code = b'\x40'

# Открываем последовательный порт
ser = serial.Serial('/dev/ttyS1', baudrate)

# Формируем пакет данных с углами roll, pitch и yaw
roll = 1000
pitch = 1500
yaw = 2000

data = b'\x20\x40' + roll.to_bytes(2, 'little') + pitch.to_bytes(2, 'little') + yaw.to_bytes(2, 'little') + b'\x00\x00\x00\x00\x00\x00\x00\x00'  # Пример данных iBUS

# Вычисляем checksum
checksum = 65535 - (roll + pitch + yaw)
data += checksum.to_bytes(1, 'little')

try:
    while True:
        # Отправляем данные через последовательный порт
        ser.write(data)
except KeyboardInterrupt:
    # Закрываем порт
    ser.close()