import time
class A_class:
    @staticmethod
    def m3():
        print("This is static method:")
a1=A_class()
print()
a1.m3()
A_class.m3()
print()
time.sleep(2)
print("End of an application")