import time
class A_class:
    def __init__(self):
        print("COnsructor_method/Constructor_Function")
    def __del__(self):
        print("Destructor_method:meant for cleaning activity purpose")
a1=[A_class(),A_class(),A_class(),A_class]
a1=None
print()
time.sleep(2)
print("End of an application")


import time
class A_class:
    def __init__(self):
        print("COnsructor_method/Constructor_Function")
    def __del__(self):
        print("Destructor_method:meant for cleaning activity purpose")
a1=[A_class(),A_class(),A_class(),A_class]
del a1
print()
time.sleep(2)
print("End of an application")