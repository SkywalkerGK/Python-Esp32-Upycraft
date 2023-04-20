from machine import Pin,PWM
import time

pwm19=PWM(Pin(19))
pwm19.freq(100)
pwm23=PWM(Pin(23))
pwm23.freq(100)

while True:
  for i in range (0,1024,11):
    pwm19.duty(i)
    pwm23.duty(1023-i)
    print(i)
    time.sleep(0.05)
    



