from urllib.parse import urlencode
import csv
import requests


GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
USGS_FEED_URL = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv'


def get_quake_data():
    resp = requests.get(USGS_FEED_URL)
    data = list(csv.DictReader(resp.text.splitlines()))
    return data

def prepare_static_gmap_url(locations, widthheight='400x300', zoom='None'):
    # return URL string
    mydict = {'size': widthheight, 'maptype': 'hybrid', 'zoom': zoom}
    if type(locations) is list:
        mydict['markers'] = locations
    else:
        mydict['markers'] = [locations]
    
    url = GMAPS_URL + urlencode(mydict, doseq=True)
    return url


