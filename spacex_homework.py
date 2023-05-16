import requests
from bs4 import BeautifulSoup
from math import radians, cos, sin, asin, sqrt

url = 'https://api.spacexdata.com/v4/launches'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = requests.get(url, headers=headers)
launches = data.json()

access_token = "pk.eyJ1IjoibGluY3hsbiIsImEiOiJjbDluMHppMjIwMTR5NDBtejl3NjNueGdyIn0.DLAhnub2hn2okIq0gwCJEw"

def distance(lat1, lat2, lon1, lon2):
     
    # Modul matematika bermuat fungsi bernama
    # radian yang mengonversi dari derajat ke radian.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # formula Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius bumi dalam kilometer. Gunakan 3956 untuk mil
    r = 6371
      
    # kalkulasikan hasil
    return(c * r)

for launch in launches:
    launchpad_id = launch['launchpad']
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    data = requests.get(launchpad_url, headers=headers)
    launchpad = data.json()
    
    date = launch['date_utc']
    full_name = launchpad['full_name']
    
    long1 = launchpad['longitude']
    lat1 = launchpad['latitude']
    
    geo_url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{full_name}.json?access_token={access_token}"
    
    geo_response = requests.get(geo_url)
    geo_json = geo_response.json()
    center = geo_json['features'][0]['center']
    
    long2 = center[0]
    lat2 = center[1]
    
    dist = distance(lat1, lat2, long1, long2)
    
    print('\ndate: ', date, '\n', 'fullname: ', full_name, '\n', 'distance: ', dist, '\n')
    