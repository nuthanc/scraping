import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

#variables
build = '1910'

# target URL to scrap
url = "http://10.204.217.152:5000/v2/contrail-vrouter-agent/tags/list"

# headers

# send request to download the data
response = requests.request("GET", url)

# parse the downloaded data
data = BeautifulSoup(response.text, 'lxml')
# print(type(data.find_all('p')))
# print(type(data.find('p').text))
parsed_dict = json.loads(data.find('p').text)
count = 0
max = 0
for tag in parsed_dict['tags']:
    if build in tag and [string.isnumeric() for string in tag.split("-")]:
        id = tag.split("-")[1]
        # For branch build
        if len(id) <= 2:
            if int(id) > max:
                max = int(id)
            print(tag)
            print(id)
            count += 1

# print("Count:", count)
print("Max:", max)
