from machine import Pin
import time
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),64)
import NeoPixelLib2
mp = NeoPixelLib2.NeoPixel(Pin(23),64)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(15,200,20)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
def hr3(): 
  np.clear
  np[15]=RED ;np[13]=RED ;np[14]=RED   #33333
  np[29]=RED ;np[31]=RED ;np[23]=RED
  np[30]=RED ;np[39]=RED ;np[45]=RED ;np[47]=RED ;np[46]=RED
  np.write()  
def hr4():
  np.clear 
  np[21]=RED ;np[13]=RED ;np[29]=RED   #33333
  np[31]=RED ;np[30]=RED ;np[15]=RED
  np[23]=RED ;np[39]=RED ;np[47]=RED 
  np.write()  
def hr5():  
  np.clear  
  np[15]=RED ;np[13]=RED ;np[14]=RED   #55555
  np[31]=RED ;np[30]=RED ;np[29]=RED
  np[21]=RED ;np[39]=RED ;np[45]=RED
  np[46]=RED ;np[47]=RED  
  np.write()    
def np0(): 
  mp.clear()
  mp[11]=RED ;mp[9]=RED ;mp[10]=RED   #000
  mp[27]=RED ;mp[17]=RED ;mp[33]=RED ;mp[19]=RED
  mp[25]=RED ;mp[35]=RED ;mp[43]=RED ;mp[42]=RED ;mp[41]=RED
  mp.write() 
def np1(): 
  mp.clear()
  mp[34]=RED ;mp[18]=RED ;mp[10]=RED   #11111
  mp[42]=RED ;mp[26]=RED 
  mp.write()
def np2(): 
  mp.clear()
  mp[11]=RED ;mp[9]=RED ;mp[10]=RED   #2222222222
  mp[27]=RED ;mp[26]=RED ;mp[19]=RED
  mp[25]=RED ;mp[33]=RED ;mp[43]=RED ;mp[42]=RED ;mp[41]=RED
  mp.write()
np.brightness=0.01
mp.brightness=0.01
while True:
  hr3()
  np0()
  time.sleep(0.5)
  hr4()
  np1()
  time.sleep(0.5)
  hr5()
  np2()
  time.sleep(0.5)
