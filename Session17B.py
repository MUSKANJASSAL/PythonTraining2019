# Regular Expression
import re

# https://www.vogella.com/tutorials/JavaRegularExpressions/article.html
quote = "Search the Candle Rather than cursing the Darkness"
# result = re.match("Search", quote) # match from starting
# result = re.match("Candle", quote)
# result = re.search("the", quote)
result = re.findall("the", quote)    # Returns a list containing all matches
print(result)
print(type(result))

print()

# data = re.split("the", quote)   # Returns a list where the string has been split at each match
# print(data)

data = re.sub("the", "a", quote)   # Replaces one or many matches with a string
print(quote)
print(data)

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")
