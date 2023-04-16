

sta_if=None
ap_if=None
from machine import Pin
def connect_wifi(ssid,pwd):

  import network
  import time

  counter =0

  global sta_if,ap_if

  sta_if = network.WLAN(network.STA_IF)
  sta_if.active(True)
  cfg =('192.168.31.219','255.255.255.0','192.168.31.1','8.8.8.8')
  sta_if.ifconfig(cfg)
  sta_if.connect(ssid,pwd)
  while not sta_if.isconnected()and counter<10:
    counter +=1
    print(".",end="")
    time.sleep(1)
  if sta_if.isconnected():
    print("Connected my IP :",sta_if.ifconfig()[0])
    return True

  else:

    print("connection fail!!")

    return False

import socket
import time
import dht
sever_ip="192.168.31.217"
sever_port=4210
s=None
from machine import I2C
from ssd1306 import SSD1306_I2C
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
try:
  if(connect_wifi("TelecomPractice","thereisnospoon")):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP
    s.connect((sever_ip,sever_port))
    while True:
      oled.fill(0)  
      s.sendto(b'temp=?',(sever_ip,sever_port))
      data=s.readline()#
      
      print("Response=",data)
      oled.text(data.decode(),1,15)
      oled.show()
      time.sleep(1.5)
      s.sendto(b'hum=?',(sever_ip,sever_port))
      data=s.readline()#
      print("Response=",data)
      oled.text(data.decode(),1,45)
      oled.show()

      time.sleep(1.5)
except NameError as err:
  print("NameError: {0}" .format(err))    
except:
  if(s):
    print("close socket exit program")
    s.close()
  sta_if.disconnect()
  sta_if.active(False)

