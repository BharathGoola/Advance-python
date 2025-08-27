import time
from threading import*
class My_Thread_1(Thread):
    def m1(self):
        for x1  in range(10):
            time.sleep(1)
            print("Generative AI Application Development")
t1=My_Thread_1()
t1.start()
for y1 in range(10):
    time.sleep(1)
    print("Python|Flask|Open_AI Tool|Gemeni2.0 Version")
print()
time.sleep(2)
print("End of an application")


import time
from threading import*
class My_Thread_1(Thread):
    def run(self):
        for x1 in range(10):
            time.sleep(1)
            print("Generative AI Application Development")
t1=My_Thread_1()
t1.start()
for y1 in range(10):
    time.sleep(1)
    print("Python|Flask|Open_AI Tool|Gemeni2.0 Version")
print()
time.sleep(2)
print("End of an application")