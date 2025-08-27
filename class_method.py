import time
class A_class:
    @classmethod
    def m2(cls):
        print("This is class_method:")
a1=A_class()
a1.m2()    #object refernce variable
A_class.m2()    #class method
print() 
time.sleep(2)
print("End of an application")