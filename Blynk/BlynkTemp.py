


# TestBlynk1.py
import BlynkLib
import network
import time
from machine import Pin,ADC
adc1=ADC(Pin(34))
adc1.atten(ADC.ATTN_11DB)

WIFI_SSID = "thananat   2.4G"
WIFI_PASS = "0891550015"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect(WIFI_SSID,WIFI_PASS)
while not wifi.isconnected() :
  pass
print(wifi.ifconfig())

BLYNK_AUTH = 'XAJLy8wQFOqSdS6iGVWDXXJda6CLqUjk'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def my_user_task():
  value=adc1.read()
  volt=value/4095*3300
  tempe=(volt-400)/15.93
  print('Temp=%.2f' %tempe)
  blynk.virtual_write(1,"{:0.2f}".format(tempe))
blynk.set_user_task(my_user_task,2000)
blynk.run()



