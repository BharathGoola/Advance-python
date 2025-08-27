import time
class A_CLASS:
    def __init__(self):
        print("Python Developer")
    def m1(self):
        print("Full Stack Python Developer")
    @classmethod
    def m2(cls):
        print("AI Engineer")
    @staticmethod
    def m3():
        print("ML & DL Developer")
class B_CLASS(A_CLASS):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
b1=B_CLASS()
print()
time.sleep(2)
print("End of an application")