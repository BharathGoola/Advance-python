import time
with open("A12.txt","w") as f1:
    L1=["1001\n","Bharath_1\n","89000\n","TCS\n"]
    L2=["1002\n","Bharath_2\n","98000\n","TCS\n"]
    L3=["1003\n","Bharath_3\n","120000\n","TCS\n"]
    f1.writelines(L1)
    f1.writelines(L2)
    f1.writelines(L3)
    print()
    print("A File is Created Sucessfully...")
print()
time.sleep(2)
print("End of an application")