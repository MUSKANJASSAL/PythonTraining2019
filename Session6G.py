# Passing Values
def squareOfNum(num):
    square = num * num
    print("Square of {} is {}".format(num, square))

def squareOfNum(num):
    num = num * num
    print("Square is {}".format(num))

n = 11
# squareOfNum(num=n):
squareOfNum(n)
print("n is:",n)

# Modifying num will not change n

def addNumbers(a, b, c):
    d = a + b + c

addNumbers(10, 20, 30)
addNumbers(a = 10, c = 20, b = 30)