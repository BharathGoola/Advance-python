import time
f1=open("A10.txt","r")
print("=========================")
print("File_name is:",f1.name)
print("==========================")
obj1=f1.readlines()
for x1 in obj1:
    print(x1,end="")
f1.close()
print()
time.sleep(2)
print("End of an application")



import time
f1=open("A10.txt","r")
for x1 in f1:
    print(x1,end="")
f1.close()
print()
time.sleep(2)
print("End of an application")