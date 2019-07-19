print(">> App started")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = 0

try:
    try:
        c = a +b
        print(">> First",c)
    except Exception as eRef:
        print("Some Error Occurred:", eRef)
    finally:
        print("First try-except block")
    c = a / b
    print(">> Second",c)
except Exception as Ref:
    print("Some Error Occurred:", Ref)
finally:
    print("Second try-except block")

print(">> App Finished")