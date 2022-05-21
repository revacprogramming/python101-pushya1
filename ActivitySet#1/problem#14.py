# Using Web Services
# https://www.py4e.com/lessons/servces
"""
#import re
import urllib.request, urllib.parse,urllib.error
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


fhand = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_1546810.xml')
text = fhand.read()
t_r=text.decode()
tree = ET.fromstring(t_r)
lst = tree.findall('.//count')
li = list()
for one in lst:
    d=int(one.text)
    li.append(d)
print(sum(li))
"""

#ans: 2395


"""
import json
import urllib.request, urllib.parse,urllib.error

fhand = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_1546811.json')
text = fhand.read().decode()
info = json.loads(text)
li = list()
for item in info['comments']:
    x=item['count']
    li.append(x)
sum(li)
"""
#ans: 2453

import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    place_id = js["results"][0]["place_id"]
    print(place_id)


    #ans:ChIJSXQyV43NvYcRdRt537z5Zg0
