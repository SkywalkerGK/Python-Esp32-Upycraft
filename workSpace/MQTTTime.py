from umqtt.simple import MQTTClient
from machine import Pin
import network
import time
from machine import I2C
from ssd1306 import SSD1306_I2C
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(12),3)
import urequests , ujson


SSID="thananat   2.4G"
PASSWORD="0891550015"

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
    bct = urequests.get('http://worldtimeapi.org/api/timezone/Asia/Bangkok')
    bct_js = bct.json()
    us_rate=bct_js['datetime']
    s=str(us_rate)  
    ss=s[11:19]
    print(ss)
    print(s[18])
    np.brightness=0.1
    if(s[18]=='0'):   
      np.clear()
      np[0]=(127,0,0)
      np.write()
    elif(s[18]=='1'):   
      np.clear()
      np[1]=(0,127,0)
      np.write()
    elif(s[18]=='2'):       
      np.clear()
      np[2]=(0,0,127)
      np.write()
    else:
      np.clear()
      np.write()
    oled.fill(0)
    oled.text('{0}'.format(ss),2,2)  
    oled.show()  
    time.sleep(0.1)
    bct.close()
  elif msg == b"off":
    np.clear()
    np[2]=(0,0,127)
    print("off")

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










