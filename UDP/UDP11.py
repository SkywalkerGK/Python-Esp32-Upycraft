
import socket
import time
from machine import Pin
LED=Pin(18,Pin.OUT)
port=4210
s=None

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

try:
  if(connect_wifi("thananat   2.4G","0891550015")):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip=sta_if.ifconfig()[0]
    s.bind((ip,port))
    s.listen(1)
    print('tcp waiting...')
    
    while True:
      print("accecpting.....")
      conn,addr=s.accept()
      print(addr,"connected")
      
      while True:

        data = conn.recv(1024)
        if(len(data)==0):
          print("close socket")
          conn.close()
          break
        print('Received:',data)
        if(data == b'a=0'):
          LED.value(0)
          conn.send("Turn OFF LED\n")
        elif(data==b'a=1'):
          LED.value(1)
          conn.send("Turn ON LED\n")
        else:
          conn.send("Unknow command\n")
       
except NameError as err:
  print("NameError: {0}" .format(err))
    
except:
  if(s):
    s.close()
  sta_if.disconnect()
  sta_if.active(False)


