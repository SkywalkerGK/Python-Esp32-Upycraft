
import BlynkLib
import network
import time
import machine
import NeoPixelLib
import usocket as socket
import ussl as ssl
from machine import Pin

np=NeoPixelLib.NeoPixel(Pin(12),3)
RED   = (255,0,0)
YELLOW= (255,150,10)
GREEN = (0,255,0)

np.clear()
np[2]=RED
np.write()
print("Red ON")

WIFI_SSID = "Only Me"
WIFI_PASS = "fernonly"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)    
wifi.connect(WIFI_SSID,WIFI_PASS)
while not wifi.isconnected() :
  pass
print(wifi.ifconfig())

BLYNK_AUTH = '75QpX-K0wiUrpZH-Ss2N7qqHZO2kuWt6'
blynk = BlynkLib.Blynk(BLYNK_AUTH)



def on_connect():
  print("connected") 
blynk.on_connect(on_connect)

def on_disconnect():
  print("disconnected")
blynk.on_disconnect(on_disconnect)

def Red(A):
      if(np[2]==RED):
        np.clear()
        print("Red OFF")
        np[0]=GREEN
        np.write()
        print("Green ON")
      elif(np[0]==GREEN):
        np.clear()
        print("Green OFF")      
        np[1]=YELLOW
        np.write()
        print("Yellow ON")
        time.sleep(2)
        np.clear()
        print("Yellow OFF")
        np[2]=RED
        np.write()
        print("Red ON")
        oled.fill(0)
        time.sleep_ms(1)
blynk.add_virtual_pin(1, write=Red)

def Green(G):
  if(np[2]==RED):
        np.clear()
        print("Red OFF")
        np[0]=GREEN
        np.write()
        print("Green ON")
blynk.add_virtual_pin(2, write=Green)


blynk.run()












