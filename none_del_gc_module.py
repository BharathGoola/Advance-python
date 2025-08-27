import time
class A_class:
    def __init__(self):
        print("Constructor_method/Constructor_Function")
    def __del__(self):
        print("Destructor_method:meant for cleaning activity purpose")
print("===Using_None===")
a1=A_class()
a2=a1
a3=a2
print()
a1=None
print("set a1=none")
time.sleep(2)
a2=None
print("set a2=none")
time.sleep(2)
a3=None
print("Set a3=none")
time.sleep(2)
print("===Using_del===")
b1=A_class()
b2=b1
b3=b2
print()
del b1
print("deleted b1")
time.sleep(2)
del b2
print("deleted b2")
time.sleep(2)
del b3
print("deleted b3")
print()
time.sleep(2)
print("End of an application")