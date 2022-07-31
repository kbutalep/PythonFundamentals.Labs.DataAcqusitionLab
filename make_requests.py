import json
import urllib.request
import requests


offset = 1
token = 'zNAcumGiNNGpKzBIzmUpQJElLKxZZTet'

for i in range (39):
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?offset=" + str(offset) + "&limit=1000"

    response = requests.get(url, headers={'Token': token})
    data = response.json()
    output_f= f"locations_" + str(i) + ".json"
    json_file = open(output_f, 'w')
    json.dump(data, json_file)
    json_file.close()
    offset += 1000

