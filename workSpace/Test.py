

# TestBlynk1.py
import BlynkLib
import network
import time
from machine import Pin
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


WIFI_SSID = "thananat   2.4G"
WIFI_PASS = "0891550015"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect(WIFI_SSID,WIFI_PASS)
while not wifi.isconnected() :
  pass
print(wifi.ifconfig())

BLYNK_AUTH = 'XAJLy8wQFOqSdS6iGVWDXXJda6CLqUjk'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def my_user_task():
  for i in color_LIST:
    np.fill(i)
    np.write()
    print(i)
    time.sleep(1)
  

blynk.set_user_task(my_user_task,2000)
blynk.run()






