import time
from abc import*
class A_class(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass
    @abstractmethod
    def m4(self):
        pass
class B_class(A_class):
    def m1(self):
        print("ABC_Method_one...")
    def m2(self):
        print("ABC_Method_Two...")
    def m3(self):
        print("ABC_Method_Three...")
class C_class(B_class):
    def m4(self):
        print("ABS_Method_Four...")
c1=C_class()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
print()
time.sleep(2)
print("End of an application")
