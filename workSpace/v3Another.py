from machine import Pin
import time
from machine import I2C
from ssd1306 import SSD1306_I2C
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),64)
RED=(255,0,0)
BLACK=(0,0,0)
BLUE=(0,0,255)



def dot():
  np.brightness=0.01
  np[16]=BLACK;np[32]=BLACK
  np.write()
  time.sleep(0.1) 
  np[16]=BLUE;np[32]=BLUE
  np.write()
  time.sleep(0.1)   

def np0(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #66666
  np[27]=RED ;np[17]=RED ;np[33]=RED ;np[19]=RED
  np[25]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write() 
def np1(): 
  np.clear()
  np[34]=RED ;np[18]=RED ;np[10]=RED   #11111
  np[42]=RED ;np[26]=RED 
  np.write()
def np2(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #2222222222
  np[27]=RED ;np[26]=RED ;np[19]=RED
  np[25]=RED ;np[33]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()
def np3(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #3333
  np[27]=RED ;np[26]=RED ;np[25]=RED
  np[19]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()
def np4(): 
  np.clear()
  np[17]=RED ;np[9]=RED ;np[25]=RED   #4444
  np[27]=RED ;np[11]=RED ;np[19]=RED
  np[26]=RED ;np[35]=RED ;np[43]=RED 
  np.write()
def np5(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #555
  np[27]=RED ;np[26]=RED ;np[17]=RED
  np[25]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()  
def np6(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #66666
  np[27]=RED ;np[26]=RED ;np[17]=RED ;np[33]=RED
  np[25]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write() 
def mp0():   
    np[14]=RED ;np[15]=RED ;np[13]=RED   #0000
    np[21]=RED ;np[23]=RED 
    np[29]=RED ;np[31]=RED ;np[37]=RED 
    np[39]=RED
    np[45]=RED ;np[46]=RED ;np[47]=RED  
    np.write()
def mp1():  
    np[14]=RED ;np[22]=RED ;np[30]=RED   #111111
    np[46]=RED ;np[38]=RED       
    np.write() 
def mp2():   
    np[15]=RED ;np[13]=RED ;np[14]=RED   #2222222222
    np[31]=RED ;np[30]=RED ;np[23]=RED
    np[29]=RED ;np[37]=RED ;np[47]=RED ;np[46]=RED ;np[45]=RED
    np.write()   
def mp3():     
    np[15]=RED ;np[13]=RED ;np[14]=RED   #33333
    np[29]=RED ;np[31]=RED ;np[23]=RED
    np[30]=RED ;np[39]=RED ;np[45]=RED ;np[47]=RED ;np[46]=RED
    np.write()  
def mp4():     
    np[21]=RED ;np[13]=RED ;np[29]=RED   #33333
    np[31]=RED ;np[30]=RED ;np[15]=RED
    np[23]=RED ;np[39]=RED ;np[47]=RED 
    np.write()  
def mp5():     
    np[15]=RED ;np[13]=RED ;np[14]=RED   #55555
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[39]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED  
    np.write()    
def mp6():    
    np[15]=RED ;np[13]=RED ;np[14]=RED   #6666
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[37]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED
    np.write() 
def mp7():       
    np[13]=RED ;np[15]=RED ;np[14]=RED #7777777777777
    np[23]=RED
    np[31]=RED ;np[39]=RED ;np[47]=RED 
    np.write() 
def mp8():       
    np[15]=RED ;np[13]=RED ;np[14]=RED   #88888
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[37]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED  
    np[23]=RED
    np.write() 
def mp9():       
    np[15]=RED ;np[13]=RED ;np[14]=RED   #99999
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED  
    np[23]=RED
    np.write()      
 

WIFI_SSID = "OPPA 91"
WIFI_PASS = "0817260364"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID,WIFI_PASS)
while not wifi.isconnected() :
  pass
print(wifi.ifconfig())
import urequests , ujson

while True:
  bct = urequests.get('http://worldtimeapi.org/api/timezone/Asia/Bangkok')
  bct_js = bct.json()
  us_rate=bct_js['datetime']
  s=str(us_rate)  
  ss=s[11:19]
  print(ss)
  np.brightness=0.01
  dot()
  if(s[14]=='0'):
    np0()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()  
  elif(s[14]=='1'):   
    np1()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()
  elif(s[14]=='2'):   
    np2()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 

      mp9()  
  elif(s[14]=='3'):   
    np3()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9() 
  elif(s[14]=='4'):   
    np4()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()       
  elif(s[14]=='5'):   
    np5()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 

      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()
  else:
    np.clear()
    np.write()  
  oled.fill(0)
  oled.text('{0}'.format(ss),2,2)  
  oled.show()  
  time.sleep(0.5)
  bct.close()
  






