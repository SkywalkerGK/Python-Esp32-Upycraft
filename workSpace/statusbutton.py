from machine import Pin
import time
button=Pin(0,Pin.IN)
LED = Pin(18,Pin.OUT)
past_value=1
cur_value=1
counter=0
LED.value(0)


while True:
  cur_value=button.value()
  if(cur_value==0) and (past_value==1):
    time.sleep_ms(20)
    if button.value() == 0 :
      counter=counter+1
      print(counter)
      LED.value(1-LED.value())
  past_value=cur_value    



