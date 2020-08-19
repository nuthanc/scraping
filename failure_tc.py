import requests
from bs4 import BeautifulSoup
import re
#variables

# target URL to scrap
url = input("Enter url to parse:")
# headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

# send request to download the data
response = requests.request("GET", url, headers=headers)

# parse the downloaded data
def parse_data():
    data = BeautifulSoup(response.text, 'html.parser')
    # print(data.find("tr",{"class":"Error"}).prettify()) 
    error_class_html = data.find_all("tr", {"class": "Error"})
    with open('log.html','w') as f:
        f.write(str(error_class_html))
    print(len(error_class_html))
    for error in error_class_html:
        case = (error.find_all('td'))
        test_case_with_class = case[0].text
        test_case = case[0].text.split("[")[0].split(".")[1]
        # import pdb;pdb.set_trace()
        if test_case.startswith('test'):
            loc = re.findall(r'/contrail-test/s.*?py', case[2].text)[0]
        else:
            loc = re.findall(r'/contrail-test/.*?py', case[2].text)[0]
        print(test_case)
        print("Test case with class:", test_case_with_class)
        print("Location of test case: ",loc)
        print()

parse_data()
