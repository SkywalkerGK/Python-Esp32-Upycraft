

from machine import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C
import network
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
SSID="thananat   5G"
PASSWORD="0891550015"
LED0=Pin(18,Pin.OUT)

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if.active(True)
#cfg=('192.168.31.219','255.255.255.0','192.168.31.1','8.8.8.8')
#sta_if.ifconfig(cfg)
print("Connecting to WiFi...")
sta_if.connect(SSID,PASSWORD) 
while sta_if.isconnected()==0  :
    print(".",end="")
    time.sleep(1)

print("My IP :",sta_if.ifconfig()[0])

res_200 = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
html = res_200 + """<!DOCTYPE html>
<html>
<head> <title>ESP8566 LED ON/OFF</title> </head>
<h1>simple Web server for turning ESP8266 LED's on and off with Micropython</h1>
<p>LED0 Status : %s</p>
<form>
<button name="LED" value="ON0" type="submit">LED 0 ON</button>
<button name="LED" value="OFF0" type="submit">LED 0 OFF</button>
</form>
</html>
"""

import socket,time
import urequests , ujson


bct = urequests.get('http://air4thai.pcd.go.th/services/getNewAQI_JSON.php?stationID=32t')
bct_js = bct.json()
us_rate=bct_js['stationID']
us_date=bct_js['LastUpdate']['date']
us_time=bct_js['LastUpdate']['time']
us_pm=bct_js['LastUpdate']['PM25']['value']
us_aqi=bct_js['LastUpdate']['AQI']['aqi']

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP
    s.bind(("0.0.0.0",80))#port 80
    s.listen(1)# 1 machune

    while True: # loop for accept request
        
        conn,addr = s.accept() #get client socket and address
        status0 = '<b>OFF</b>'
        print("Got a connection from %s" % str(addr))
        request = conn.recv(1024)
        request = str(request) 
        if(request.find('/ON')==6):
          print('Turn LED0 ON')
          status0 = '<b>ON</b>'
          LED0.value(1)
          response = html % (status0)
        elif(request.find('/OFF')==6):
          print('Turn LED0 OFF')
          status0 = '<b>OFF</b>'
          LED0.value(0)
          response = html % (status0)                
        elif(request.find('/ ')==6):
          response = html % (status0)
        else:
          response = res_200 + "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"        
        #write data to client
        
        conn.send(response)#response
        conn.close()        # close connection
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
        oled.show()  
        time.sleep(1)
        bct.close()
