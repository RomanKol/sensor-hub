import smbus
import json

DEVICE_BUS = 1
DEVICE_ADDR = 0x17

HUMAN_DETECT = 0x0D

bus = smbus.SMBus(DEVICE_BUS)

print(json.dumps({
    "human": bool(bus.read_byte_data(DEVICE_ADDR, HUMAN_DETECT))
}))
