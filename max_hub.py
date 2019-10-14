import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

#variables
build = '1910'

# target URL to scrap
url = "https://hub.juniper.net/v2/contrail-nightly/contrail-vrouter-agent/tags/list"

# headers
headers = {
    'Authorization': "Basic Sk5QUi1DdXN0b21lcjIwMDpGU2cwdkxXXjdvTSNHWnk4SnUqZg=="
}

# send request to download the data
response = requests.request("GET", url, headers=headers)

# parse the downloaded data
data = BeautifulSoup(response.text, 'lxml')
# print(type(data.find_all('p')))
# print(type(data.find('p').text))
parsed_dict = json.loads(data.find('p').text)
count = 0
max = 0 
for tag in parsed_dict['tags']:
    if build in tag and '.' in tag and '-' not in tag:
        id = tag.split(".")[1]
        # For branch build
        if len(id)<=2:
            if int(id)>max:
                max=int(id)
            print(tag)
            print(id)
            count+=1

# print("Count:",count)
print("Max:",max)
