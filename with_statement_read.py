import time
with open("A12.txt","r") as f1:
    # obj1=f1.read()
    # obj1=f1.read(12)
    obj1=f1.readlines()
    print(obj1)
    print()
    print("Data is read successfully from the file")
print()
time.sleep(2)
print("End of an application")



import time
with open("A12.txt","r") as f1:
    for x1 in f1:
        print(x1,end="")
    print()
    print("A Data is Read Successfully...")
print()
time.sleep(2)
print("End of an application")