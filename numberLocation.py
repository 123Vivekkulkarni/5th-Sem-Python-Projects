import phonenumbers

# from myNumber import number

from phonenumbers import geocoder

number = '+917975251112'
MyNumber = phonenumbers.parse(number)

Location = geocoder.country_name_for_number(MyNumber, 'en')
print(Location)

# Get Service Provider
from phonenumbers import carrier

Service_Provider = phonenumbers.parse(number)
print(carrier.name_for_number(Service_Provider, 'en'))

# Finding Latitude and Longitude

from opencage.geocoder import OpenCageGeocode

Key = '8bf1e9ad059b4cb49e7f4feabe1fa03c'

geocode = OpenCageGeocode(Key)

query = str(Location)

Result = geocode.geocode(query)

# print(Result)

lat = Result[0]['geometry']['lat']

lng = Result[0]['geometry']['lng']

print(lat, lng)

# displaying place in map and putting marker in that location using folium

import folium

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker(location=[lat, lng], popup=Location).add_to(myMap)

# save map in html file

myMap.save('myLocation.html')
