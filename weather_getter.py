import requests, json

accu_search_url = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=DlwYnYFYBSB7Uy8UAfQ61e1AtNkONA1p&q="

city = "aarhus"

r = requests.get(accu_search_url+city)
data = r.json()
print(data[0]["Key"])
key = data[0]["Key"]

accu_12hour_url = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" + key + "?apikey=DlwYnYFYBSB7Uy8UAfQ61e1AtNkONA1p&metric=true"

weather = requests.get(accu_12hour_url)
weather = weather.json()

for item in weather:
    print(item["DateTime"][-14:-6])
    print(item["IconPhrase"])
    print(str(item["Temperature"]["Value"]) + " degrees celcius")
    print(str(item["PrecipitationProbability"]) + "% chance of rain")
