import smbus
import json

DEVICE_BUS = 1
DEVICE_ADDR = 0x17

TEMP_REG = 0x01
BMP280_TEMP_REG = 0x08
BMP280_PRESSURE_REG_L = 0x09
BMP280_PRESSURE_REG_M = 0x0A
BMP280_PRESSURE_REG_H = 0x0B
BMP280_STATUS = 0x0C
HUMAN_DETECT = 0x0D

bus = smbus.SMBus(DEVICE_BUS)

data = {
    "status": bus.read_byte_data(DEVICE_ADDR, BMP280_STATUS),
    "temperature": bus.read_byte_data(DEVICE_ADDR, BMP280_TEMP_REG),
    "pressure": (bus.read_byte_data(DEVICE_ADDR, BMP280_PRESSURE_REG_L) | bus.read_byte_data(DEVICE_ADDR, BMP280_PRESSURE_REG_M) << 8 | bus.read_byte_data(DEVICE_ADDR, BMP280_PRESSURE_REG_H) << 16)
}

print(json.dumps(data));