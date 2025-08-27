import time
class A_class:
    def m1(self):
        print("A_class imp....")
class B_class (A_class):    #Child_Class
    def m2(self):
        print("B_class imp...")
a1=A_class()
a1.m1()
print()
b1=B_class()
b1.m1()
b1.m2()
print()
time.sleep(2)
print("End of an application")
