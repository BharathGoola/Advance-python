import time
class A_class:
    def m1(self):
        print("A_class Imp...")
class B_class(A_class):
    def m2(self):
        print("B_class Imp...")
class C_class(B_class):
    def m3(self):
        print("C_class Imp...")
class D_class(C_class):
    def m4(self):
        print("D_class Imp...")
class E_class(D_class):
    def m5(self):
        print("E_class Imp...")
a1=A_class()
a1.m1()
print()
b1=B_class()
b1.m1()
b1.m2()
print()
c1=C_class()
c1.m1()
c1.m2()
c1.m3()
print()
d1=D_class()
d1.m1()
d1.m2()
d1.m3()
d1.m4()
print()
e1=E_class()
e1.m1()
e1.m2()
e1.m3()
e1.m4()
e1.m5()
print()
time.sleep(2)
print("End of an application")