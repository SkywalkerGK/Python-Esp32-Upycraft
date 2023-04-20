
# Web-Server-static.py ; By Opas Sirikunchittavorn
import network
import time

SSID="OPPO A91"
PASSWORD="0817260364"

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
    <head> <title>Simple web server</title> </head>
    <body> 
        <h1>My First Heading Black</h1>
        <p>My first paragraph.</p>
    </body>
</html>
"""

import socket,time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP
    s.bind(("0.0.0.0",80))#port 80
    s.listen(1)# 1 machune

    while True: # loop for accept request
        conn,addr = s.accept() #get client socket and address
        request = conn.recv(1024)
        request = str(request) 
        print("Content = %s" % str(request))
        if(request.find('/ ')==6):
          response = res_200 + "<b>Hello world</b>"
        elif(request.find('/cakes')==6):
          response = res_200 + "<b>Cake++++</b>"
        elif(request.find('/puddind')==6):
          response = res_200 + "<b>Pudding!!!</b>" 
        else:
          response = res_200 + "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"         
        #write data to client
        conn.send(html)
        conn.send(response)#response
        conn.close()        # close connection
    
finally :
  if(s) :
    s.close()
  sta_if.disconnect()
  sta_if.active(False)


