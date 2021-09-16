# Imports:

from urllib.parse import quote
from urllib.request import urlopen
from json import loads, dumps


# API Key:

api_key = ''  # if you have a Google Places API key, paste it here
# https://developers.google.com/maps/documentation/geocoding/overview

if not api_key:
    service_url = 'http://py4e-data.dr-chuck.net/json?key=42&address='
else:
    service_url = f'https://maps.googleapis.com/maps/api/geocode/json?key={api_key}&address='


# Main:

print('\nADDRESS FORMATTER')

while True:

    # Input:

    address = input('\nEnter Location: ').strip()
    if not address:
        exit('Exiting...')

    print('Loading...')

    # Processing:

    url = service_url + quote(string=address)  # proper url
    url_handle = urlopen(url=url)
    data = url_handle.read().decode()
    js = loads(s=data)  # parsing

    # print(dumps(obj=js, indent=4))  # debugging

    # Output:

    status = js['status']
    if status == 'OK':
        print('Formatted Location:', js['results'][0]['formatted_address'])
    else:
        print('Error:', status)
