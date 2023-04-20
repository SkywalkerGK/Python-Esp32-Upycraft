




from machine import Pin
import time
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),64)
np.fill((0,0,0))
np.write()



while True:
    np.brightness=0.005
    np.rainbow_cycle(100)
    np.write()    
    














