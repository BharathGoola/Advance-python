import time 
class A_class:
    def __init__(self):
        print('0-number of argument')
    def __init__(self,a1):
        print('1-number of argument')
    def __init__(self,a1,a2):
        print('2-number of argument')
    def __init__(self,a1,a2,a3):
        print('3-number of argument')
a1=A_class(10,20,30)
print()
time.sleep(2)
print("End of an application")