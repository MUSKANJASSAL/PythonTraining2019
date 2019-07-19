# DEFAULT ARGUMENTS IN FUNCTION
# Right to Left

def addNumbers(num1, num2, num3=0):
    sum = num1 + num2 + num3
    print("Sum is:",sum)

print("addNumbers is:",addNumbers)    # Overwriting
addNumbers(10, 20)
addNumbers(10, 20, 30)

# Updation on Functions
def addNumbers(num1, num2, num3, num4):
    sum = num1 + num2 + num3 + num4
    print("Sum is:",sum)
print("addNumbers is:",addNumbers)