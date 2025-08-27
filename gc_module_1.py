import time
class A_class:
    def __init__(self):
        print("Constructor_method/Constructor__function")
    def __del__(self):
        print("Destructor_method:meant for cleaning activity purpose")
a1=A_class()
a2=a1
a3=a2
a4=a3
a5=a4
a6=a5
del a1
print()
time.sleep(2)
print("a1 refernce gone object is there")
print()
del a2
time.sleep(2)
print("a2 refernce gone object is there")
print()
del a3
time.sleep(2)
print("a3 refernce gone object is there")
print()
del a4
time.sleep(2)
print("a4 refernce gone object is there")
print()
del a5
time.sleep(2)
print("a5 refernce gone object is there")
print()
del a6
print()
time.sleep(2)
print("End of an application")







import time
class A_class:
    def __init__(self):
        print("Constructor_method/Constructor__function")
    def __del__(self):
        print("Destructor_method:meant for cleaning activity purpose")
a1=A_class()
a1=None
a2=a1
a3=a2
a4=a3
a5=a4
a6=a5
del a1
print()
time.sleep(2)
print("a1 refernce gone object is there")
print()
del a2
time.sleep(2)
print("a2 refernce gone object is there")
print()
del a3
time.sleep(2)
print("a3 refernce gone object is there")
print()
del a4
time.sleep(2)
print("a4 refernce gone object is there")
print()
del a5
time.sleep(2)
print("a5 refernce gone object is there")
print()
del a6
print()
time.sleep(2)
print("End of an application")  