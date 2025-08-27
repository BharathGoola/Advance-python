import time
class A_class:
    def __init__(self):
        print("Constructor_method/constructor_function")
    def __del__(self):
        print("Destructor_method:meant for cleaning activity purpose")
a1=A_class()   #use_full object
print()
del a1         #use_less object
print()
time.sleep(2)
print("End of an application")