

# Web-Server-static.py ; By Opas Sirikunchittavorn
import network
import time
from machine import Pin
LED0=Pin(18,Pin.OUT)

import dht
d=dht.DHT22(Pin(19))

SSID="thananat   5G"
PASSWORD="0891550015"

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
    
finally :
  if(s) :
    s.close()
  sta_if.disconnect()
  sta_if.active(False)



