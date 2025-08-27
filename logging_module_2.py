import time
import logging
logging.basicConfig(filename="obj2.txt",format="%(asctime)s:%(levelname)s:%(message)s",level=logging.DEBUG,datefmt="%d/%m/%Y %I:%M:%S %p",filemode="w")
print("---A Request With Problem For Solutions---")
try:
    x1=int(input("Enter the x1_value:"))
    x2=int(input("Enter the value of x2:"))
    res1=x1//x2
    print("The Result_Set is:",res1)
except ZeroDivisionError as e:
    print("Exception_Name is:",e)
    logging.exception(e)
print()
print("Request Processed Successfully")
print()
time.sleep(2)
print("End of an application")