

from machine import Pin
import time
button=Pin(0,Pin.IN)
LED = Pin(18,Pin.OUT)
counter = 0

def inter(e):
  time.sleep_ms(20)
  if button.value()==0:
    global counter
    counter+=1
    print(counter)
button.irq(trigger=Pin.IRQ_FALLING,handler=inter)

while True:
  LED.value(1)
  time.sleep(0.5)
  LED.value(0)
  time.sleep(0.5)



