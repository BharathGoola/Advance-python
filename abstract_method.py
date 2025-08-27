import time
from abc import*
class A_class:
    @abstractmethod
    def m1(self):
        pass
a1=A_class()
a1.m1()
print()
time.sleep(2)
print("End of an application")
