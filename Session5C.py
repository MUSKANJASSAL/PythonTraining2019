# Built-Ins on Strings

# Strings are IMMUTABLE
# Whenever we perform any modification operation on String we get a new String in memory
# No modification in Original String
name = "Fionna Flynn"
newName = name.upper()
print(name)
print(newName)

anotherName = "john watson"
anotherName = anotherName.capitalize()
print(anotherName)


anotherName = "john watson"
#an = anotherName.capitalize()
#print(an)
anotherName = anotherName.capitalize()    # Modifying
print(anotherName)

names = "John, Jennie, Jim, Jack, John, Joe"
#idx = names.index("h")
#print(idx)
idx = names.index("Jennie")
print(idx)

newNames = names.replace('J','K')
print(names)
print(newNames)

#num = names.count("J", 0, len(names))
num = names.count("John", 0, len(names))     # Occurence of some substring
print(num)

data = "John, Jennie, Jim, Jack, John, Joe"
data = names.split(",")
print(data, type(data))

print()

for n in data:        # Next line
    print(n)

print()

for n in data:        # Removes the white space
    print(n.strip())

# --------------------------  #

# Counting Words
quote = "Search the candle rather than cursing the darkness"
data = quote.split(" ")
print(data)
print(data, type(data), len(data))

# --------------------------  #

salutation ="Mr."
fname = "George"

name = salutation + fname      # Concatenation
print(name)

#  -----------------------  #

number = "100"
print(type(number))

if number.isdigit():
    n = int(number)
    print("n is:",n,type(n))
# --------------------------  #

number1 = "Hundred"
print(type(number1))

if number1.isdigit():
        n = int(number1)
        print("n is:", n, type(n))

# --------------------------  #

numb = 100
print(type(numb))

songName = "Hello.mp3"
if songName.endswith(".mp3"):   # startsWith
    print("Play the Audio File")

# Explore more String Built-Ins by using your . as intellisense
