
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
    np[10]=RED ;np[11]=RED ;np[9]=RED   #0000
    np[17]=RED ;np[19]=RED 
    np[25]=RED ;np[27]=RED ;np[33]=RED 
    np[35]=RED
    np[41]=RED ;np[42]=RED ;np[43]=RED 
  
  
    np.brightness=0.01  
    np[10]=RED ;np[18]=RED ;np[26]=RED   #111111
    np[42]=RED ;np[34]=RED 
    
  
  
    #np[15]=RED ;np[13]=RED ;np[14]=RED   #2222222222
    #np[31]=RED ;np[30]=RED ;np[23]=RED
    #np[29]=RED ;np[37]=RED ;np[47]=RED ;np[46]=RED ;np[45]=RED
  
    #np[13]=RED ;np[15]=RED ;np[14]=RED #7777777777777
    #np[23]=RED
    #np[31]=RED ;np[39]=RED ;np[47]=RED 
    

    
        
    np.write()
 
 

