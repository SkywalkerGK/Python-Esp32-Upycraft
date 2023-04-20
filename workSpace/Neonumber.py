from machine import Pin
import time
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),64)
RED=(255,0,0)
GREEN=(0,255,0)
B=(15,200,20)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
while True:
    np.brightness=0.01
    np.fill(BLACK)
    np.write()
    time.sleep(0.5)
    np[11]=RED ;np[12]=RED
    np.write()
    time.sleep(0.5)
  
    np[5]=RED ;np[6]=RED
    np.write()
    time.sleep(0.5)
 
    np[15]=RED ;np[23]=RED
    np.write()
    time.sleep(0.5)
   
    np[30]=RED ;np[37]=RED
    np.write()
    time.sleep(0.5)
   
    np[44]=RED ;np[43]=RED
    np.write()
    time.sleep(0.5)
    
    np[34]=RED ;np[25]=RED
    np.write()
    time.sleep(0.5)
    
    np[16]=RED ;np[8]=RED
    np.write()
    time.sleep(0.5)
    
    np[1]=RED ;np[2]=RED
    np.write()
    time.sleep(0.5) 
 
