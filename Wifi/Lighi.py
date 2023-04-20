




import network


ap_if=network.WLAN(network.AP_IF)

ap_if.active(True)

ap_if.config(essid="Bass",password="bc20cf7f5c5e")
ap_if.config(channel=19,authmode=network.AUTH_WPA2_PSK)

import socket
import time
from machine import Pin
port = 4210
LED = Pin(18,Pin.OUT)


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip=ap_if.ifconfig()[0]
s.bind((ip,port))
print('waiting...')

while True:
  data,addr=s.recvfrom(1024)
  print('received:',data, 'from',addr)
  if(data==b'a=0'):
    LED.value(0)
    s.sendto("Turn OFF LED\n",addr)
  elif(data==b'a=1'):
    LED.value(1)
    s.sendto("Turn ON LED\n",addr)
  else:
    s=sendto("Unknow command\n",addr)





