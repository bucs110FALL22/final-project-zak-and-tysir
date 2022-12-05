import requests, json, random


class Quotes():

    def get_quote(state=None):
        headlines = []
        url = "https://zenquotes.io/api/quotes"
        response = json.loads(requests.get(url)._content.decode('utf-8'))

        for resp in response:
            headlines.append(resp['q'])
        random.seed(len(headlines))
        get_index = random.random()
        return headlines[int(get_index)]
