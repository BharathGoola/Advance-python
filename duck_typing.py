import time
class I_HUB_IT_SERVICES:
    def developers(self):
        print("Developers are develop the application bussiness Logic")
    def UI_Developers(self):
        print("UI Developers develop the FrontEnd of web applications")
    def Angular_developers(self):
        print("Angular Developers develop the ERP web")
    def tester(self):
        print("Testers are test the code or debug the code")

i1=I_HUB_IT_SERVICES()
i1.developers()
i1.UI_Developers()
i1.Angular_developers()
i1.tester()
print()
time.sleep(2)
print("End of an application")

import time
class Calculator_class:
    def Add(self,x1,x2):
        self.x1=x1
        self.x2=x2
        return self.x1+self.x2
    def Division(self,y1,y2):
        self.y1=y1
        self.y2=y2
        return self.y1/self.y2
    def mul(self,z1,z2):
        self.z1=z1
        self.z2=z2
        return self.z1*self.z2
c1=Calculator_class()
print("Sum is:",c1.Add(580,560))
print()
print("Division is:",c1.Division(100,2))
print()
print("Multiplication is:",c1.mul(12,18))
print()
time.sleep(2)
print("End of an application")
