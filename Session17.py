import json  # Java Script Object Notation
# String Represenattion of Dictionary

employee = {"eid":101, "name":"John", "salary":30000}
print(employee)
print(type(employee))

print()

# Convert Dictionary into JSON
# NewsAPI
# JSON is a textual i.e. String representation of Dictionary
# Marshing and Unmarshing

jsonData = json.dumps(employee)   # By Default Double Quotes
print(jsonData)
print(type(jsonData))

print()

# jsonData = str(employee)
# print(jsonData)
# print(type(jsonData))

# Get the json data i.e. string format of dictionary
# and convert it into Dictionary

dictData = json.loads(jsonData)
print(dictData)
print(type(dictData))