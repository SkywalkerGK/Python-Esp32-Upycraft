from umqtt.simple import MQTTClient
from machine import Pin
import network
import time
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),64)
button=Pin(32,Pin.IN)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)

import LibHR2
import urequests , ujson
SSID="OPPO A91"
PASSWORD="0817260364"

led=Pin(18, Pin.OUT, value=0)
SERVER= "mqtt.eclipse.org"  #  "137.135.83.217"
server_port = 1883
CLIENT_ID = "EnET-group01"
TOPIC = b"/OpenKB-19/pin18/set"
username=''
password=''
c=None

def sub_cb(topic, msg):
  print((topic, msg))
  if msg == b"on":
    led.value(1)
    print("LED on")
  elif msg == b"off":
    led.value(0)    
    print("LED off")

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)         #create a wlan object
  wlan.active(True)                         #Activate the network interface
  wlan.disconnect()                         #Disconnect the last connected WiFi
  wlan.connect(ssid,passwd)                 #connect wifi
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)

    
#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
  connectWifi(SSID,PASSWORD)
  server=SERVER
  c = MQTTClient(CLIENT_ID, server,server_port)     #create a mqtt client
  c.set_callback(sub_cb)                    #set callback
  c.connect()                               #connect mqtt
  c.subscribe(TOPIC)                        #client subscribes to a topic
  print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

  while True:

    c.wait_msg()                            #wait message 

finally:
    if(c is not None):
        c.disconnect()
    wlan.disconnect()
    wlan.active(False)










