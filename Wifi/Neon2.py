

import network


ap_if=network.WLAN(network.AP_IF)

ap_if.active(True)

ap_if.config(essid="Bass",password="bc20cf7f5c5e")
ap_if.config(channel=19,authmode=network.AUTH_WPA2_PSK)

import socket
import time
from machine import Pin
port = 4210
blue = Pin(23,Pin.OUT)
green = Pin(19,Pin.OUT)
red = Pin(5,Pin.OUT)
x=0
y=0
z=0

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip=ap_if.ifconfig()[0]
s.bind((ip,port))
print('waiting...')

while True:
  data,addr=s.recvfrom(1024)
  print('received:',data, 'from',addr)
  if(data==b'a=0'):
    x=1-x
    red.value(x)
    s.sendto("RED\n",addr)
  elif(data==b'a=1'):
    y=1-y
    blue.value(y)
    s.sendto("Blue\n",addr)
  elif(data==b'a=2'):
    z=1-z
    green.value(z)
    s.sendto("Green\n",addr)
  else:
    s=sendto("Unknow command\n",addr)


