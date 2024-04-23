"""request isnt inbuilt in python """

import requests
import json
from bs4 import BeautifulSoup

query = "algorithms"
url = "https://google.com/search?q=" + query
r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")
data = {}
for h3 in soup.find_all("h3"):
    name = h3.text

    while h3.name != "a":
        h3 = h3.parent

    f = filter(lambda x: x.startswith("q="), h3.attrs["href"].split("?")[1].split("&"))
    url = list(f)[0].split("=")[1]

    data[url] = name
data_json = json.dumps(data, indent=4)
print(data_json)
