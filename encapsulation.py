import time
class Product_class:
    def setpid(self,pid):
        self.pid=pid
    def getpid(self):
        return self.pid
    def setpname(self,pname):
        self.pname=pname
    def getpname(self):
        return self.pname
    def setprice(self,price):
        self.price=price
    def getprice(self):
        return self.price
    def setcompany(self,company):
        self.company=company
    def getcompany(self):
        return self.company
p1=Product_class()
p1.setpid(1001)
p1.setpname("mobile_1")
p1.setprice(98000)
p1.setcompany("Oneplus")
print("Product_Information")
print("Pid is:",p1.getpid())
print("Pname is:",p1.getpname())
print("Price is:",p1.getprice())
print("Company is:",p1.getcompany())
print()
time.sleep(2)
print("End of an application")