technologies = ["AI", "Android", "Hadoop", "JEE"]
technologies[1] = "Mobile Apps"       # Update/Set Operation in List
print(technologies)

print()

del technologies[2]

print(technologies)
print(technologies[2])

print(technologies[0:2])
print(technologies[-1])
print(technologies[-2])
print(technologies[-3])
print(technologies[-1:-3])
print(technologies[-3:-1])

data = [1, 2, 3, 4, 5, "John", "Jennie", "Jim", "Jack","John", "Joe"]
data.pop(3)  # Removes on the basis of indexing
print(data)

data.remove(3)   # Removes on the basis of value(Removes the matching element)
print(data)

data.remove("John")   # 1st time in existence
print(data)