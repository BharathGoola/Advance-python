import time
class A_class:
    def m1(self):
        print("A_class Imp...")
class B_class:
    def m2(self):
        print("B_class Imp...")
class C_class:
    def m3(self):
        print("C_class Imp...")
class D_class:
    def m4(self):
        print("D_class Imp...")
class S1_Class(A_class,B_class,C_class,D_class):
    def m5(self):
        print("S1_Class...")
s1=S1_Class()
s1.m1()
s1.m2()
s1.m3()
s1.m4()
s1.m5()
print()
time.sleep(2)
print("End of an application")



# if methods are same in multiple_inheritance then
import time
class A_class:
    def m1(self):
        print("A_class Imp...")
class B_class:
    def m1(self):
        print("B_class Imp...")
class C_class:
    def m1(self):
        print("C_class Imp...")
class D_class:
    def m1(self):
        print("D_class Imp...")
class S1_Class(A_class,B_class,C_class,D_class):
    def m1(self):
        print("S1_class...")
s1=S1_Class()
s1.m1()
print()
time.sleep(2)
print("End of an application")



import time
class A_class:
    def m1(self):
        print("A_class Imp...")
class B_class:
    def m1(self):
        print("B_class Imp...")
class C_class:
    def m1(self):
        print("C_class Imp...")
class D_class:
    def m1(self):
        print("D_class Imp...")
class S1_Class(D_class,C_class,B_class,A_class):pass
s1=S1_Class()
s1.m1()
print()
time.sleep(2)
print("End of an application")