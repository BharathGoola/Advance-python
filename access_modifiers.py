import time
class A_class:
    product_id=1001
    _product_name="mobile_1"
    __product_price=87000
    def m1(self):
        print("Product_Id is:",A_class.product_id)  #Public_access_modifier
        print()
        print("Product_Name is:",A_class._product_name) #protected access modifier
        print()
        print("Product_Price is:",A_class.__product_price)  #private access modifier
        print()
a1=A_class()
a1.m1()  #Instance_method
print()
print("Product_Id is:",A_class.product_id) 
print()
print("Product_Name is:",A_class._product_name) 
print()
print("Product_Price is:",A_class.__product_price)   #private access modifier can be acceptable within class
print()
time.sleep(2)
print("end of an application")