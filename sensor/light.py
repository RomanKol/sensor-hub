import smbus
import json

DEVICE_BUS = 1
DEVICE_ADDR = 0x17


LIGHT_REG_L = 0x02
LIGHT_REG_H = 0x03

bus = smbus.SMBus(DEVICE_BUS)

print(json.dumps({
    "low": bus.read_byte_data(DEVICE_ADDR, LIGHT_REG_L),
    "high": bus.read_byte_data(DEVICE_ADDR, LIGHT_REG_H) ,
}))