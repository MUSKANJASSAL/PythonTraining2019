"""
	Sequences in Python
		List
		Tuple
		String
		Set
		Dictionary
	Operations on Sequence :
		1. Concatenation
		2. Repetition
		3. Membership Testing
		4. Slicing
		5. Indexing
"""

# SEQUENCES
# LIST IN PYTHON

students = ["John", "Jennie", "Jim", "Jack", "Joe"]
print(students, type(students))

# 1. Concatenation
print(students +  ["Fionna", "George"])
print(students)   # No change in the original list with concatenation operator "+"
print()

# 2 . Repetition
print(students * 2)
print(students)         # No change in the original list
print(students * 3)     # Shopping Cart
print(students)
print()

# 3. Membership Testing
print("John" in students)

# 4. Indexing
print(students[2])

# 5. Slicing
print(students[1:4])      # 1-inclusive and 4-exclusive

# Lists, Tuples, Strings, Sets and Dictionaries