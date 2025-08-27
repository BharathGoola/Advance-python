import time
class A_class:
    def m1(self,*x1):
        s1=0
        for a1 in x1:
            s1=s1+a1
        print("Sum of arguments:",s1)
a1=A_class()
a1.m1()
a1.m1(10)
a1.m1(10,20)
a1.m1(10,20,30)
a1.m1(10,20,30,40)
a1.m1(10,20,30,40,50)
print()
time.sleep(2)
print("End of an application")

import time 
class A_class:
    def m1(self,*X1):
        for a1 in X1:
            print(a1)      
a1=A_class()
a1.m1(1001,"Mobile_1",23000.0,"Samsung")
print()
a1.m1(1002,"Mobile_2",25000.0,"Samsung")
print()
time.sleep(2)
print("End of an application")
