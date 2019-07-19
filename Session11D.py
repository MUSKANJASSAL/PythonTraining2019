# BUIT-IN FUNCTION
#file = open("Session11.py", "r") # Read Mode
# file = open("/Users/ishantkumar/Downloads/MyApp.py","r")
file = open("C:/Users/vb/Desktop/Training/Python/Auribises/FILES/My.py","r")
print(type(file))

fileContents = file.read()
print(type(fileContents))

print()

print(fileContents)
print(len(fileContents))  # 1 character is 1 byte in memory

print(">> Re-Read File")

# Re-Read the File
fileContents = file.read()    # Re-read
print(fileContents)


# Once a File is Opened and Read, we cannot re-read it !!
# You need to re-open and re-read

# HW: Read a Python File and Create a Dictionary which will
# tell us how many classes and Objects exist
# Keys will be Class Name and Values will be Object Count