from machine import Pin
import time
button=Pin(0,Pin.IN)
LED = Pin(18,Pin.OUT)



while True:
  if button.value() == 0 :
    LED.value(1)
    print('Button Press')
  else:
    LED.value(0)
    print('Do not Press')
  time.sleep(0.5)  

