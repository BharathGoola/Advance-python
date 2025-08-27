import time
class A_class:pass
class B_class(A_class):pass
class C_class(A_class):pass
class D_class(A_class):pass
print()
print("===MRO of B_CLASS===")    #mro function is to display the mro of each class
print(A_class.mro())
print()
print("===MRO of B_class")
print(B_class.mro())
print()
print("===MRO of C_class===")
print(C_class.mro())
print()
print("===MRO of D_CLASS===")
print(D_class.mro())
print()
time.sleep(2)
print("End of an application")





import time 
class A_class:pass 
class B_class:pass 
class C_class:pass 
class X_class(A_class,B_class):pass 
class Y_class(B_class,C_class):pass 
class Z_class(X_class,Y_class,C_class):pass 
print()
print("===MRO OF A_CLASS===")
print(A_class.mro())
print()
print("===MRO OF B_CLASS===")
print(B_class.mro())
print()
print("===MRO OF C_CLASS===")
print(C_class.mro())
print()
print("===MRO OF X_CLASS===")
print(X_class.mro())
print()
print("====MRO OF Y_CLASS====")
print(Y_class.mro())
print()
print("===MRO OF Z_CLASS===")
print(Z_class.mro())
print()
time.sleep(2)
print("End of an application")


