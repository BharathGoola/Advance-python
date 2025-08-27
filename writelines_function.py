import time
f3=open("A3.txt","w")
# L1=[1001,"mobile_1",68000.0,"samsung"]   write() argument mustbe string, not int
L1=["1001\n","Mobile_1\n","68000.0\n","Samsung\n"]
f3.writelines(L1)
print()
print("A File is created Successfully...")
print()
f3.close()
print()
time.sleep(2)
print("End of an application")


import time 
f1=open("A10.txt","w")
L1=["1001\n","Mobile_1\n","23000\n","Samsung\n"]
L2=["1002\n","Mobile_2\n","24000\n","Samsung\n"]
L3=["1003\n","Mobile_3\n","25000\n","Samsung\n"]
L4=["1004\n","Mobile_4\n","26000\n","Samsung\n"]
f1.writelines(L1)
f1.writelines(L2)
f1.writelines(L3)
f1.writelines(L4)
print()
print("A file is created successfully ...")
print()
f1.close()
print()
time.sleep(2)
print("End of an application")