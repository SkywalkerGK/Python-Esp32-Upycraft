
import socket
import time
sta_if=None
ap_if=None
from machine import Pin

port=4210
sw1=Pin(32,Pin.IN)
sw2=Pin(33,Pin.IN)

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
sever_ip='192.168.31.217'
sever_port=4210
s=None
try:
  if(connect_wifi("TelecomPractice","thereisnospoon")):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP
    s.connect((sever_ip,sever_port))
    while True:
      if(sw1.value()==0):
        s.sendto(b'a=1',(sever_ip,sever_port))
        data=s.readline()
        print("Response =",data)
        time.sleep(0.5)
      if(sw2.value()==0):
        s.sendto(b'a=0',(sever_ip,sever_port))
        data=s.readline()
        print("Response =",data)
        time.sleep(0.5)
       
except NameError as err:
  print("NameError: {0}" .format(err))
    
except:
  if(s):
    print("close socket exit program")
    s.close()
  sta_if.disconnect()
  sta_if.active(False)

