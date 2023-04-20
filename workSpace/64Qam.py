from machine import Pin
import time
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),128)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)

while True:
  np.brightness=0.01
  np.color_chase(MAGENTA,0.2)
  np.write()
