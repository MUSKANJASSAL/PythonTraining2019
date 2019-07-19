# Logical Operators

physics = 85
chemistry = 90
maths = 80

print("Can student be an engineer? ", (maths>physics and maths>chemistry))
print("Can student be an physist? ", (physics>maths or physics>chemistry))

# not ! -> Implement not

x = 5
print(not(x>3 and x<=10))

a = True
print("NOT a is:", (not a))