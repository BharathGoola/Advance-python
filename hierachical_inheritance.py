import time
class Father_class:
    def m1(self):
        print("Father_class Imp...")
class Son_1(Father_class):
    def m2(self):
        print("Son1_class Imp...")
class Son_2(Father_class):
    def m3(self):
        print("Son2_class Imp...")
f1=Father_class()
f1.m1()
print()
s1=Son_1()
s1.m1()
s1.m2()
print()
s2=Son_2()
s2.m1()
s2.m3()
print()
time.sleep(2)
print("End of an application")