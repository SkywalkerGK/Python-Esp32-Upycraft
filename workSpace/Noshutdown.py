import NeoPixelLib2
mp = NeoPixelLib2.NeoPixel(Pin(23),64)

def dot():
  np.brightness=0.01
  np[16]=BLACK;np[32]=BLACK
  np.write()
  time.sleep(0.1) 
  np[16]=BLUE;np[32]=BLUE
  np.write()
  time.sleep(0.1)   

def np0(): 
  mp.clear()
  mp[11]=RED ;mp[9]=RED ;mp[10]=RED   #000
  mp[27]=RED ;mp[17]=RED ;mp[33]=RED ;mp[19]=RED
  mp[25]=RED ;mp[35]=RED ;mp[43]=RED ;mp[42]=RED ;mp[41]=RED
  mp.write() 
def np1(): 
  mp.clear()
  mp[34]=RED ;mp[18]=RED ;mp[10]=RED   #11111
  mp[42]=RED ;mp[26]=RED 
  mp.write()
def np2(): 
  mp.clear()
  mp[11]=RED ;mp[9]=RED ;mp[10]=RED   #2222222222
  mp[27]=RED ;mp[26]=RED ;mp[19]=RED
  mp[25]=RED ;mp[33]=RED ;mp[43]=RED ;mp[42]=RED ;mp[41]=RED
  mp.write()
def np3(): 
  mp.clear()
  mp[11]=RED ;mp[9]=RED ;mp[10]=RED   #3333
  mp[27]=RED ;mp[26]=RED ;mp[25]=RED
  mp[19]=RED ;mp[35]=RED ;mp[43]=RED ;mp[42]=RED ;mp[41]=RED
  mp.write()
def np4(): 
  mp.clear()
  mp[17]=RED ;mp[9]=RED ;mp[25]=RED   #4444
  mp[27]=RED ;mp[11]=RED ;mp[19]=RED
  mp[26]=RED ;mp[35]=RED ;mp[43]=RED 
  mp.write()
def np5(): 
  mp.clear()
  mp[11]=RED ;mp[9]=RED ;mp[10]=RED   #555
  mp[27]=RED ;mp[26]=RED ;mp[17]=RED
  mp[25]=RED ;mp[35]=RED ;mp[43]=RED ;mp[42]=RED ;mp[41]=RED

  mp.write()  
def np6(): 
  mp.clear()
  mp[11]=RED ;mp[9]=RED ;mp[10]=RED   #66666
  mp[27]=RED ;mp[26]=RED ;mp[17]=RED ;mp[33]=RED
  mp[25]=RED ;mp[35]=RED ;mp[43]=RED ;mp[42]=RED ;mp[41]=RED
  mp.write() 
def mp0():   
  mp[14]=RED ;mp[15]=RED ;mp[13]=RED   #0000
  mp[21]=RED ;mp[23]=RED 
  mp[29]=RED ;mp[31]=RED ;mp[37]=RED 
  mp[39]=RED
  mp[45]=RED ;mp[46]=RED ;mp[47]=RED  
  mp.write()
def mp1():  
  mp[14]=RED ;mp[22]=RED ;mp[30]=RED   #111111
  mp[46]=RED ;mp[38]=RED       
  mp.write() 
def mp2():   
  mp[15]=RED ;mp[13]=RED ;mp[14]=RED   #2222222222
  mp[31]=RED ;mp[30]=RED ;mp[23]=RED
  mp[29]=RED ;mp[37]=RED ;mp[47]=RED ;mp[46]=RED ;mp[45]=RED
  mp.write()   
def mp3():     
  mp[15]=RED ;nm[13]=RED ;nm[14]=RED   #33333
  mp[29]=RED ;nm[31]=RED ;nm[23]=RED
  mp[30]=RED ;nm[39]=RED ;nm[45]=RED ;nm[47]=RED ;nm[46]=RED
  mp.write()  
def mp4():     
  mp[21]=RED ;mp[13]=RED ;mp[29]=RED   #33333
  mp[31]=RED ;mp[30]=RED ;mp[15]=RED
  mp[23]=RED ;mp[39]=RED ;mp[47]=RED 
  mp.write()  
def mp5():     
  mp[15]=RED ;mp[13]=RED ;mp[14]=RED   #55555
  mp[31]=RED ;mp[30]=RED ;mp[29]=RED
  mp[21]=RED ;mp[39]=RED ;mp[45]=RED
  mp[46]=RED ;mp[47]=RED  
  mp.write()    

def mp6():    
  mp[15]=RED ;mp[13]=RED ;mp[14]=RED   #6666
  mp[31]=RED ;mp[30]=RED ;mp[29]=RED
  mp[21]=RED ;mp[37]=RED ;mp[45]=RED
  mp[46]=RED ;mp[47]=RED ;mp[39]=RED
  mp.write() 
def mp7():       
  mp[13]=RED ;mp[15]=RED ;mp[14]=RED #7777777777777
  mp[23]=RED
  mp[31]=RED ;mp[39]=RED ;mp[47]=RED 
  mp.write() 
def mp8():       
  mp[15]=RED ;mp[13]=RED ;mp[14]=RED   #88888
  mp[31]=RED ;mp[30]=RED ;mp[29]=RED
  mp[21]=RED ;mp[37]=RED ;mp[45]=RED
  mp[46]=RED ;mp[47]=RED ;mp[39]=RED  
  mp[23]=RED
  mp.write() 
def mp9():       
  mp[15]=RED ;mp[13]=RED ;mp[14]=RED   #99999
  mp[31]=RED ;mp[30]=RED ;mp[29]=RED
  mp[21]=RED ;mp[45]=RED
  mp[46]=RED ;mp[47]=RED ;mp[39]=RED  
  mp[23]=RED
  mp.write()  

while True:
  np.brightness=0.01
  dot()
  if(s[14]=='0'):
    np0()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()  
  elif(s[14]=='1'):   
    np1()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()
  elif(s[14]=='2'):   
    np2()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 

      mp9()  
  elif(s[14]=='3'):   
    np3()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9() 
  elif(s[14]=='4'):   
    np4()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()       
  elif(s[14]=='5'):   
    np5()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 

      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()
  elif(s[14]=='6'):   
    np6()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9() 
  elif(s[14]=='7'):   
    np7()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9() 
  elif(s[14]=='8'):   
    np8()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 

      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()
  elif(s[14]=='9'):   
    np9()
    if(s[15]=='0'):
      mp0()
    elif(s[15]=='1'):
      mp1()
    elif(s[15]=='2'): 
      mp2()   
    elif(s[15]=='3'): 
      mp3()
    elif(s[15]=='4'): 
      mp4() 
    elif(s[15]=='5'): 
      mp5()    
    elif(s[15]=='6'): 
      mp6()      
    elif(s[15]=='7'):
      mp7()    
    elif(s[15]=='8'): 
      mp8()    
    elif(s[15]=='9'): 
      mp9()       
  else:
    np.clear()
    np.write()  

  





