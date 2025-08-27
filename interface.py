import time
from abc import *
class IHUB_App_Store(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
class MYSQL_DB(IHUB_App_Store):
    def m1(self):
        print("Connecting to MYSQL_DB for Indian_users")
    def m2(self):
        print("Disconnecting to MYSQL_DB for Indian_users")
class Mongo_DB(IHUB_App_Store): 
    def m1(self):
        print("Connecting to MongoDB for USA_users")
    def m2(self):
        print("Disconnecting to MongoDb for USA_user")
class PostGRESQL(IHUB_App_Store):
    def m1(self):
        print("Connecting to postGRESQL for China_users")
    def m2(self):
        print("Disconnecting to postGRESQL for China_users")
DB_Name=input("Enter the database name:")
x1=globals()[DB_Name]
obj1=x1()
obj1.m1()
print()
time.sleep(3)
obj1.m2()
print()
time.sleep(2)
print("End of an application")