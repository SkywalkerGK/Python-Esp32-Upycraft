


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
LED=Pin(23,Pin.OUT)

port = 4210
s=None
try:
  if(connect_wifi("OPPO A91","0817260364")):
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip=sta_if.ifconfig()[0]
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
finally:
  if(s):
    s.close()
  sta_if.disconnect()
  sta_if.active(False)


