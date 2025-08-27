import  time
class A_CLASS:
    def __init__(self):
        print("Python Developer")
    def m1(self):
        print("Full Stack Python Developer")
    @classmethod
    def m2(cls):
        print("AI Engineer")
    @staticmethod
    def m3():
        print("ML & DL Developer")
class B_CLASS(A_CLASS):
    def s1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
b1=B_CLASS()
b1.s1()
print()
time.sleep(2)
print("End of an application")

import time
class A_class:
    def m1(self):
        print("A_CLASS Implementation....")
class B_class(A_class):
    def m2(self):
        print("B_CLASS Implementation....")
class C_class(B_class):
    def m3(self):
        print("C_CLASS Implementation....")
class D_class(C_class):
    def m4(self):
        print("D_CLASS Implementation....")
class E_class(D_class):
    def m1(self):
        A_class.m1(self)
        super(B_class,self).m1()
e1=E_class()
e1.m1()
print()
time.sleep(2)
print("End of an application")

