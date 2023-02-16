import requests as req
import geocoder


def naa(sted):
    g = geocoder.arcgis(sted)
    lat = g.json["lat"]
    lng = g.json["lng"]
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lat}&lon={lng}"
    resultat = req.get(url, headers = {'User-Agent': 'Morten'})
    data = resultat.json()
    return data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]

















