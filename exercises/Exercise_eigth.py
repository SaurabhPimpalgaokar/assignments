from time import sleep
import threading
import sys

class MultiThreading(threading.Thread):
     flag = True
     def __init__(self,sleeptime,name):
        super().__init__()
        self.sleeptime = sleeptime
        self.name = name
        

     def run (self):
        b=0
        while True:
            if MultiThreading.flag == False :
                break
            else:
                print(self.name," ", b)
                b=b+1
                sleep(self.sleeptime)
            
                
           
\
t1 = MultiThreading(1,"Thread_1")
t2 = MultiThreading(1.5,"Thread_2")
t3 = MultiThreading(2,"Thread_3")

a=int( input("Enter number :"))
if ( a != 0):
    t1.daemon = True
    t2.daemon = True
    t3.daemon = True
    t1.start()
    t2.start()
    t3.start()
else:
    MultiThreading.flag = False
while a!= 0 :
    a=int( input("Enter number :") )
    if(a == 0):
       MultiThreading.flag=False
    sleep(10)





        

      




