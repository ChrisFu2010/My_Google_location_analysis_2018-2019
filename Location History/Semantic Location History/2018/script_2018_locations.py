import json
import csv

from datetime import datetime

with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2018/2018 _location_compile.json") as google_places:
    places_data = json.load(google_places)
'''
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_FEBRUARY.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_MARCH.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_APRIL.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_MAY.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_JUNE.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_JULY.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_AUGUST.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_SPETEMBER.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_OCTOBER.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_NOVEMBER.json") as google_places:
    places_data = json.load(google_places)
with open("/Users/macbookpro/Desktop/py/my_map_project2/Location History/Semantic Location History/2019/2019_DECEMBER.json") as google_places:
    places_data = json.load(google_places)
'''
# print(places_data)

location_log = []


for item in places_data['timelineObjects']:

    location_dataPoints = {}
    if "placeVisit" in item:
        # geolocation and time
        location_dataPoints['Latitude'] = float(
            item['placeVisit']["location"]['latitudeE7']/10000000)
        location_dataPoints['Longitude'] = float(
            item['placeVisit']["location"]['longitudeE7']/10000000)
        location_dataPoints['Time'] = datetime.fromtimestamp(
            int(item['placeVisit']["duration"]['startTimestampMs'])/1000).strftime('%Y-%m-%d %H:%M:%S')

# address
        location_dataPoints['Address'] = item['placeVisit']["location"]['address'].replace(
            "\n", " ,")
# name
        if 'name' in item['placeVisit']["location"]:
            location_dataPoints['Name'] = item['placeVisit']["location"]['name']

        location_log.append(location_dataPoints)


print(location_log)

# location_dataPoints['Latitude'] =
# print(int(timelineObjects['placeVisit']
#          ['location']['latitudeE7'])/10000000)
# location_dataPoints['Longitude'] = int(
#   inner_item['placeVisit']['location']['longitudeE7'])/10000000
# location_dataPoints['Time'] = datetime.fromtimestamp(
#   int(inner_item['timestampMs'])/1000).strftime('%Y-%m-%d %H:%M:%S')
# print(location_dataPoints)
# location_log.append(location_dataPoints)


fields = ['Latitude', 'Longitude', 'Time', "Address", "Name"]


with open("output_data_2018_WHOLE_YEAR.csv", "w") as output_test:
    writer = csv.DictWriter(output_test, fieldnames=fields)

    writer.writeheader()
    for item in location_log:
        writer.writerow(item)
