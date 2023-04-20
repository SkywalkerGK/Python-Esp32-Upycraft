






from machine import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C
from umqtt.simple import MQTTClient
import network
import time
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
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(19),64)
button=Pin(32,Pin.IN)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
WHITE=(255,255,255)
counter = 0
n=0
def inter(e):
  time.sleep_ms(20)
  if button.value()==0:
    global counter
    counter+=1
    print(counter)
button.irq(trigger=Pin.IRQ_FALLING,handler=inter)
import LibHR2



import urequests , ujson

while True:
  bct = urequests.get('http://worldtimeapi.org/api/timezone/Asia/Bangkok')
  bct_js = bct.json()
  us_rate=bct_js['datetime']
  s=str(us_rate)  
  ss=s[11:19]
  print(ss)
  np.brightness=0.01
  x=s[15]
  y=s[15]
  if(s[11]=='0'):
    hd0()
    if(s[12]=='0'):
      hr0()
    elif(s[12]=='1'):
      hr1()
    elif(s[12]=='2'): 
      hr2()   
    elif(s[12]=='3'): 
      hr3()
    elif(s[12]=='4'): 
      hr4() 
    elif(s[12]=='5'): 

      hr5()    
    elif(s[12]=='6'): 
      hr6()      
    elif(s[12]=='7'):
      hr7()    
    elif(s[12]=='8'): 
      hr8()    
    elif(s[12]=='9'): 
      hr9()  
  elif(s[11]=='1'):   
    hd1()
    if(s[12]=='0'):
      hr0()
    elif(s[12]=='1'):
      hr1()
    elif(s[12]=='2'): 
      hr2()   
    elif(s[12]=='3'): 
      hr3()
    elif(s[12]=='4'): 
      hr4() 
    elif(s[12]=='5'): 
      hr5()    
    elif(s[12]=='6'): 
      hr6()      
    elif(s[12]=='7'):
      hr7()    
    elif(s[12]=='8'): 
      hr8()    
    elif(s[12]=='9'): 
      hr9()
  elif(s[11]=='2'):   
    hd2()
    if(s[12]=='0'):
      hr0()
    elif(s[12]=='1'):
      hr1()
    elif(s[12]=='2'): 
      hr2()   
    elif(s[12]=='3'): 
      hr3()
  else:
    np.clear()
    np.write()
  while(x==y):
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

    bct = urequests.get('http://worldtimeapi.org/api/timezone/Asia/Bangkok')
    bct_js = bct.json()
    us_rate=bct_js['datetime']
    s=str(us_rate)
    ss=s[11:19]
    y=s[15]
    oled.fill(0)
    print(ss)
    oled.text('{0}'.format(ss),2,2)  
    oled.show()
    
    if(counter==1):
      RED=GREEN
      if(n==0):
        x=555
        n=1
    if(counter==2):
      RED=BLUE
      if(n==1):
        x=555
        n=2
    if(counter==3):
      RED=YELLOW
      if(n==2):
        x=555
        n=3
    if(counter==4):
      RED=CYAN
      if(n==3):
        x=555
        n=4  
    if(counter==5):
      RED=MAGENTA
      if(n==4):
        x=555
        n=5
    if(counter==6):
      RED=WHITE
      if(n==5):
        x=555
        n=6        
    if(counter>6):
      RED=(255,0,0)
      counter=0
      if(n==6):
        x=555
        n=0          
   

   
    time.sleep(0.1)
    bct.close() 
    
           
  oled.fill(0)
  oled.text('{0}'.format(ss),2,2)  
  oled.show()  
  time.sleep(0.)
  bct.close()












