from machine import Pin

import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),64)
button=Pin(32,Pin.IN)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)

counter = 0
n=0
def inter(e):
  time.sleep_ms(20)
  if button.value()==0:
    global counter
    counter+=1
    print(counter)
button.irq(trigger=Pin.IRQ_FALLING,handler=inter)
import LibHR2



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
  ss=s[11:19]
  print(ss)
  np.brightness=0.01
  x=s[15]
  y=s[15]
  if(s[11]=='0'):
    hd0()
    if(s[12]=='0'):
      hr0()
    elif(s[12]=='1'):
      hr1()
    elif(s[12]=='2'): 
      hr2()    
  elif(s[11]=='2'):   
    hd2()
    if(s[12]=='0'):
      hr0() 
    elif(s[12]=='3'): 
      hr3()
  else:
    np.clear()
    np.write()
  while(x==y):
    bct = urequests.get('http://worldtimeapi.org/api/timezone/Asia/Bangkok')
    bct_js = bct.json()
    us_rate=bct_js['datetime']
    s=str(us_rate)
    ss=s[11:19]
    y=s[15]

    print(ss)

    
    if(counter==1):
      RED=GREEN
      if(n==0):
        x=555
        n=1
    if(counter==2):
      RED=BLUE
      if(n==1):
        x=555
        n=2
    if(counter==3):
      RED=YELLOW
      if(n==2):
        x=555
        n=3
   
    if(counter>3):
      RED=(255,0,0)
      counter=0
      if(n==3):
        x=555
        n=0          
   

   
    time.sleep(0.1)
    bct.close() 
    
           
 
  bct.close()
  












