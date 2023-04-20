def dot():
  np.brightness=0.01
  np[80]=BLACK;np[96]=BLACK
  np.write()
  time.sleep(0.1) 
  np[80]=BLUE;np[96]=BLUE
  np.write()
  time.sleep(0.1) 


def hd0(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #0000
  np[27]=RED ;np[17]=RED ;np[33]=RED ;np[19]=RED
  np[25]=RED ;np[35]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write() 
def hd1(): 
  np.clear()
  np[34]=RED ;np[18]=RED ;np[10]=RED   #11111
  np[42]=RED ;np[26]=RED 
  np.write()
def hd2(): 
  np.clear()
  np[11]=RED ;np[9]=RED ;np[10]=RED   #2222222222
  np[27]=RED ;np[26]=RED ;np[19]=RED
  np[25]=RED ;np[33]=RED ;np[43]=RED ;np[42]=RED ;np[41]=RED
  np.write()

def hr0():   
    np[14]=RED ;np[15]=RED ;np[13]=RED   #0000
    np[21]=RED ;np[23]=RED 
    np[29]=RED ;np[31]=RED ;np[37]=RED 
    np[39]=RED
    np[45]=RED ;np[46]=RED ;np[47]=RED  
    np.write()
def hr1():  
    np[14]=RED ;np[22]=RED ;np[30]=RED   #111111
    np[46]=RED ;np[38]=RED       
    np.write() 
def hr2():   
    np[15]=RED ;np[13]=RED ;np[14]=RED   #2222222222
    np[31]=RED ;np[30]=RED ;np[23]=RED
    np[29]=RED ;np[37]=RED ;np[47]=RED ;np[46]=RED ;np[45]=RED
    np.write()   

def hr3():     
    np[15]=RED ;np[13]=RED ;np[14]=RED   #33333
    np[29]=RED ;np[31]=RED ;np[23]=RED
    np[30]=RED ;np[39]=RED ;np[45]=RED ;np[47]=RED ;np[46]=RED
    np.write()  
def hr4():     
    np[21]=RED ;np[13]=RED ;np[29]=RED   #33333
    np[31]=RED ;np[30]=RED ;np[15]=RED
    np[23]=RED ;np[39]=RED ;np[47]=RED 
    np.write()  
def hr5():     
    np[15]=RED ;np[13]=RED ;np[14]=RED   #55555
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[39]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED  
    np.write()    
def hr6():    
    np[15]=RED ;np[13]=RED ;np[14]=RED   #6666
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[37]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED
    np.write() 
def hr7():       
    np[13]=RED ;np[15]=RED ;np[14]=RED #7777777777777
    np[23]=RED
    np[31]=RED ;np[39]=RED ;np[47]=RED 
    np.write() 
def hr8():       
    np[15]=RED ;np[13]=RED ;np[14]=RED   #88888
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[37]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED  
    np[23]=RED
    np.write() 
def hr9():       
    np[15]=RED ;np[13]=RED ;np[14]=RED   #99999
    np[31]=RED ;np[30]=RED ;np[29]=RED
    np[21]=RED ;np[45]=RED
    np[46]=RED ;np[47]=RED ;np[39]=RED  
    np[23]=RED
    np.write()      
def np0(): 
  np[73]=RED ;np[74]=RED ;np[75]=RED   #66666
  np[81]=RED ;np[83]=RED ;np[89]=RED ;np[91]=RED
  np[97]=RED ;np[99]=RED ;np[105]=RED ;np[106]=RED ;np[107]=RED
  np.write() 
def np1(): 
  np[74]=RED ;np[82]=RED ;np[90]=RED   #11111
  np[98]=RED ;np[106]=RED 
  np.write()
def np2(): 
  np[73]=RED ;np[74]=RED ;np[75]=RED   #2222222222
  np[83]=RED ;np[89]=RED ;np[90]=RED
  np[91]=RED ;np[97]=RED ;np[105]=RED ;np[106]=RED ;np[107]=RED
  np.write()
def np3(): 
  np[73]=RED ;np[74]=RED ;np[75]=RED   #3333
  np[83]=RED ;np[89]=RED ;np[90]=RED
  np[91]=RED ;np[99]=RED ;np[105]=RED ;np[106]=RED ;np[107]=RED
  np.write()
def np4(): 
  np[73]=RED ;np[75]=RED ;np[81]=RED   #4444
  np[83]=RED ;np[89]=RED ;np[90]=RED
  np[91]=RED ;np[99]=RED ;np[107]=RED 
  np.write()
def np5(): 
  np[73]=RED ;np[74]=RED ;np[75]=RED   #555
  np[81]=RED ;np[89]=RED ;np[90]=RED
  np[91]=RED ;np[99]=RED ;np[105]=RED ;np[106]=RED ;np[107]=RED
  np.write() 

def mp0():  
    np[77]=RED ;np[78]=RED ;np[79]=RED   #0000
    np[85]=RED ;np[87]=RED 
    np[93]=RED ;np[95]=RED ;np[101]=RED 
    np[103]=RED
    np[109]=RED ;np[110]=RED ;np[111]=RED  
    np.write()
def mp1(): 
    np[78]=RED ;np[86]=RED ;np[94]=RED   #111111
    np[102]=RED ;np[110]=RED       
    np.write() 
def mp2():    
    np[77]=RED ;np[78]=RED ;np[79]=RED   #2222222222
    np[87]=RED ;np[93]=RED ;np[94]=RED
    np[95]=RED ;np[101]=RED ;np[109]=RED ;np[110]=RED ;np[111]=RED
    np.write()   
def mp3():     
    np[77]=RED ;np[78]=RED ;np[79]=RED   #33333
    np[87]=RED ;np[93]=RED ;np[94]=RED
    np[95]=RED ;np[103]=RED ;np[109]=RED ;np[110]=RED ;np[111]=RED
    np.write()  
def mp4():    
    np[77]=RED ;np[87]=RED ;np[79]=RED   #33333
    np[85]=RED ;np[93]=RED ;np[94]=RED
    np[95]=RED ;np[103]=RED ;np[111]=RED 
    np.write()  
def mp5():   
    np[77]=RED ;np[78]=RED ;np[79]=RED   #55555
    np[85]=RED ;np[93]=RED ;np[94]=RED
    np[95]=RED ;np[103]=RED ;np[109]=RED
    np[110]=RED ;np[111]=RED  
    np.write()    
def mp6():   
    np[77]=RED ;np[78]=RED ;np[79]=RED   #6666
    np[85]=RED ;np[93]=RED ;np[94]=RED
    np[95]=RED ;np[101]=RED ;np[103]=RED
    np[109]=RED ;np[110]=RED ;np[111]=RED
    np.write() 
def mp7():    
    np[77]=RED ;np[78]=RED ;np[79]=RED #7777777777777
    np[87]=RED
    np[95]=RED ;np[103]=RED ;np[111]=RED 
    np.write() 
def mp8():      
    np[77]=RED ;np[78]=RED ;np[79]=RED   #99999
    np[85]=RED ;np[87]=RED ;np[93]=RED
    np[94]=RED ;np[95]=RED
    np[103]=RED ;np[109]=RED ;np[110]=RED  
    np[111]=RED ;np[101]=RED
    np.write() 
def mp9():     
    np[77]=RED ;np[78]=RED ;np[79]=RED   #99999
    np[85]=RED ;np[87]=RED ;np[93]=RED
    np[94]=RED ;np[95]=RED
    np[103]=RED ;np[109]=RED ;np[110]=RED  
    np[111]=RED
    np.write()   
