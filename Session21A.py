import requests
from bs4 import BeautifulSoup # External Library for Parsing HTML Data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# url = "https://www.imdb.com/india/top-rated-indian-movies/"
url = "https://www.imdb.com/chart/top"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

movies_Tags = soup.find_all("td", class_="titleColumn")
# print(movies_Tags)
movies = []

for tag in movies_Tags:
    # print(tag.text)
    # print("------")
    data = tag.text
    movies.append(data.strip())
print(movies)

rating_Tags = soup.find_all("td", class_="ratingColumn imdbRating")
ratings = []

for tag in rating_Tags:
    data = tag.text
    ratings.append(data.strip())
print(ratings)

Years = []
for year in movies:
    Years.append(year.split("  ")[-1].split("\n")[1])

print(Years)

movies_Name = []
for movie in movies:
    movies_Name.append(movie.split("  ")[-1].split("\n")[0])

print(movies_Name)

rating1 = pd.DataFrame(ratings, columns=["ratings"], dtype=float)
rating1["name"] = movies_Name
rating1["year"] = Years

rating2 = rating1.sort_values("ratings", ascending=False)
plt.figure(figsize=(12, 8))

ax = rating2["ratings"][:10].plot(kind="bar")
ax.set_xticklabels(rating2["name"][:10])

plt.ylim(8, 10)
plt.xlabel("YEAR", fontsize=15)
plt.ylabel("RATING", fontsize=15)

rects = ax.patches
year_labels = rating1["year"][:10]

for rect, label in zip(rects, year_labels):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height, label, ha="center", va="bottom"
    )

plt.show()
# tags = soup.find_all("span", class_="secondaryInfo")
# years = []

# for tag in tags:
#     # print(tag.text)
#     # print("------")
#
#     data = tag.text
#     years.append(data.strip())
#
# years.sort()
# #print(years)
#
# for year in years:
#     print(year)
#     print("**********")
#
# print(years)