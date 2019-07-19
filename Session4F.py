"""
cart = []

foodItem = input("Enter a Food Item of your Choice: ")

cart.append(foodItem)
"""
cart = ["dal", "paneer"]
print(cart)
print()

cart.append("sizzler")
print(cart)
print()

cart.extend(["noodles", "manchurian"])
print(cart)
print()

cart.insert(1, "tacos")
print(cart)
print()

cart.remove("paneer")
print(cart)

cart.pop(1)
print(cart)

# HW: Use all the above operations by taking inputs from User

list = []
choice = "yes"
while choice == "yes":
    foodItem = input("Enter a Food Item of your Choice: ")
    list.append(foodItem)
    choice = input("Would you like to add food item in list (yes/no):")
print(list)
list.append("waffles")