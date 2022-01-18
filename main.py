import serial
from telnetlib import Telnet
import time

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=1200, bytesize=7, 
    parity=serial.PARITY_EVEN, 
    stopbits=1,
    timeout = 0
    )

tn = Telnet('bbs.8bitclassics.com')
# Clear the screen
cw = [0x0C]
ser.write(serial.to_bytes(cw))



# while True:
#     data = ser.read()
#     if data:
#         # print (data)
#         tn.write(data)
    
#     data = tn.read_very_eager()

#     if data:
#         # print (data)
#         ser.write(data)
    
# cw = [0x1B, 0x3A, 0x31, 0x7D]
ser.write(serial.to_bytes(cw))
ser.write(b"J")
ser.write(b"Testing 123 ")

# ser.write(b'\x07\x0c\x1f\x40\x41connexion\x0a')
# ser.write(b'\x1b\x3b\x60\x58\x52')
while True:
    data = ser.read()
    print (data.hex())
