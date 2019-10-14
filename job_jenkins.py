import requests
from bs4 import BeautifulSoup
import pandas as pd

# target URL to scrap
url = "http://anamika.englab.juniper.net:8080/job/Nuthan_contrail_command/"

# headers
headers = {
    'Authorization': "Basic YnVpbGRlcjpidWlsZGVyQDEyMw=="
}

# send request to download the data
response = requests.request("GET", url, headers=headers)

# parse the downloaded data
data = BeautifulSoup(response.text, 'html.parser')
print(data.find_all('ul'))
# print(data.find_all("h1", attrs={'class', 'job-index-headline page-headline'})[0].text)

# tags = data.find_all('div', attrs={'class','status'})
# print(tags)
# for tag in tags:
#     print(tag)
