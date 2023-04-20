from machine import Pin
import time

blue = Pin(23,Pin.OUT)
green = Pin(19,Pin.OUT)
red = Pin(5,Pin.OUT)

def led_on(obj_led,delay):
  obj_led.value(1)
  time.sleep(delay)
  obj_led.value(0)

while True:
  led_on(blue,2)
  led_on(green,2)
  led_on(red,2)



