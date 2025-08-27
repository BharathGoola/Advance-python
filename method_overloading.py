import time
class A_class:
    def m1(self):
        print("o's number of argument")
    def m1(self,x1):
        print("1's number of argument")
    def m1(self,x1,x2):
        print("2's number of argument")
    def m1(self,x1,x2,x3):
        print("3's number of argument")
a1=A_class()
a1.m1(1000,2000,3000)
print()
time.sleep(2)
print("End of an application")