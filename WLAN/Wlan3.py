


sta_if=None
ap_if=None
import time
def connect_wifi(ssid,pwd):
  import network
  import time
  
  counter = 0
  global sta_if,ap_if
  sta_if = network.WLAN(network.STA_IF)
  
  sta_if.active(True)
  cfg=('192.168.31.219','255.255.255.0','192.168.31.1','8.8.8.8')
  sta_if.ifconfig(cfg)
  
  sta_if.connect(ssid,pwd)
  while not sta_if.isconnected() and counter < 10 :
    counter += 1
    print(".",end="")
    time.sleep(1)
  if sta_if.isconnected():
    print("Connected my IP :",sta_if.ifconfig()[0])
    return True
  else:
    print("Connection fail !")
    return False
    
import socket
from machine import Pin
blue=Pin(23,Pin.OUT)
green = Pin(19,Pin.OUT)
red = Pin(5,Pin.OUT)
port = 4210
s=None
try:
  if(connect_wifi("TelecomPractice","thereisnospoon")):
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip=sta_if.ifconfig()[0]
    s.bind((ip,port))
    print('waiting...')
    while True:
      data,addr=s.recvfrom(1024)
      print('received:',data, 'from',addr)
      if(data==b'a=0'):
        if(green.value()==0 and red.value()==0):
          red.value(1)
          s.sendto("Turn ON RED\n",addr)
        if(green.value()==1):
          green.value(0)
          blue.value(1)
          s.sendto("Turn ON Yellow\n",addr)
          time.sleep(1.5)
          blue.value(0)    
          red.value(1)
        if(red.value()==1):
          red.value(1)
          s.sendto("Turn ON Red\n",addr)
      elif(data==b'a=1'):
        green.value(1)
        red.value(0)
        blue.value(0)
        s.sendto("Turn ON Green\n",addr)
      else:
        s=sendto("Unknow command\n",addr)
finally:
  if(s):
    s.close()
  sta_if.disconnect()
  sta_if.active(False)



