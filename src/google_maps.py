import requests
import os
from dotenv import load_dotenv
import urllib.parse
import json

load_dotenv()

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_address(place):
    place_url = urllib.parse.quote(place)

    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_url}&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key={API_KEY}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)

    formatted_address = data['candidates'][0]['formatted_address']

    return formatted_address

def get_coordinates(place):
    place_url = urllib.parse.quote(place)

    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_url}&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key={API_KEY}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)

    lat = data['candidates'][0]['geometry']['location']['lat']
    lng = data['candidates'][0]['geometry']['location']['lng']

    return lat, lng


print(get_address("Amtsgericht Aichach"))
print(get_coordinates("Amtsgericht Aichach"))
