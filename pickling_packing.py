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
print("===Pickling/Packing===")
with open("A14.txt","wb") as f:
    t1=train_class(12345,"Rajadani_Express","11:30 AM","1:00 PM","21/07/2025","Hyderabad","Tirupathi")
    pickle.dump(t1,f)
    print()
    print("Pickling_Process is Done Successfully....")
print()
time.sleep(2)
print("End of an application")