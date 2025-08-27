import time
class Employee_class:
    Company_Name="TATA CONSULTANCY SERVICES"
    def __init__(self,Eid,Ename,Esal,Email):
        self.Eid=Eid
        self.Ename=Ename
        self.Esal=Esal
        self.Email=Email
    def m1(self):
        print("==Employee_Details==")
        print("Eid is:",self.Eid)
        print("Ename is:",self.Ename)
        print("Esal is:",self.Esal)
        print("Email is:",self.Email)    
e1=Employee_class(1001,"Bharath_1",35000,"goolabharath08@gmail.com")
e1.m1()
print()
print("Company is:",Employee_class.Company_Name)
print()
time.sleep(2)
print("End of application")