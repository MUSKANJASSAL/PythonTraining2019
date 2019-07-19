import requests
from bs4 import BeautifulSoup # External Library for Parsing HTML Data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

url = "https://www.tripadvisor.in/Restaurants-g297664-Ludhiana_Ludhianar_District_Punjab.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("div", class_="item name")

Names = []
for tag in tags:
    # print(tag.text)
    # print("------")
    data = tag.text
    Names.append(data.strip())

print(Names)

Rates = soup.find_all("a", class_="review_count")

Reviews = []
for Rate in Rates:
    # print(tag.text)
    # print("------")
    data = Rate.text
    Reviews.append(data.strip())

Ratings = []
for rate in Reviews:
    Ratings.append(rate.split("  ")[-1].split(" ")[0])

print(Ratings)

# Review1 = pd.DataFrame(Reviews, columns=["Reviews"], dtype=float)
# Review1["Reviews"] = Reviews
# Review2 = Review1.sort_values("Reviews", ascending=False)
# plt.figure(figsize=(12, 8))
# ax = Review2["Reviews"][:10].plot(kind="bar")
# ax.set_xticklabels(Review2["name"][:10])
Review1 = pd.DataFrame(Reviews, columns=["Reviews"], dtype=str)
Review1["Reviews"] = Ratings
Review2 = Review1.sort_values("Reviews", ascending=False)
plt.figure(figsize=(12, 8))
ax = Review2["Reviews"][:10].plot(kind="bar")
ax.set_xticklabels(Review2["name"][:10])
plt.ylim(8, 10)
plt.xlabel("Restaurant Names", fontsize=10)
plt.ylabel("Reviews", fontsize=10)
plt.title("Restaurants")

# rects = ax.patches
# for rect in zip(rects):
#     height = rect.get_height()
#     ax.text(
#         rect.get_x() + rect.get_width() / 2, height, label, ha="center", va="bottom"
#     )
plt.show()
"""
pos = np.arange(len(X))
plt.bar(pos, Y, align='center', alpha=0.5)
plt.xticks(pos, X)
"""