import time
class A_class:
    def __init__(self,*a1):
        print("Constructor overloading using variable length argument")
a1=A_class()
print()
a1=A_class(10,20)
print()
a1=A_class(10,20,30)
print()
a1=A_class(10,20,30,40)
print()
a1=A_class(10,20,30,40,50)
print()
time.sleep(2)
print("End of an application")