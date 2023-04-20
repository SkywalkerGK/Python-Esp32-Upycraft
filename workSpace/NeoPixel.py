from machine import Pin
import time
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(12),3)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
color_LIST = (RED,GREEN,BLUE,YELLOW,CYAN,MAGENTA,WHITE,BLACK)
np.brightness=0.1
while True:
  for i in color_LIST:
    np.fill(i)
    np.write()
    print(i)
    time.sleep(1)

