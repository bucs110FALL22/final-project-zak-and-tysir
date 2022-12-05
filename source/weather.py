import requests, json


class Weather():

  def get_alerts(self, state='NY'):
    headlines = []
    url = "http://api.weather.gov/alerts/active?area=NY"
    response = json.loads(requests.get(url)._content.decode('utf-8'))
    if 'features' in response:
      for x in response['features'][0:5]:
        headlines.append(x['properties']['headline'])
      if len(headlines) == 0:
        headlines.append('No Weather Alerts')
      return headlines
    else:
      return ['No Alerts']
