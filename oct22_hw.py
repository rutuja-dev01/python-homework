
class A : 

    # Class variable
    p = 10

    # Constructor
    def __init__(self,b):
        self.var = b

obj = A(99)

# TASK1 : prove both the statements are same & stored in same location
print("A.p :",A.p, "| ID :",id(A.p))                        # Accessing by, class var        
print("obj.p :",obj.p, "| ID : ",id(obj.p))                 # Accessing by, obj var


# TASK2 : prove why both the 'y' are same and why 'x' is different
obj.p = 12345
print("\nA.p :",A.p, "| ID : ",id(A.p))                     # x
print("obj.p :",obj.p, "| ID : ",id(obj.p))                 # y


obj2 = A(33)
print("\nobj2.p :",obj2.p, "| ID : ",id(obj2.p))            #y
