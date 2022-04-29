import smbus
import json

DEVICE_BUS = 1
DEVICE_ADDR = 0x17

ON_BOARD_TEMP_REG = 0x05
ON_BOARD_HUMIDITY_REG = 0x06
ON_BOARD_SENSOR_ERROR = 0x07

bus = smbus.SMBus(DEVICE_BUS)

data = {
    "error": bus.read_byte_data(DEVICE_ADDR, ON_BOARD_SENSOR_ERROR),
    "temperature": bus.read_byte_data(DEVICE_ADDR, ON_BOARD_TEMP_REG),
    "humidity": bus.read_byte_data(DEVICE_ADDR, ON_BOARD_HUMIDITY_REG),
}

print(json.dumps(data));
