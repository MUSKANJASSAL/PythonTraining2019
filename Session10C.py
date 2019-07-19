class CA:
    num = 100

    def __init__(self):
        #self.a = 1000
        self.num = 101

    def show(self):
        #print("No. is:", CA.num)   # 100
        #print("a is:", ca.a)       # 1000
        #print("No. is:", self.num)  # 100
        print("Num is:", CA.num)     # Accessing num using Class
        print("Num is:", self.num)   # Accessing num using Object
        #print("Num is:", ca.num)

ca = CA()
ca.show()

# Rule : Property of class can be accessed by class name
# or Ref Var of Object i.e. self
# But Property of Object is not accessible by Class

# Rule : If object has no attribute which is further available in class, object can access it !!
#        if object shall have it, object will use its own !! :)