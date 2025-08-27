import time
from threading import*
def Test_Case1():
    for x1 in range(10):
        time.sleep(1)
        print("Generative AI Application Development")
if(__name__=="__main__"):
    t1=Thread(target=Test_Case1)
    t1.start()
    for y1 in range(10):
        time.sleep(1)
        print("1. Python|Flask|Open_AI|Tools|Numpy|Pandas|Javascript|FastAPI")
print()
time.sleep(2)
print("End of an application")