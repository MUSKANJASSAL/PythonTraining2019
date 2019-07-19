# Converting string as list
quote = "Work Hard Be Luckier"
#data = list(quote)
#data = tuple(quote)
#data = set(quote)
#data = dict(quote)     -> TRY TO EXPLORE IT!
# Only when you have key and value
#print(data)

print(quote*2)    # Replication
#print(quote[::-1])     # Reverse
#print(quote.replace())    # Not Working

for i in range(0, len(quote)):
    #print(quote[i])
    print(quote[i], end=" ")

print()

for i in range(len(quote)-1,-1,-1):
    print(quote[i], end=" ")