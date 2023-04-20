
# MQTT-LED.py : Opas Sirikunchittavorn
#Result: input MQTTlibrary and remote controls LED by mqtt communication.

from umqtt.simple import MQTTClient
from machine import Pin
import network
import time
import dht
d=dht.DHT22(Pin(19))

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
blue=Pin(23,Pin.OUT)
green = Pin(19,Pin.OUT)
red = Pin(5,Pin.OUT)
def sub_cb(topic, msg):
  print((topic, msg))
  if msg == b"on":
    if(green.value()==0 and red.value()==0):
      red.value(1)
      c.publish("/OpenKB-19/pin18/status",'red')
      print("red")
    if(green.value()==1):
      green.value(0)
      blue.value(1)
      c.publish("/OpenKB-19/pin18/status",'blue')
      print("blue")
      time.sleep(1.5)
      blue.value(0)    
      red.value(1)
      print("red")
    if(red.value()==1):
      red.value(1)
      c.publish("/OpenKB-19/pin18/status",'red')
      print("red")
  elif msg == b"off":
    green.value(1)
    red.value(0)
    blue.value(0)
    c.publish("/OpenKB-19/pin18/status",'green')
    print("green")
  else:
    c.publish("/OpenKB-19/pin18/status",'red')
    
    
 

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






