#!/user/bin/python3

import serial
from serial.tools import list_ports

# Get list of available ports
availablePorts = list_ports.comports()
portNumber = 0
for port in availablePorts:
     print(portNumber, port.device)
     portNumber += 1


ser = serial.Serial(availablePorts[0].device, 4800, timeout=1)

while True:
     x = ser.read(1200)
     index1 = x.find(b'$GPRMC')
     index2 = x.find(b'\n', index1)
     loc = x[index1:index2]
     data = loc.split(b',')

     try:
          if data[2] == b'V':
               print("No location found.\n")
          else:
               print("Latitude:", data[3], data[4])
               print("Longitude:", data[5], data[6])

     except:
          print("There was an error.\n")

