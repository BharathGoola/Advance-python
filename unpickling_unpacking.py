import time
import pickle
class train_class:
    def __init__(self,tno,tname,arr_time,dept_time,date,source,destination):
        self.tno=tno
        self.tname=tname
        self.arr_time=arr_time
        self.dept_time=dept_time
        self.date=date
        self.source=source
        self.destination=destination
    def m1(self):
        print("===Train_Information===")
        print("Tno is:",self.tno)
        print("Tname is:",self.tname)
        print("Arr_time is",self.arr_time)
        print("Dept_time is",self.dept_time)
        print("DAte is:",self.date)
        print("Source is:",self.source)
        print("Destination is:",self.destination)
print()
print("===Unpickling/Unpacking===")
with open("A14.txt","rb") as f:
    obj1=pickle.load(f)
    obj1.m1()
    print(obj1)
    print()
    print("Unpiickling_Process is Done Successfully....")
print()
time.sleep(2)
print("End of an application")