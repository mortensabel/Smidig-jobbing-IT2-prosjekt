import requests as req

def naa(breddegrad, lengdegrad):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={breddegrad}&lon={lengdegrad}"
    resultat = req.get(url, headers = {'User-Agent': 'Morten'})
    data = resultat.json()
    return data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
naa(59.89, 10.52)

def langtidsvarsel(breddegrad, lengdegrad):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={breddegrad}&lon={lengdegrad}"
    resultat = req.get(url, headers = {'User-Agent': 'Morten'})
    data = resultat.json()
    return data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
langtidsvarsel(59.89, 10.52)













