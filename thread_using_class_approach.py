import time
from threading import*
class Test_Case1:
    # def m1(self):
    #     time.sleep(1)
    #     print("Generative AI Application Development")
    def m1(self):
        for x1 in range(10):
            time.sleep(1)
            print("Generative AI Application Development")
t1=Test_Case1()
t2=Thread(target=t1.m1)
t2.start()
for y1 in range(10):
    time.sleep(1)
    print("Python|Flask|Open_AI Tool|Gemeni 2.0 Version")
print()
time.sleep(2)
print("End of an application")

