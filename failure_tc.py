import requests
from bs4 import BeautifulSoup
import re
#variables

# target URL to scrap
url = "http://10.204.216.50/Docs/logs/1911-1_2019_10_22_19_06_42/junit-noframes.html"

# headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

# send request to download the data
response = requests.request("GET", url, headers=headers)

# parse the downloaded data
data = BeautifulSoup(response.text, 'html.parser')
# print(data.find("tr",{"class":"Error"}).prettify()) 
error_tc = data.find_all("tr", {"class": "Error"})
print(len(error_tc))
for case in data.find_all("tr", {"class": "Error"}):
    fm = (case.find('td').text).split("[")[0].split(".")[1]
    print(fm)

print("\nLocation of test cases\n")
test_cases = set()


for code in data.find_all("code"):
    cases = re.findall(r'/contrail-test/s.*py',code.text)
    for case in cases:
        test_cases.add(case)
        
for tc in test_cases:
    print(tc)


# with open('error_tc.html','w') as f:
#     for case in data.find_all("tr", {"class": "Error"}):
#         f.write(case.prettify())

