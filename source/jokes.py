import requests, json


class Jokes():

  def get_joke(self):
    url = "https://official-joke-api.appspot.com/random_joke"
    response = json.loads(requests.get(url)._content.decode('utf-8'))
    '''
    {
      "id":207,
      "type":"general",
      "setup":"What do you call a cow with no legs?"
      ,"punchline":"Ground beef."
    }
    '''
    headlines = []
    for item in response:
      if item == 'setup':
        headlines.append('   Question:  ' + response['setup'])
      if item == 'punchline':
        headlines.append('   Answer:  ' + response['punchline'])
    if len(headlines) == 0:
      headlines.append('No Jokes for ')

    return headlines
