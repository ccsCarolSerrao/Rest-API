import requests
from pprint import pprint
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

city = "RioDeJaneiro"
country = "Brasil"
appid = "20bdc8631a3328e58276f82057cca93d"
'''For temperature in Fahrenheit use units=imperial
#For temperature in Celsius use units=metric
#Temperature in Kelvin is used by default, no need to use units parameter in API call
'''
units = "metric"

def main():
    '''Using Open Weather Map API
    http://openweathermap.org/
    '''
    #http://openweathermap.org/
    url = "http://api.openweathermap.org/data/2.5/weather?{}"
    params =    { 'q':      city + ',' + country,
                'appid':  appid,
                'units':  units
                }
    params =  urlencode(params)
    resp = requests.get(url.format(params))
    weather = resp.json()
    #pprint(weather)

    print("The weather for", weather['name'])
    print(weather['main']['temp'])
    print(weather['weather'][0]['description'])

if __name__ == "__main__":
    main()
    