"""

    Object Oriented Programming Language
    OOPS
    > Object
    > Class

        1. Encapsulation
        2. Abstraction
        3. Inheritance
        4. Polymorphism

    Real World:

        Object: is anything which you can see and touch
                Which is Real -> Real Time Entity

        Class: is drawing of an object
               is representation how an object will look like
               OOPS Principle
               1. Think of an Object
               2. Draw Object
               3. Create Real Object by looking Drawing

        Computer Science:
            Object: Multi value container (for customization)
            Class: Textual Representation of Object

        eg: Geometry Box
            All Pencils                 |HOMO
            Pencils, Eraser, Sharpner   | HETRO

            User is an Object
            User has lot of data associated with it
                name
                phone
                email
                gender
                age
                address
                .
                ..

            Identification of Object
            Requirement: User should register in m app.
            User should enter source and destination loction and book a cab.
            User should be allocated a Driver to complete a ride.

            Model View Controller
            Model -> Object

            Driver: name, pjone, email, license, experience...
            Cab: brand, type, color, regNum...
            Ride: source, destination, user, cab, driver

            Data associated with object in attributes

"""

class User:
    pass        # empty

class Driver:
    pass

data = []
print(type(data))

# 1. Object Construction Statement
u = User()
v = User()
d = Driver()

print(type(u))
print(type(v))
print(type(d))

print(u)
print(v)
print(d)

# 2. Write Data in Object
u.name = "John"
u.phone ="=91 99999 88888"
u.email = "john@example.com"
u.address =" Redwood Street"

u.name = "Fionna"
v.age = 30
v.salary = 30000

# Reference Copy
w = v

print(w)

d.name = "George"
d.phone = "=91 99900 88800"
d.email = "george@example.com"
d.experience = "3"
d.license = "PBXS314"

# 3. Update Operation
u.name = "John Watson"
#v.age = 33  |  w.age = 33

# 4. Delete Operation
del u.phone
del d.license

# 5. Read Operation or Object
print(u.__dict__)
print(v.__dict__)
print(d.__dict__)

class MyClass:
  x = 5
print(MyClass)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()