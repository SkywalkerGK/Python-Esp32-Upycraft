

from machine import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
def connect_wifi(ssid,pwd):
  import network
  import time
  
  counter = 0  
  global sta_if,ap_if
  sta_if = network.WLAN(network.STA_IF)
  
  sta_if.active(True)
  #cfg=('192.168.31.219','255.255.255.0','192.168.31.1','8.8.8.8')
 #sta_if.ifconfig(cfg)
  
  sta_if.connect(ssid,pwd)
  while not sta_if.isconnected() and counter < 10 :
    counter += 1
    print(".",end="")
    time.sleep(1)
  if sta_if.isconnected():
    print("Connected my IP :",sta_if.ifconfig()[0])
    return True

  else:
    print("Connection fail !")
    return False
connect_wifi("thananat   2.4G","0891550015")
import urequests , ujson


bct = urequests.get('http://air4thai.pcd.go.th/services/getNewAQI_JSON.php?stationID=32t')
bct_js = bct.json()
us_rate=bct_js['stationID']
us_date=bct_js['LastUpdate']['date']
us_time=bct_js['LastUpdate']['time']
us_pm=bct_js['LastUpdate']['PM25']['value']
us_aqi=bct_js['LastUpdate']['AQI']['aqi']

while True:
  print('stationTD :',us_rate)
  print('Day',us_date)
  print('Time:',us_time)
  print('PM:',us_pm)
  print('AQI:',us_aqi)
  oled.fill(0)
  oled.text('StationID:{0}'.format(us_rate),2,2)
  oled.text('Date:{0}'.format(us_date),2,12)
  oled.text('Time:{0}'.format(us_time),2,22)
  oled.text('PM:{0}'.format(us_pm),2,32)
  oled.text('AQI:{0}'.format(us_date),2,42)
  if int(us_aqi)<=25:
    oled.text('Excellent',2,52)
    print('Excellent')
  elif 26<=int(us_aqi)<=50:
    oled.text('Satisfactory',2,52)
    print('Satisfactory')

  elif 51<=int(us_aqi)<=100:
    oled.text('Moderate',2,52)
    print('Moderate')
  elif 101<=int(us_aqi)<=200:
    oled.text('Unhealthy',2,52)
    print('Unhealthy')   
  elif int(us_aqi)>200:
    oled.text('Very Unhealthy',2,52)
    print('Very Unhealthy')
    
    
  oled.show()  
  time.sleep(1)
  bct.close()





