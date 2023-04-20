from machine import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C
import HourLib
import MinuteLib
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
import NeoPixelLib
import NeoPixelLib2
np = NeoPixelLib.NeoPixel(Pin(19),64)
mp = NeoPixelLib2.NeoPixel(Pin(23),64)
RED=(255,0,0)
BLACK=(0,0,0)
BLUE=(0,0,255)  
 
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
  print(s[11])
  np.brightness=0.01
  mp.brightness=0.01
  if(s[11]=='0'):
    hd0()
    if(s[12]=='0'):
      hr0()
    elif(s[12]=='1'):
      hr1()
    elif(s[12]=='2'): 
      hr2()   
    elif(s[12]=='3'): 
      hr3()
    elif(s[12]=='4'): 
      hr4() 
    elif(s[12]=='5'): 
      hr5()    
    elif(s[12]=='6'): 
      hr6()      
    elif(s[12]=='7'):
      hr7()    
    elif(s[12]=='8'): 
      hr8()    
    elif(s[12]=='9'): 
      hr9()  
  elif(s[11]=='1'):   
    hd1()
    if(s[12]=='0'):
      hr0()
    elif(s[12]=='1'):
      hr1()
    elif(s[12]=='2'): 
      hr2()   
    elif(s[12]=='3'): 
      hr3()
    elif(s[12]=='4'): 
      hr4() 
    elif(s[12]=='5'): 
      hr5()    
    elif(s[12]=='6'): 
      hr6()      
    elif(s[12]=='7'):
      hr7()    
    elif(s[12]=='8'): 
      hr8()    
    elif(s[12]=='9'): 
      hr9()
  elif(s[11]=='2'):   
    hd2()
    if(s[12]=='0'):
      hr0()
    elif(s[12]=='1'):
      hr1()
    elif(s[12]=='2'): 
      hr2()   
    elif(s[12]=='3'): 
      hr3()
    elif(s[12]=='4'): 
      hr4()
    elif(s[12]=='5'): 
      hr5()            
    elif(s[12]=='6'): 
      hr6()      
    elif(s[12]=='7'):
      hr7()    
    elif(s[12]=='8'): 
      hr8()    
    elif(s[12]=='9'): 
      hr9()  
  else:
    np.clear()
    np.write()  
  oled.fill(0)
  oled.text('{0}'.format(ss),2,2)  
  oled.show()  
  time.sleep(0.5)
  bct.close()
  





