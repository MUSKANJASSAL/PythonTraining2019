# Web Service for Weather : https://openweathermap.org/api
# Web Service for News : https://newsapi.org/
# APIKey = f5ca389b50614443a19e979493d6e764
# import requests
import requests as rq
import json as js

#url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f5ca389b50614443a19e979493d6e764"
response = rq.get(url)
# print(response.text)
# print(type(response))

newsData = js.loads(response.text)
print(newsData)

# JSON Parsing
print(newsData['articles'][0])
print(newsData['articles'][0]['source']['name'])
print(newsData['articles'][0]['author'])
print(newsData['articles'][0]['title'])

url_list = ["list1", "list2", "list3", "list4"]
list1 = "https://newsapi.org/v2/everything?q=bitcoin&from=2019-05-27&sortBy=publishedAt&apiKey=f5ca389b50614443a19e979493d6e764"
list2 = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f5ca389b50614443a19e979493d6e764"
list3 = "https://newsapi.org/v2/everything?q=apple&from=2019-06-26&to=2019-06-26&sortBy=popularity&apiKey=f5ca389b50614443a19e979493d6e764"
list4 = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=f5ca389b50614443a19e979493d6e764"
response = rq.get(url_list)
print(response.text)
print(type(response))