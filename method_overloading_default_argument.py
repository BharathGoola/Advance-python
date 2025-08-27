import time
class A_class:
    def m1(self,obj1=None,obj2=None,obj3=None):
        if(obj1!=None and obj2!=None and obj3!=None):
            print("Sum of three numbers of arguments:",obj1+obj2+obj3)        
        elif(obj1!=None and obj2!=None):
            print("Sum of two number of argument:",obj1+obj2)
        else:
            print("only two or three number of arguments is allowed")
a1=A_class()
a1.m1(10,20,30)
print()
a1.m1(10,20)
print()
a1.m1(10)
print()
time.sleep(2)
print("End of an application")
        