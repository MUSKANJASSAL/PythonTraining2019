"""names = ["John", "Fionna", "Kia"]
names[0] = "John Watson"     # Modify the data
print(names)"""

# IMMUTABLE TUPLE
names = ("John", "Fionna", "Kia")
#names[0] = "John Watson"    # Modify the data
#names.append("Kim")
print(names)

# Converted Tuple into Lists
newNames = list(names)
print(newNames, type(newNames))

# HW: Session4 till last: Explore on Tuples and Sets