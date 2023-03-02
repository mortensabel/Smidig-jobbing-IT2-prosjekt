import requests as req
import geocoder


def naa(sted):
    g = geocoder.arcgis(sted)
    liste = []
    lat = g.json["lat"]
    lng = g.json["lng"]
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lat}&lon={lng}"
    resultat = req.get(url, headers = {'User-Agent': 'Morten'})
    data = resultat.json()
    liste.append(sted)
    liste.append(data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])
    liste.append(data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed"])
    return liste
    #return data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]

















