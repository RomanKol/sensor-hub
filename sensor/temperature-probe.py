import smbus
import json

DEVICE_BUS = 1
DEVICE_ADDR = 0x17

TEMP_REG = 0x01
LIGHT_REG_L = 0x02
LIGHT_REG_H = 0x03
STATUS_REG = 0x04
HUMAN_DETECT = 0x0D


bus = smbus.SMBus(DEVICE_BUS)

aReceiveBuf = []

aReceiveBuf.append(0x00)

for i in range(TEMP_REG,HUMAN_DETECT + 1):
    aReceiveBuf.append(bus.read_byte_data(DEVICE_ADDR, i))

data = {
    "error": None,
    "temperature": None,
}

if aReceiveBuf[STATUS_REG] & 0x01 :
    data["error"] = "Off-chip temperature sensor overrange!"
elif aReceiveBuf[STATUS_REG] & 0x02 :
    data["error"] = "No external temperature sensor!"
else :
    data["temperature"] = aReceiveBuf[TEMP_REG]

print(json.dumps(data))