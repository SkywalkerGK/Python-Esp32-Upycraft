

from machine import Pin

def connect_wifi(ssid,pwd):
  import network
  import time
  
  counter = 0  
  global sta_if,ap_if
  sta_if = network.WLAN(network.STA_IF)
  
  sta_if.active(True)
  #cfg=('192.168.31.219','255.255.255.0','192.168.31.1','8.8.8.8')
 #sta_if.ifconfig(cfg)
  
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
connect_wifi("thananat   2.4G","0891550015")
import urequests , ujson







while True: 
  bct = urequests.get('http://worldtimeapi.org/api/timezone/Asia/Bangkok')
  bct_js = bct.json()
  us_rate=bct_js['datetime']
  s=str(us_rate)
  x=s[17]
  y=s[17]
  while(x==y):
    print('5')
    bct = urequests.get('http://worldtimeapi.org/api/timezone/Asia/Bangkok')
    bct_js = bct.json()
    us_rate=bct_js['datetime']
    s=str(us_rate)
    y=s[17]
    print('',x,y)
    time.sleep(0.5)
    bct.close()
  print('Loop')  
  time.sleep(0.5)  
  bct.close()  
  
    
    
    




  
  






