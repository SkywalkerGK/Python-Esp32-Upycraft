from machine import Pin
import NeoPixelLib
sw1=Pin(0,Pin.IN)
np = NeoPixelLib.NeoPixel(Pin(12),3)
while True:
  if(sw1.value()==0):
    np.brightness=0.1
    np[0]=(127,0,0)
    np[1]=(0,127,0)
    np[2]=(0,0,127)
    np.write()
  else:
    np.clear()
    np.write()


