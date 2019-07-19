# IPL DATA
import pandas as pd

Teams = ["Rajasthan Royals",
         "Deccan Chargers",
         "Chennai Super Kings",
         "Chennai Super Kings",
         "Kolkata Knight Riders",
         "Mumbai Indians",
         "Kolkata Knight Riders",
         "Mumbai Indians",
         "Sunrisers Hyderabad",
         "Mumbai Indians",
         "Chennai Super Kings",
         "Mumbai Indians"
         ]

Ranks = [2, 3, 3, 5, 1, 6, 1, 1, 3, 4, 4, 5]

Years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(len(Teams))
print(len(Ranks))
print(len(Years))

# frame = pd.DataFrame({
#     "Team" : Teams,
#     "Rank" : Ranks,
#     "Year" : Years
# })
data = {
    "Team" : Teams,
    "Rank" : Ranks,
    "Year" : Years
}
frame = pd.DataFrame(data)

print("***********************************************")
print(frame)
print("***********************************************")

print("-----Group by Teams-----")
group = frame.groupby("Team")
print(group)
print(group.groups) # In the form of Dictionary
print("------------------------")

# print("-----Group by Teams, Ranks-----")
# group = frame.groupby("Team", "Rank")
# print(group)
# print(group.groups)
# print("-------------------------------")

print()

print("-----Iterate in Group-----")
# We are getting Unique Teams

group = frame.groupby("Team")

for teamName, grp in group:
    print(teamName)
print("--------------------------")

print("-----Group by Team-----")

print(group.get_group("Chennai Super Kings"))

print("-----------------------")

# HW: Cricket World Cup Table
