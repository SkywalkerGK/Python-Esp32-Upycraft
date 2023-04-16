

from machine import Pin
LED = Pin(18,Pin.OUT)



# TestBlynk1.py
import BlynkLib
import network
import time


WIFI_SSID = "OPPA 91"
WIFI_PASS = "0817260364"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect(WIFI_SSID,WIFI_PASS)
while not wifi.isconnected() :
  pass
print(wifi.ifconfig())

BLYNK_AUTH = 'XAJLy8wQFOqSdS6iGVWDXXJda6CLqUjk'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

blynk.run()





