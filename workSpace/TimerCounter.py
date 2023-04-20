


from machine import Pin
import time
x=0
counter=0
button=Pin(0,Pin.IN)
button2=Pin(32,Pin.IN)




def inter(e):
  time.sleep_ms(20)
  if button.value()==0:
    global counter
    counter=1-counter
    print(counter)
button.irq(trigger=Pin.IRQ_FALLING,handler=inter)





  
while True:
  if(counter==1):   
    x=x+1
    time.sleep(1)
    print(x)
if(counter==0):
  print(x)
  x=0

