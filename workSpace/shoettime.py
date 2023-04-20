import network
WIFI_SSID = "thananat   2.4G"
WIFI_PASS = "0891550015"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID,WIFI_PASS)

while True:
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








