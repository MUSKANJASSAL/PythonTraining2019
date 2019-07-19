# STRING LITERALS

a = "Hello, World!"   # PS: First character has the position 0
print(a[1])

print(len(a))      # The len() method returns the length of a string

print(a.lower())    # The lower() method returns the string in lower case

print(a.upper())    # The upper() method returns the string in upper case

print(a.replace("H", "J"))    # The replace() method replaces a string with another string
#print(a.replacE("Hello", "HI");

print(a.split(","))    # returns ['Hello', ' World!']
                       #The split() method splits the string into substrings if it finds instances of the separator:

print(a.split(" "))

b = "Hello World!"   # Get the characters from position 2 to position 5 (not included)
print(b[2:5])