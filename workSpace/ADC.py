from machine import Pin,ADC
import time
from machine import I2C
from ssd1306 import SSD1306_I2C
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)
while True:
  oled.fill(0)
  adc1=ADC(Pin(36))
  adc1.atten(ADC.ATTN_11DB)
  value=adc1.read()
  volt=value/4095*3.3
  print('KNOB-SVP = %4d = %0.3f V' %(value,volt))
  oled.text('value = {0}' .format(value),2,2)
  oled.text('volt = {0:.2f}' .format(volt),2,10)
  oled.show() 
  time.sleep(0.5)

