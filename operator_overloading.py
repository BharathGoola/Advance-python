import time
class product_class:
    def __init__(self,items):
        self.items=items
    def __str__(self):
        return str(self.items)
    def __add__(self,other):
        obj1=self.items,other.items
        p1=product_class(obj1)
        return p1
p1=product_class(30)
print("Number items in p1 is:",p1)
print()
p2=product_class(5)
print("Number items in p2:",p2)
print()
p3=product_class(15)
print("Number items in p3:",p3)
print()
p4=product_class(23)
print("Number items in p4",p4)
print()
p5=product_class(27)
print("Number items in p5:",p5)
print()
print("The Result is:",p1+p2+p3+p4+p5)
print()
time.sleep(2)
print("End of an application")


import time
class product_class:
    def __init__(self,items):
        self.items=items
    def __str__(self):
        return str(self.items)
    def __imul__(self,other):
        return self.items*other.items
p1=product_class(30)
print("Number of items in p1 is:",p1)
print()
p2=product_class(5)
print("Number of items in p2 is:",p2)
print()
p1*=p2
print("The result is:",p1)
print()
time.sleep(2)
print("End of an application")

