import time
with open("A10.txt","r") as f:
    print("===File_Information===")
    print("File_Name is:",f.name)
    print("File_Mode is:",f.mode)
    print("File_Closed:",f.closed)
    print("File is Readable",f.readable())
    print("File is writable or not:",f.writable())
print()
time.sleep(2)
print("End of an application")


import time 
with open("A10.txt","r") as f:
    print("===File_Information===")
    print("File_Name is:",f.name) 
    print("File_Mode is:",f.mode)
    print("File_Closed",f.closed)
    print("File is Readable:",f.readable())
    print("File is writable or not:",f.writable())
print()
print("File_Closed:",f.closed)
print()
time.sleep(2)
print("End of an application")