import time
from threading import*
def Test_Case1(obj1):
    for x1 in obj1:
        time.sleep(1)
        print("Square of a number is:",x1*x1)
def Test_Case2(obj1):
    for y1 in obj1:
        time.sleep(1)
        print("Adding_Operations:",y1+1000)
def Test_Case3(obj1):
    for z1 in obj1:
        time.sleep(1)
        print("Multiply_Operations:",z1*15)
def Test_Case4(obj1):
    for a1 in obj1:
        time.sleep(1)
        print("Expo_Value is:",a1**a1)
if(__name__=="__main__"):
    obj1=[1,2,3,4,5,6,7,8,9,10,11,12]
    begin_time=time.time()
    t1=Thread(target=Test_Case1,args=(obj1,))
    t2=Thread(target=Test_Case2,args=(obj1,))
    t3=Thread(target=Test_Case3,args=(obj1,))
    t4=Thread(target=Test_Case4,args=(obj1,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()    #Join function is to calculate the time
    t2.join()
    t3.join()
    t4.join()
    end_time=time.time()
    print("Time with_out multithreading is:",end_time-begin_time)
print()
time.sleep(2)
print("End of an application")