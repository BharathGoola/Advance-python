import time
def test_case2(test_case1):
    def inner(name):
        if(name=="Python"):
            print(name,":Meant for general purpose application Development")
        else:
            test_case1(name)
    return inner

def test_case1(name):
    print("Name of the Language:",name)
decorfunction=test_case2(test_case1)
if(__name__=="__main__"):
    test_case1("Python")
    print()
    decorfunction("Python")
print()
time.sleep(2)
print("End of an application")



           

import time
def test_case2(test_case1):
    def inner(name):
        # if(name=="python"):
          if(name=="Python"):
            print(name,":meant for General purpose application Development")
          elif(name=="javaScript"):
              print(name,":Meant For Clientside Validation")
          elif(name=="Sql"):
              print(name,":Meant For Database Operations")
          else:
            test_case1(name)
    return inner
@test_case2
def test_case1(name):
    print("Name of the language is:",name)
if(__name__=="__main__"):
    test_case1("Python")
    print()
    test_case1("JavaScript")
    print()
    test_case1("Sql")
print()
time.sleep(2)
print("End of an application")


import time
def test_case2(test_case1):  #new function
    def inner(x1,x2):
        if (x2==0):
            print(x2,":Upcoming Software engineer how can divide a number with 0 Sorry...")
        else:
            return test_case1(x1,x2)
    return inner
        

@test_case2
def test_case1(x1,x2):  #exisisting function
    return x1//x2
if(__name__=="__main__"):
    print(test_case1(10,2))
    print()
    print(test_case1(150,15))
    print()
    print(test_case1(100,10))
    print()
    print(test_case1(1000,0))
    print()
    print(test_case1(2000,100))
    print()
    print(test_case1(1200,200))
    print()
    print()
    print(test_case1(2000,200))
print()
time.sleep(2)
print("End of an application")