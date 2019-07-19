# Parse an HTML table and write to a CSV

import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
url = "http://www.espncricinfo.com/india/content/player/253802.html"
# response = requests.get(url)
# print(response.text)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
# print(html)
table = soup.select_one("table.engineTable")
# for i in table:
#     print(i)
header = [th.text for th in table.select("tr th")]
value = [[td.text for td in row.select("td")]  for row in table.find_all("tr")]
print(value)
with open('Virat Kohli.csv', 'w') as f:
    wr = csv.writer(f)
    wr.writerow(header)
    wr.writerows(
        [[td.text for td in row.select("td")] for row in table.find_all("tr")][1:]
    )

"""
html = open("http://www.espncricinfo.com/india/content/player/253802.html").read()
soup = BeautifulSoup(html)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)

with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)
"""

tensorflow