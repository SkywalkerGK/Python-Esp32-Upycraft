
from machine import Pin
import time
np = NeoPixelLib.NeoPixel(Pin(19),64)
RED=(255,0,0)
def np1(): 
  np.clear()
  np[34]=RED ;np[18]=RED ;np[10]=RED   #11111
  np[42]=RED ;np[26]=RED 
  np.write()
def np2(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #2222222222
  np[27]=RED ;np[26]=RED ;np[19]=RED
  np[25]=RED ;np[33]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()
def np3(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #3333
  np[27]=RED ;np[26]=RED ;np[25]=RED
  np[19]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()
def np4(): 
  np.clear()
  np[17]=RED ;np[9]=RED ;np[25]=RED   #4444
  np[27]=RED ;np[11]=RED ;np[19]=RED
  np[26]=RED ;np[35]=RED ;np[43]=RED 
  np.write()
def np5(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #555
  np[27]=RED ;np[26]=RED ;np[17]=RED
  np[25]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()  
def np6(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #66666
  np[27]=RED ;np[26]=RED ;np[17]=RED ;np[33]=RED
  np[25]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()    
  
  









while True:
  np.brightness=0.01
  np1()
  time.sleep(1)
  np2()
  time.sleep(1)
  np3()
  time.sleep(1)
  np4()
  time.sleep(1)
  np5()
  time.sleep(1)
  np6()
  time.sleep(1)
  
    
