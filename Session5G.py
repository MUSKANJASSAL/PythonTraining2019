S = {1, 2, 3, 'A', 'B'}
print(S, type(S))
S.add('C')
print(S)

S.remove('A')
S.remove(1)

print(S)

S.pop()    # First element in the set is popped out
print(S)

S.clear()
print(S)

data = [10, 20, 30]
data.clear()
print(data)

# name = "John"
# name.clear()
# print(name)