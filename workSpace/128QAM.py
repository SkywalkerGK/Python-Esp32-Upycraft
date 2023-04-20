from machine import Pin
import time
np = NeoPixelLib.NeoPixel(Pin(19),128)
RED=(255,0,0)
i=0
np.brightness=0.01 
  
while True:
  if i<128:
    np.clear()
    np[i]=RED
    np.write()
    i=i+1
    time.sleep(0.1)
  else:
    i=0

  
    



