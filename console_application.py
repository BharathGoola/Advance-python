import time
f1=open("A10.txt","r")
print("===========================")
print("File_name is:",f1.name)
print("===========================")
# obj1=f1.read()
# obj1=f1.read(19)  read character from file
# obj1=f1.readline()   read only line from file
obj1=f1.readlines()   #read one line and perform operation,it return data in list
print(obj1)
print()
f1.close()
print()
time.sleep(2)
print("End of an application")



import time
f1=open("A10.txt","r")
print("========================")
print("File name is:",f1.name)
print("========================")
obj1=f1.readlines()
for x1 in obj1:
    # print(x1)
    print(x1,end="")
print()
f1.close()
print()
time.sleep(2)
print("End of an application")