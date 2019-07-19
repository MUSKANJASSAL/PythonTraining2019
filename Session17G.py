# Vehicle Number
import re

pattern = "^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"
"""
"^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$"
^ means start of string 
[A-Z]{2} means 2 characters in the range of A through Z
\s means white space
[0-9]{2} means 2 characters in the range of 0 through 9
\s means white space
[A-Z]{2} means 2 characters in the range of A through Z
\s means white space
[0-9]{4} means 4 characters in the range of 0 through 9
$ means end of string
"""
#"^[A-Z]{2}[- ][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$"
# ^ means starting of string
# $ ending of string


finished = False

while not finished:
    vehicle_no = input("Enter your vehicle number:")
    if len(vehicle_no) == 0:
        finished = True
    else:
        if re.match(pattern, vehicle_no):
            print("Valid !!")
        else:
            print("Invalid !!")