import pandas as pd

nums1 = [10, 20, 30, 40, 50]
nums2 = [11, 22, 33, 44, 55]

student1 = {"roll":101, "name":"John", "age":20}
student2 = {"roll":201, "name":"Fionna", "age":22}
student3 = {"roll":301, "name":"Kia", "age":24, "address":"Redwood Shores"}

frame1 = pd.DataFrame([nums1, nums2])
frame2 = pd.DataFrame([student1, student2, student3])

print(frame1)
print()

#Column Wise
# Access Columns
print(frame2)

print()
print(frame1[0])
print()
print(frame2["name"])

# Access Data of Row in a cloumn
# Column-Row
print(frame2["name"][0])
print(frame2["age"][0])
print(frame2["roll"][0])

# Explore Slicing
# How it works rows and columns

print(frame1[0:2])
print(frame2[0:2])