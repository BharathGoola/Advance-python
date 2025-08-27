import time
class car_class:
    print("Car Implementation....")
    class Engine_class:
        print("Engine Implementation...")
        def m1(self):
            print("This is First_Service of car")
c1=car_class().Engine_class().m1()
print()
time.sleep(2)
print("End of an application")

import time
class Language_class:
    def __init__(self):
        self.name="Python Programming Language"
        self.dor=self.DOR()
    def m1(self):
        print("Name of the class is:",self.name)

    class DOR:
        def __init__(self):
            self.day=10
            self.month=7
            self.year=2025
        def m2(self):
            print("Date of release is:{}/{}/{}".format(self.day,self.month,self.year))
l1=Language_class()
l1.m1()
print()
time.sleep(2)
print("End of an application")