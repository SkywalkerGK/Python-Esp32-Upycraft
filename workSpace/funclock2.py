  
from machine import Pin
import time
np = NeoPixelLib.NeoPixel(Pin(19),64)
RED=(255,0,0)
def mp0(): 
    np.clear()  
    np[14]=RED ;np[15]=RED ;np[13]=RED   #0000
    np[21]=RED ;np[23]=RED 
    np[29]=RED ;np[31]=RED ;np[37]=RED 
    np[39]=RED
    np[45]=RED ;np[46]=RED ;np[47]=RED  
    np.write()
def mp1(): 
    np.clear() 
    np[14]=RED ;np[22]=RED ;np[30]=RED   #111111
    np[46]=RED ;np[38]=RED       
    np.write() 
def mp2(): 
    np.clear()    
    np[15]=RED ;np[13]=RED ;np[14]=RED   #2222222222
    np[31]=RED ;np[30]=RED ;np[23]=RED
    np[29]=RED ;np[37]=RED ;np[47]=RED ;np[46]=RED ;np[45]=RED
    np.write()   
def mp3(): 
    np.clear()    
    np[15]=RED ;np[13]=RED ;np[14]=RED   #33333
    np[29]=RED ;np[31]=RED ;np[23]=RED
    np[30]=RED ;np[39]=RED ;np[45]=RED ;np[47]=RED ;np[46]=RED
    np.write()  
def mp4(): 
    np.clear()    
    np[21]=RED ;np[13]=RED ;np[29]=RED   #33333
    np[31]=RED ;np[30]=RED ;np[15]=RED
    np[23]=RED ;np[39]=RED ;np[47]=RED 
    np.write()  
def mp5(): 
    np.clear()    
    np[15]=RED ;np[13]=RED ;np[14]=RED   #55555
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[39]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED  
    np.write()    
def mp6(): 
    np.clear()    
    np[15]=RED ;np[13]=RED ;np[14]=RED   #6666
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[37]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED
    np.write() 
def mp7(): 
    np.clear()      
    np[13]=RED ;np[15]=RED ;np[14]=RED #7777777777777
    np[23]=RED
    np[31]=RED ;np[39]=RED ;np[47]=RED 
    np.write() 
def mp8(): 
    np.clear()      
    np[15]=RED ;np[13]=RED ;np[14]=RED   #88888
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[37]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED  
    np[23]=RED
    np.write() 
def mp9(): 
    np.clear()      
    np[15]=RED ;np[13]=RED ;np[14]=RED   #99999
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED  
    np[23]=RED
    np.write()     
while True:
  np.brightness=0.01
  mp1()
  time.sleep(1)
  mp2()
  time.sleep(1)
  mp3()
  time.sleep(1)
  mp4()
  time.sleep(1)
  mp5()
  time.sleep(1)
  mp6()
  time.sleep(1) 
  mp7()
  time.sleep(1)
  mp8()
  time.sleep(1)
  mp9()
  time.sleep(1)
  mp0()
  time.sleep(1)   
    
    
    
    
    
    

