name = "John Watson"
print(name, type(name), hex(id(name)))
print(len(name))
print("Max:",max(name))
print("Min:",min(name))

print(name[1])
print(name[len(name)-1])    # Last Index

print(name[1:3])         # Slicing

print("t" in name)       # Membership Testing

name1 = "JohnWatson"
print(name1, type(name1), hex(id(name1)))
print(len(name1))
print("Max:",max(name1))
print("Min:",min(name1))


email = "john@example.com"

if "@" in email and "." in email:     # In as Membership Testing
    print("Valid email!")
else:
    print("Not valid")


"""
email = "john@example.com"

if ("@" in email) and ("." in email):
    print("Valid Email")
else:
    print("Invalid Email")
"""

# HW: Create a Program to Test a Member in a Sequence
# Your program should work on List, Tuple, String