# Dictionary

employees = {"name":"John","eid":101,"email":"john@example.com","salary":300000}
print(employees, type(employees))
print(len(employees))
print("Max:",max(employees))    # Works on Keys(Homogeneous)
print("Min:",min(employees))

employees["name"] = "John Watson"   # Update Operation
print(employees)
print(employees["name"])

#keys = employees.keys()
#values = employees.values()

keys = list(employees.keys())
values = list(employees.values())

print(keys, type(keys))
print(values, type(values))

# In Dictionary we have Keys as Unique !!
# But Values can be duplicated

for key in keys:
    print(key, employees[key])


dishes = {"dish1":100, "dish2":200, "dish3":300}
print(dishes, type(dishes))
print("Max:",max(dishes))
print("Min:",min(dishes))
print(dishes["dish3"])
print(dishes.keys())
print(dishes.values())


# PS: KEYS ARE ALWAYS UNIQUE IN DICTIONARY BUT VALUES CAN BE DUPLICATED
# HW: Explore Dictionary in Dictionary, Set in Set
# dishes. -> Explore more Built Ins :)
# Set in Dictionary and Dictionary in List etc etc....
# newsapi.org