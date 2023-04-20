from machine import Pin, PWM
from micropython import const
import time
DO=const(523)
RE=const(587)
ME=const(659)
FA=const(698)
SO=const(783)
LA=const(880)
TE=const(987)
pwmPiezo=PWM(Pin(25))
pwmPiezo.duty(5)
pwmPiezo.freq(DO)
time.sleep(0.5)
pwmPiezo.duty(0)



