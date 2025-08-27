import time
class Product_class_1:
    def __init__(self,pid,pname):   #constructor
        self.pid=pid
        self.pname=pname
    def m1(self):         #method 
        print("pis is:",self.pid)
        print("pname is:",self.pname)
class Product_class_2(Product_class_1):
    def __init__(self,pid,pname,price,company,m_date,exp_date):
        super().__init__(pid,pname)
        self.price=price
        self.company=company
        self.m_date=m_date
        self.exp_date=exp_date
    def m2(self):
        super().m1()
        print("Price is:",self.price)
        print("Company is:",self.company)
        print("M_date is:",self.m_date)
        print("Exp_date is:",self.exp_date)
p1=Product_class_2(1001,"Mobile_1",68000,"Samsung","24/7/2025","24/8/2025")
p1.m2()
print()
time.sleep(2)
print("End of an application")