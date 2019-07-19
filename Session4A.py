# SEQUENCES
# TUPLES IN PYTHON

students = ("John", "Jennie", "Jim", "Jack", "Joe")
print(students, type(students))

# 1. Concatenation
print(students + ("Fionna", "Henna"))
print(students)
"""print(students + ("George"))     # Not Applicable
print(students)"""

# 2. Repetition
print(students *2)
print(students)

# 3. Membership Testing
print(("Jim" in students))

# 4. Indexing
print(students[2])

# 5. Slicing
print(students[1:4])