"""

     Student
        name
        phone
        email
        password
        isCollegeTraining    # Boolean
        collegeName
        rollNum

"""

"""
class Student:
    pass

s1 = Student()

s1.name = "John"
s1.phone = "+91 99999 777777"
s1.email = "john@example.com"
s1.password = "pass123"
s1.isCollegeTraining = True
s1.collegeName = "ABC International"
s1.rollNum = 24

print(s1.__dict__)

s2 = Student()

s2.fullName = "Jack"
s2.phone = "+91 99999 56777"
s2.email = "jack@example.com"
s2.passphrase = "pass123"
s2.isCollegeTraining = True
s2.collegeName = "ABC International"
s2.rollnm = 24

print(s2.__dict__)

Student = [s1, s2]

"""

# Challenge: No Standardization
# Solution: Constructors

class Student:

    schoolName = "ATPL"

    # self is a reference varibale which will hold hascode of current object
    # __init__ is known as Constructor
    # Condtructor is property of class
    def __init__(self, name, phone, email, password, isCollegeTraining, collegeName, rollNum):
        print("<<self is:",self)
        self.fullName = name
        self.phone = phone
        self.email = email
        self.password = password
        self.isCollegeTraining = isCollegeTraining
        self.collegeName = collegeName
        self.rollNum = rollNum

    # Over-Writing -> A new constructor will be created and old will be removed
    # Overloading does not happen
    #def __init__(self, name, phone):
        #self.name = name
        #self.phone = phone

    def showStudentDetails(self):    # Function inside Class
        print("Details of:",self.fullName)
        print("Phone:",self.phone)

# s1 = Student()   # Student.__init__(s1)
s1 = Student("John","+91 99999 777777","john@example.com","pass123",True,"ABC International",14)
print("s1 is:",s1)

s2 = Student("Jack","+91 99899 777007","jaack@example.com","pass023",True,"ABC International",9)
print("s2 is:",s2)

print(s1.__dict__)
print(s2.__dict__)

s1.age = 22
s1.vehicleName = "PB10AB1234"

s1.fullName = "John Watson"
s2.fullName = "Fionna Flynn"

print(s1.__dict__)
print(s2.__dict__)

#del s1.age
#del s1.phone
#print(s1.__dict__)

s1.showStudentDetails()   # Student.showStudentDetails(s1)
s2.showStudentDetails()

print()

Student.showStudentDetails(s1)
Student.showStudentDetails(s2)

print()

print(s1.__dict__)
print(Student.__dict__)

# Right hand side properties are of Constructor
# Left hand side properties are of the Object (Creating attribute inside Object)