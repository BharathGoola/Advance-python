import time
class person_class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
class Employess_class(person_class):
    def __init__(self, name, age,eid,esal,design,company):
        super().__init__(name, age)
        self.eid=eid
        self.esal=esal
        self.design=design
        self.company=company
    def m2(self):
        super().m1()
        print("Eid is:",self.eid)
        print("Esal is:",self.esal)
        print("Design is:",self.design)
        print("Company is:",self.company)
class Student_class(person_class):
    def __init__(self, name, age,sid,subject,marks):
        super().__init__(name,age)
        self.sid=sid
        self.subject=subject
        self.marks=marks
    def m3(self):
        super().m1()
        print("Sid is:",self.sid)
        print("Subject is:",self.subject)
        print("Marks is:",self.marks)
e1=Employess_class("Bharath",17,1001,180000,"Software Developer","Infosys")
e1.m2()
print()
s1=Student_class("Satish",18,2001,"Python/JavaScript/AI(ML & DL),",98)
s1.m3()
print()
time.sleep(2)
print("End of an application")