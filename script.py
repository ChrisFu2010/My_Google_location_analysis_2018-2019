import json
import csv

from datetime import datetime

with open("Location History/Location History.json") as google_places:
    places_data = json.load(google_places)

# print(places_data)

location_log = []

for item in places_data['locations']:
    location_dataPoints = {}
    location_dataPoints['Latitude'] = item['latitudeE7']/10000000
    location_dataPoints['Longitude'] = item['longitudeE7']/10000000
    location_dataPoints['Time'] = datetime.fromtimestamp(
        int(item['timestampMs'])/1000).strftime('%Y-%m-%d %H:%M:%S')
    print(location_dataPoints)
    location_log.append(location_dataPoints)


fields = ['Latitude', 'Longitude', 'Time']

test_dic = {'Latitude': '38.6521027', 'Longitude': '-122.5998661',
            'Time': '2020-07-10T17:49:48Z'}

with open("output_data.csv", "w") as output_test:
    writer = csv.DictWriter(output_test, fieldnames=fields)

    writer.writeheader()
    for item in location_log:
        writer.writerow(item)
