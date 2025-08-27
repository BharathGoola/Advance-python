import time
class A_class:
    def __init__(self,a1=None,a2=None,a3=None):
        print("Constructor overloading using default argument")
a1=A_class(10,20,30)
print()
a1=A_class(10,20)
print()
a1=A_class(10)
print()
time.sleep(2)
print("End of an application")