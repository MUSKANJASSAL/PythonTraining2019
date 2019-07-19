import requests
from bs4 import BeautifulSoup # External Library for Parsing HTML Data
import matplotlib.pyplot as plt
import numpy as np

url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/women/batting"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("a", class_="text-hvr-underline text-bold cb-font-16")

Batting = []

for tag in tags:
    # print(tag.text)
    # print("------")

    data = tag.text
    Batting.append(data.strip())


for W_Bat in Batting:
    print(W_Bat)
    print("*******")

print(Batting)

rates = soup.find_all("div", class_="cb-col cb-col-17 cb-rank-tbl pull-right")

Ratings = []

for rate in rates:
    # print(tag.text)
    # print("------")

    data = rate.text
    Ratings.append(data.strip())

Ratings.sort()
print(Ratings)

for Rating in Ratings:
    print(Rating)
    print("*******")

print(Ratings)

X = Batting
Y = Ratings
#plt.plot(X,Y)
plt.xlim(0,4)
plt.bar(X, Y)
plt.ylim(0,100)
width = 0.35
plt.yticks(np.arange(0, 110, 50))
plt.xlabel("Names")
plt.ylabel("Ratings")
plt.title("Batting")
plt.show()