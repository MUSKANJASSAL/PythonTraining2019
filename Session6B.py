# Whatever we write in Python file is executed automatically line by line
# Automatic: main thread(Execution Context) in the process
#print(__name__)

def anyName():
    print("Hello")
    print("This is a Good Day !")

if __name__=="__main__":
    anyName()