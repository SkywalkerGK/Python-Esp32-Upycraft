




import time
from machine import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C
i2cbus = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)

  
 
while True:
  oled.fill(0)
  oled.text('StationID',2,2)   
  oled.show()  
  time.sleep(1)









