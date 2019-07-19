# FUNCTIONS
# f(x) = x*x
# f(2) = 2*2 = 4
# METHODS/ PROCEDURES/ ROUTINES
"""
    FUNCTION
    1. Name
    2. Inputs (May or May Not) | Parameters | Arguments
    3. return (May or May Not) | Acknowledgement
    4. Definition (May or May Not) -> Sequence

    LOOP
        Where we write statements which are repeated again and again

    Why Functions ?
        Group of Statements / logic which has to be executed again and again

    Modularization is something which we are doing in our program to simplify the process
"""

# Definition of Function: addNumbers
# num1 and num2 are inputs
def addNumbers(num1, num2):
    num3 = num1 + num2
    # print("Sum of {} and {} is {}".format(num1, num2, num3))
# Execution of addNumbers Function
addNumbers(10, 20)
#addNumbers(20, 33)
#addNumbers(45, 78)
#addNumbers(-12, 76)

"""
def addNumbers(num1, num2):
    num3= num1 + num2
    return num3
result = addNumbers(10, 20)
print("Sum is:",result)
print(addNumbers(20, 33))
print("Sum is:",addNumbers(45, 78))
"""


# defining the function
def func(name):
    print("Hi ", name);
# calling the function
func("Ayush")


# python function to calculate the sum of two variables
# defining the function
def sum(a, b):
    return a + b;
# taking values from the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
# printing the sum of a and b
print("Sum = ", sum(a, b))

#the function simple_interest accepts three arguments and returns the simple interest accordingly
def simple_interest(p,t,r):
    return (p*t*r)/100
p = float(input("Enter the principle amount? "))
r = float(input("Enter the rate of interest? "))
t = float(input("Enter the time in years? "))
print("Simple Interest: ",simple_interest(p,r,t))