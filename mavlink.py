#!/usr/bin/python3

from pymavlink import mavutil

# Устанавливаем параметры для подключения по UART
master = mavutil.mavlink_connection('/dev/ttyS1', baud=57600)

# Задаем угол крена (roll) в градусах (1000 = 1 градус)
roll = 1000

# Формируем сообщение MAVLink для установки угла крена (roll)
msg = master.mav.command_long_encode(
    master.target_system,                # System ID
    master.target_component,             # Component ID
    mavutil.mavlink.MAV_CMD_DO_SET_ROLL_PITCH_YAW_THRUST,  # Command
    0,                                   # Confirmation
    roll, 0, 0, 0, 0, 0, 0               # Parameters
)

# Отправляем сообщение
master.mav.send(msg)