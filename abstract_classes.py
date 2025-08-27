import time
from abc import*
class A_class(ABC):  #only capital ABC is allowed
    pass
a1=A_class()
print()
time.sleep(2)
print("End of an application")




import time
from abc import*
class B_class(ABC):
    @abstractmethod
    def m1(self):
        pass
class C_class(B_class):
    def m1(self):
        print("Parent_Class ABS_method")
c1=C_class()
c1.m1()
print()
time.sleep(2)
print("End of an application")