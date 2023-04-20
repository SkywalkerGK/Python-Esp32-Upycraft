from machine import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),128)
RED=(255,0,0)
BLACK=(0,0,0)
def hd0(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #0000
  np[27]=RED ;np[17]=RED ;np[33]=RED ;np[19]=RED
  np[25]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write() 
def hd1(): 
  np.clear()
  np[34]=RED ;np[18]=RED ;np[10]=RED   #11111
  np[42]=RED ;np[26]=RED 
  np.write()
def hd2(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #2222222222
  np[27]=RED ;np[26]=RED ;np[19]=RED
  np[25]=RED ;np[33]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()

def hr0():   
    np[14]=RED ;np[15]=RED ;np[13]=RED   #0000
    np[21]=RED ;np[23]=RED 
    np[29]=RED ;np[31]=RED ;np[37]=RED 
    np[39]=RED
    np[45]=RED ;np[46]=RED ;np[47]=RED  
    np.write()
def hr1():  
    np[14]=RED ;np[22]=RED ;np[30]=RED   #111111
    np[46]=RED ;np[38]=RED       
    np.write() 
def hr2():   
    np[15]=RED ;np[13]=RED ;np[14]=RED   #2222222222
    np[31]=RED ;np[30]=RED ;np[23]=RED
    np[29]=RED ;np[37]=RED ;np[47]=RED ;np[46]=RED ;np[45]=RED
    np.write()   

def hr3():     
    np[15]=RED ;np[13]=RED ;np[14]=RED   #33333
    np[29]=RED ;np[31]=RED ;np[23]=RED
    np[30]=RED ;np[39]=RED ;np[45]=RED ;np[47]=RED ;np[46]=RED
    np.write()  
def hr4():     
    np[21]=RED ;np[13]=RED ;np[29]=RED   #33333
    np[31]=RED ;np[30]=RED ;np[15]=RED
    np[23]=RED ;np[39]=RED ;np[47]=RED 
    np.write()  
def hr5():     
    np[15]=RED ;np[13]=RED ;np[14]=RED   #55555
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[39]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED  
    np.write()    
def hr6():    
    np[15]=RED ;np[13]=RED ;np[14]=RED   #6666
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[37]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED
    np.write() 
def hr7():       
    np[13]=RED ;np[15]=RED ;np[14]=RED #7777777777777
    np[23]=RED
    np[31]=RED ;np[39]=RED ;np[47]=RED 
    np.write() 
def hr8():       
    np[15]=RED ;np[13]=RED ;np[14]=RED   #88888
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[37]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED  
    np[23]=RED
    np.write() 
def hr9():       
    np[15]=RED ;np[13]=RED ;np[14]=RED   #99999
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED  
    np[23]=RED
    np.write()      
def np0(): 
  np[73]=RED ;np[74]=RED ;np[75]=RED   #66666
  np[81]=RED ;np[83]=RED ;np[89]=RED ;np[91]=RED
  np[97]=RED ;np[99]=RED ;np[105]=RED ;np[106]=RED ;np[107]=RED
  np.write() 
def np1(): 
  np[74]=RED ;np[82]=RED ;np[90]=RED   #11111
  np[98]=RED ;np[106]=RED 
  np.write()
def np2(): 
  np[73]=RED ;np[74]=RED ;np[75]=RED   #2222222222
  np[83]=RED ;np[89]=RED ;np[90]=RED
  np[91]=RED ;np[97]=RED ;np[105]=RED ;np[106]=RED ;np[107]=RED
  np.write()
def np3(): 
  np[73]=RED ;np[74]=RED ;np[75]=RED   #3333
  np[83]=RED ;np[89]=RED ;np[90]=RED
  np[91]=RED ;np[99]=RED ;np[105]=RED ;np[106]=RED ;np[107]=RED
  np.write()
def np4(): 
  np[73]=RED ;np[75]=RED ;np[81]=RED   #4444
  np[83]=RED ;np[89]=RED ;np[90]=RED
  np[91]=RED ;np[99]=RED ;np[107]=RED 
  np.write()
def np5(): 
  np[73]=RED ;np[74]=RED ;np[75]=RED   #555
  np[81]=RED ;np[89]=RED ;np[90]=RED
  np[91]=RED ;np[99]=RED ;np[105]=RED ;np[106]=RED ;np[107]=RED
  np.write()   

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
  else:
    np.clear()
    np.write()  
  oled.fill(0)
  oled.text('{0}'.format(ss),2,2)  
  oled.show()  
  time.sleep(0.5)
  bct.close()
  








