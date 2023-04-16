
import socket


import time


from machine import Pin,ADC





adc1 = ADC(Pin(34))


adc1.atten(ADC.ATTN_11DB)


adc2 = ADC(Pin(39))


adc2.atten(ADC.ATTN_11DB)





port = 4210


s = None


sta_if = None


ap_if = None





def connect_wifi(ssid,pwd):


  import network


  import time


  


  counter = 0


  global sta_if,ap_if


  sta_if = network.WLAN(network.STA_IF)





  sta_if.active(True)


  cfg = ('192.168.31.217','255.255.255.0','192.168.31.1','8.8.8.8')


  sta_if.ifconfig(cfg)


  


  sta_if.connect(ssid,pwd)


  while not sta_if.isconnected() and counter < 10:


    counter += 1


    print('.',end = '')


    time.sleep(1)


  if sta_if.isconnected() :


    print('Connected my IP :',sta_if.ifconfig()[0])


    return True


  else :


    print('Connected Fail !!')


    return False





try :


  if (connect_wifi('TelecomPractice','thereisnospoon')):


    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    ip = sta_if.ifconfig()[0]


    s.bind((ip,port))


    s.listen(1)


    print('tcp waiting...')


    while True:


        print('accepting...')


        conn,addr = s.accept()


        print(addr,'connected')


        


        while True:


            data = conn.recv(1024)


            if(len(data)==0):


              print('close socket')


              conn.close()


              break


            print('Received:',data)


            if(data == b'adc1=?'):


              value1 = adc1.read()


              msg='Volt1='+str(value1)+'V\n'


              conn.send(msg.encode())


            elif(data == b'adc2=?'):


              value2 = adc2.read()


              msg='Volt2='+str(value2)+'V\n'


              conn.send(msg.encode())


            else :


              conn.send('Unknow command\n')


            


except OSError as err:


  print('OSError: {0}'.format(err))





except:


  if(s):


    s.close()


  sta_if.disconnect()


  sta_if.active(False)




