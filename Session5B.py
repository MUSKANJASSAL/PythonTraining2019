# String Formatting

name = "Fionna"
age = 31
print("Welcome to our club %s"%(name))
print("Your age is %d"%(age))

print("Hey. %s You are %d years old"%(name, age))
print("Hey",name,"You are",age,"years old")
print("Hey" +name)
print("Hey " +name)

print("Hey, {} You are {} years old".format(name, age))

# Table of a number

num = int(input("Enter a number:"))
for i in range(1,11):
    print("{} * {} = {}".format(num, i, (num*i)))

number = 7
for i in range(1, 11):
    print("{} {}'s are {}".format(number, i, number*i))