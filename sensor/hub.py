import smbus
import json

DEVICE_BUS = 1
DEVICE_ADDR = 0x17

TEMP_REG = 0x01
LIGHT_REG_L = 0x02
LIGHT_REG_H = 0x03
STATUS_REG = 0x04
ON_BOARD_TEMP_REG = 0x05
ON_BOARD_HUMIDITY_REG = 0x06
ON_BOARD_SENSOR_ERROR = 0x07
BMP280_TEMP_REG = 0x08
BMP280_PRESSURE_REG_L = 0x09
BMP280_PRESSURE_REG_M = 0x0A
BMP280_PRESSURE_REG_H = 0x0B
BMP280_STATUS = 0x0C
HUMAN_DETECT = 0x0D

bus = smbus.SMBus(DEVICE_BUS)

data = {
    "temperature-probe": bus.read_byte_data(DEVICE_ADDR, TEMP_REG),
    "light": {
        "low": bus.read_byte_data(DEVICE_ADDR, LIGHT_REG_L),
        "heigh": bus.read_byte_data(DEVICE_ADDR, LIGHT_REG_H),
    },
    "status": bus.read_byte_data(DEVICE_ADDR, STATUS_REG),
    "onboard": {
        "temperature": bus.read_byte_data(DEVICE_ADDR, ON_BOARD_TEMP_REG),
        "humidity": bus.read_byte_data(DEVICE_ADDR, ON_BOARD_HUMIDITY_REG),
        "error": bool(bus.read_byte_data(DEVICE_ADDR, ON_BOARD_SENSOR_ERROR)),
    },
    "bmp280": {
        "temperature": bus.read_byte_data(DEVICE_ADDR, BMP280_TEMP_REG),
        "pressure": {
            "low": bus.read_byte_data(DEVICE_ADDR, BMP280_PRESSURE_REG_L),
            "medium": bus.read_byte_data(DEVICE_ADDR, BMP280_PRESSURE_REG_M),
            "heigh": bus.read_byte_data(DEVICE_ADDR, BMP280_PRESSURE_REG_H),
        },
        "status": bool(bus.read_byte_data(DEVICE_ADDR, BMP280_STATUS)),
    },
    "human": bool(bus.read_byte_data(DEVICE_ADDR, HUMAN_DETECT))
}

print(json.dumps(data))
