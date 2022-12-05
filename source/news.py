import requests, json


class News():

  def get_articles(self):
    url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=a25042a25c9c4b8ea055c44cb2228b12"

    response = json.loads(requests.get(url)._content.decode('utf-8'))
    headlines = []
    for articles in response['articles'][0:10]:
      headlines.append(articles['title'])

    return headlines
