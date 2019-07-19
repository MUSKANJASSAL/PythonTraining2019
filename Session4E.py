#data = ["C++", "Java", "Python", 90, 80, 90]   # Heterogenous
#length = len(data)
#print(length)

"""print(len(data))
print(max(data))
print(min(data))"""

data1 = [10, 20, 90, 80, 90]    # Homogeneous
print(len(data1))
print(max(data1))
print(min(data1))

"""
data2 = ["C++", "Java", "Python"]      # Homogeneous
print(len(data2))
print(max(data2))   # Order sequence of Dictionary/ASCII
print(min(data2))
"""

# Iteration in List
print("=======")
for i in range(len(data1)):  # Regular for loop
    print(data1[i])
print("=======")
print()

# Enhanced for Loop/ For-Each Loop
for elm in data1:      # Read All Operation
    print(elm)
print("=======")
print()

data3 = [1, 2, 3, 4, 5]
print([x**2 for x in data3])   # Exponential
print()

print([x*3 for x in data3])
print([x+3 for x in data3])
print([x%2 == 0 for x in data3])

numbers = list(range(1,101))
print(numbers)