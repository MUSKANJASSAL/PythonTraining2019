"""
print(">> App Started")

numbers = [10, 20, 30, 40, 50]
a = 10; b=3; c=0
c = a//b

print(numbers[3])
# print(numbers[30])
print("c is:",c)

print(">> App Finished")
"""
print(">> App Started")

numbers = [10, 20, 30, 40, 50]

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = 0
idx = int(input("Enter Index to View Data: "))

try:
    print(numbers[idx])
    c = a // b
# except IndexError as iRef:
#     print("Some Error Occurred:",iRef)
# except ZeroDivisionError as zRef:
#     print("Some Error Occurred:",zRef)
except Exception as eRef:
    print("Some Error Occurred:", eRef)
finally:  # it will be executed regardless if the try block raises an error or not
    print("This is Awesome")

print("c is:", c)

print(">> App Finished")

# Graceful/Normal Termination of Program
# Line#1 till end of line was executed :)

# AbNormal Termination of Program / Run Time Error
# Crash in Program :)

#print(x)  # NameError
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:  # else keyword to define a block of code to be executed if no errors were raised
  print("Nothing went wrong")
"""
    try:  
    # block of code   
    # this may throw an exception  
    finally:  
    # block of code  
    # this will always be executed   
"""

"""
    try:
        ...
    except:
        ...
    finally:
        ... 

    try:
        ...
    except:
        ...
    except:
        ...
    finally:
        ...   

    try:
        try:
            ...
        except:
            ...
        finally:
            ...   
    except:
        try:
            ...
        except:
            ...
        finally:
            ...  
    finally:
        try:
            ...
        except:
            ...
        finally:
            ...   



     Exception                  : Parent Class
         ZeroDivisionError      : Children to Exception 
         IndexError
         .
         ..
         .....    

"""