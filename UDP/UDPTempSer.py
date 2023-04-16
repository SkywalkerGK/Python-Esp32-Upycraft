
sta_if=None
ap_if=None
def connect_wifi(ssid,pwd):
    import network
    import time
    counter = 0
    global sta_if,ap_if
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    cfg = ('192.168.31.219','255.255.255.0','192.168.31.1','8.8.8.8')
    sta_if.ifconfig(cfg)
    sta_if.connect(ssid,pwd)
    while not sta_if.isconnected() and counter<10 :
        counter += 1
        print(".",end="")
        time.sleep(1)
    if sta_if.isconnected():
        print("Connected my IP :",sta_if.ifconfig()[0])
        return True
    else :
        print("Connection fail !")
        return False
import socket
import time
from machine import Pin
import dht
d=dht.DHT22(Pin(19))
port = 4210
s=None
try:
    if(connect_wifi("TelecomPractice","thereisnospoon")) :
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        ip=sta_if.ifconfig()[0]
        s.bind((ip,port))
        print('waiting..')
        while True:
         temp=d.temperature()
         hum=d.humidity()
         time.sleep(2)
         data,addr=s.recvfrom(1024)
         print('received:',data,'from',addr)
         if(data == b'hum=?'):
           d.measure()
           msg='hum='+str(d.humidity())+'%'
           s.sendto(msg.encode(),addr)
           print('1')
         elif(data == b'temp=?'):
           d.measure()
           msg='temp='+str(d.temperature())+'C'
           s.sendto(msg.encode(),addr)
         else :
           s.sendto(msg.encode(),addr)
finally:
    if (s):
      s.close()
    sta_if.disconnect()
    sta_if.active(False)












